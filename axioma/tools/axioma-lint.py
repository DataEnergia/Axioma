#!/usr/bin/env python3
"""axioma-lint (v2.2): verificação determinística da coerência do pacote AXIOMA.

Uso: python3 tools/axioma-lint.py [diretório-do-projeto]

Verifica, sem dependências externas:
  1. frontmatter presente e campos obrigatórios por artefato (schemas/ documenta o contrato);
  2. cadeia de rastreabilidade: brief_id, requisitos (RF/RNF) da spec cobertos no plano (coluna Cobre);
  3. plano: IDs únicos, gates com descrição do que o humano valida;
  4. dashboard-data.js: JSON estrito, campos obrigatórios, IDs coerentes com o plano,
     gates aprovados com eco não vazio, métricas presentes;
  5. regras de nível: N2/N3 exigem plano; N3 exige spec;
  6. auditoria: gate aprovado no dashboard deve constar na auditoria.

Saída: linhas ERRO/AVISO. Código de saída 1 se houver ERRO; 0 caso contrário.
Erros bloqueiam fechamento de microetapa e abertura de gate (ver execucao.md).
"""
import json
import re
import sys
from pathlib import Path

REQUIRED_FM = {
    "brief.md":     ("axioma/brief", ["id", "status", "level", "risk", "environment",
                                       "target", "target_decision"]),
    "spec.md":      ("axioma/spec", ["id", "brief_id"]),
    "plano.md":     ("axioma/plan", ["id", "brief_id"]),
    "auditoria.md": ("axioma/audit", ["id", "brief_id"]),
    "skill.md":     ("axioma/skill", ["id", "brief_id"]),
    "handoff.md":   ("axioma/handoff", ["id", "brief_id"]),
}
DASH_REQUIRED = ["kit_version", "project", "level", "risk", "environment", "lang",
                 "updated", "steps", "risks", "decisions", "gates", "metrics"]
METRIC_KEYS = ["rework", "reopened", "gates_failed", "drift_events"]
REQ_ID = re.compile(r"\bR?N?F-\d{3}\b")
STEP_ID = re.compile(r"^M\d+$")

errors, warnings = [], []
err = lambda m: errors.append(f"ERRO  {m}")
warn = lambda m: warnings.append(f"AVISO {m}")


