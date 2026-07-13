/* AXIOMA v2.2 · estado do projeto.
   Regras: o agente edita APENAS este arquivo, nunca o dashboard.html.
   O conteúdo entre as chaves é JSON ESTRITO: aspas duplas em todas as
   chaves e strings, sem comentários dentro do objeto, sem vírgula final.
   Validado por tools/axioma-lint.py. Em divergência com auditoria.md,
   a auditoria prevalece (drift_event). */
const DATA = {
  "kit_version": "2.2",
  "lang": "pt",
  "project": "Nome do projeto",
  "level": "N2",
  "risk": "medio",
  "environment": "cli",
  "updated": "2026-07-11 00:00",
  "commit": "-",
  "steps": [
    {"id": "M0", "name": "Setup", "status": "done", "gate": false},
    {"id": "M1", "name": "Exemplo em curso", "status": "doing", "gate": false},
    {"id": "M2", "name": "Exemplo com gate", "status": "pending", "gate": true}
  ],
  "risks": [
    {"text": "Exemplo de risco monitorado", "level": "medio"}
  ],
  "decisions": [
    "Exemplo de decisão aguardando o dono"
  ],
  "gates": [],
  "metrics": {"rework": 0, "reopened": 0, "gates_failed": 0, "drift_events": 0}
};
