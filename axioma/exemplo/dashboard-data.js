/* AXIOMA v2.2 · estado do projeto exemplo. JSON estrito entre as chaves. */
const DATA = {
  "kit_version": "2.2",
  "lang": "pt",
  "project": "ETL de outorgas solares e eólicas (SIGA/ANEEL)",
  "level": "N2",
  "risk": "medio",
  "environment": "cli",
  "updated": "2026-07-11 16:40",
  "commit": "a3f19c2",
  "steps": [
    {"id": "M0", "name": "Setup", "status": "done", "gate": false},
    {"id": "M1", "name": "Sonda de layout", "status": "done", "gate": false},
    {"id": "M2", "name": "Parser e limpeza", "status": "done", "gate": false},
    {"id": "M3", "name": "Validação de totais", "status": "done", "gate": true},
    {"id": "M4", "name": "Encerramento", "status": "doing", "gate": false}
  ],
  "risks": [
    {"text": "mudança de layout do CSV da ANEEL (mitigado pela sonda M1)", "level": "medio"}
  ],
  "decisions": [],
  "gates": [
    {"step": "M3", "date": "2026-07-11", "verdict": "ok", "echo": "diferenças conferidas contra o painel ANEEL; só BA acima de 0,3%, justificada por outorgas suspensas"}
  ],
  "metrics": {"rework": 0, "reopened": 0, "gates_failed": 0, "drift_events": 0}
};