def parse_frontmatter(text, name):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        err(f"{name}: frontmatter ausente (arquivo deve começar com ---)")
        return {}
    fm, key = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            return fm
        if re.match(r"^\s*-\s+", line) and key:
            fm.setdefault(key, [])
            if isinstance(fm[key], list):
                fm[key].append(re.sub(r"^\s*-\s+", "", line).strip())
            continue
        m = re.match(r"^([A-Za-z_][\w]*)\s*:\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip().strip("'\"")
            fm[key] = val if val else []
    err(f"{name}: frontmatter não fechado (segundo --- ausente)")
    return fm


def table_rows(text, header_regex):
    """Retorna listas de células das linhas de dados da primeira tabela cujo cabeçalho casa."""
    lines, rows, inside = text.splitlines(), [], False
    for line in lines:
        if not inside and re.search(header_regex, line) and line.strip().startswith("|"):
            inside = True
            continue
        if inside:
            s = line.strip()
            if not s.startswith("|"):
                break
            if re.match(r"^\|[\s:\-|]+\|$", s):
                continue
            rows.append([c.strip() for c in s.strip("|").split("|")])
    return rows


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    if not root.is_dir():
        print(f"ERRO  diretório não encontrado: {root}")
        return 1

    fms, texts = {}, {}
    for name, (schema, required) in REQUIRED_FM.items():
        p = root / name
        if not p.exists():
            continue
        texts[name] = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(texts[name], name)
        fms[name] = fm
        if fm.get("schema") and fm["schema"] != schema:
            err(f"{name}: schema '{fm.get('schema')}' difere do esperado '{schema}'")
        for k in required:
            if not fm.get(k):
                err(f"{name}: campo obrigatório ausente ou vazio no frontmatter: {k}")

    brief = fms.get("brief.md")
    others = [n for n in fms if n != "brief.md"]
    if others and not brief:
        err("artefatos presentes sem brief.md; o brief precede todos os demais")
    if brief:
        bid = brief.get("id", "")
        for n in others:
            if fms[n].get("brief_id") and fms[n]["brief_id"] != bid:
                err(f"{n}: brief_id '{fms[n]['brief_id']}' não corresponde ao id do brief '{bid}'")
        level = brief.get("level", "")
        if level in ("N2", "N3") and "plano.md" not in fms:
            err(f"brief nível {level} exige plano.md, não encontrado")
        if level == "N3" and "spec.md" not in fms:
            err("brief nível N3 exige spec.md, não encontrado")
        if level == "N3" and "auditoria.md" not in fms:
            warn("brief nível N3 sem auditoria.md")

    # spec: requisitos
    req_ids = []
    if "spec.md" in texts:
        req_ids = sorted(set(REQ_ID.findall(texts["spec.md"])))

    # plano: microetapas
    plan_ids, covered = [], set()
    if "plano.md" in texts:
        rows = table_rows(texts["plano.md"], r"\bID\b.*\bC[ou]bre\b")
        if not rows:
            rows = table_rows(texts["plano.md"], r"\bID\b.*\bAutonom[ií]a\b")
            if rows:
                warn("plano.md: tabela de microetapas sem coluna Cobre (rastreabilidade incompleta)")
        for cells in rows:
            if not cells:
                continue
            sid = cells[0]
            if not STEP_ID.match(sid):
                warn(f"plano.md: ID de microetapa fora do padrão Mn: '{sid}'")
                continue
            if sid in plan_ids:
                err(f"plano.md: ID de microetapa duplicado: {sid}")
            plan_ids.append(sid)
            if len(cells) >= 6:
                gate_cell = cells[5].lower()
                if gate_cell.startswith("sim") and len(cells[5].strip()) <= 5:
                    err(f"plano.md: {sid} tem Gate: sim sem descrever o que o humano valida")
            if len(cells) >= 8:
                covered.update(REQ_ID.findall(cells[7]))
        if req_ids:
            missing = [r for r in req_ids if r not in covered]
            for r in missing:
                err(f"rastreabilidade: requisito {r} da spec sem cobertura em nenhuma microetapa")
        elif covered and "spec.md" not in texts:
            warn("plano.md referencia requisitos na coluna Cobre, mas não há spec.md")

    # dashboard-data.js
    dpath = root / "dashboard-data.js"
    if dpath.exists():
        raw = dpath.read_text(encoding="utf-8")
        a, b = raw.find("{"), raw.rfind("}")
        if a < 0 or b < 0:
            err("dashboard-data.js: objeto DATA não encontrado")
        else:
            try:
                data = json.loads(raw[a:b + 1])
            except json.JSONDecodeError as e:
                err(f"dashboard-data.js: conteúdo não é JSON estrito ({e})")
                data = None
            if data is not None:
                for k in DASH_REQUIRED:
                    if k not in data:
                        err(f"dashboard-data.js: campo obrigatório ausente: {k}")
                for k in METRIC_KEYS:
                    if k not in data.get("metrics", {}):
                        err(f"dashboard-data.js: metrics sem a chave: {k}")
                dash_ids = [s.get("id") for s in data.get("steps", [])]
                if plan_ids:
                    for i in dash_ids:
                        if i not in plan_ids:
                            err(f"dashboard-data.js: microetapa '{i}' não existe no plano.md")
                    for i in plan_ids:
                        if i not in dash_ids:
                            warn(f"dashboard-data.js: microetapa {i} do plano ausente no dashboard")
                for g in data.get("gates", []):
                    step, verdict = g.get("step", "?"), g.get("verdict")
                    if verdict not in ("ok", "fail"):
                        err(f"dashboard-data.js: gate {step} com verdict inválido: {verdict}")
                    if verdict == "ok" and not str(g.get("echo", "")).strip():
                        err(f"dashboard-data.js: gate {step} aprovado sem eco de julgamento")
                    if "auditoria.md" in texts and step not in texts["auditoria.md"]:
                        err(f"precedência de estado: gate {step} no dashboard sem registro na auditoria")
                if brief:
                    for field in ("level", "risk", "environment"):
                        if data.get(field) and brief.get(field) and data[field] != brief[field]:
                            err(f"dashboard-data.js: {field}='{data[field]}' difere do brief ('{brief[field]}')")
    elif plan_ids:
        warn("plano.md presente sem dashboard-data.js (obrigatório em N2/N3 antes da primeira microetapa)")

    for line in errors + warnings:
        print(line)
    print(f"\naxioma-lint: {len(errors)} erro(s), {len(warnings)} aviso(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
