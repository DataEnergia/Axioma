---
schema: axioma/audit
version: 2
id: etl-siga-outorgas-auditoria
brief_id: etl-siga-outorgas
---

# Auditoria · ETL de outorgas solares e eólicas do SIGA/ANEEL

## Registro
- ID: etl-siga-outorgas | Data: 2026-07-10 | Humano responsável: dono | Planejador: LLM-P | Executor: LLM-E | Nível: N2 | Ambiente: cli

## Decisões tomadas
| Data | Decisão | Justificativa | Responsável |
|---|---|---|---|
| 2026-07-10 | usar CSV público, sem API | suficiente para o recorte; menos acoplamento | dono |
| 2026-07-11 | manter outorgas vencidas com flag, não excluir | preserva rastreabilidade do recorte | dono |

## Premissas ativas
- CSV do SIGA atualizado mensalmente; data de corte registrada no README do dataset.

## Riscos
| Risco | Severidade | Mitigação | Status |
|---|---|---|---|
| mudança de layout do CSV | media | sonda M1 com falha explícita | mitigado |
| encoding inconsistente | baixa | detecção na sonda M1 | mitigado |

## Log de execução
| Etapa | Data | Ação | Arquivos | Desvio | Decisão humana | Status |
|---|---|---|---|---|---|---|
| M0 | 2026-07-10 | setup e download bruto | download.py, data/raw/ | nenhum | não | done |
| M1 | 2026-07-10 | sonda de layout | test_layout.py | separador ";" e não ",": registrado, sonda ajustada | não | done |
| M2 | 2026-07-11 | parser e limpeza | etl.py, data/clean/outorgas.csv, dicionario.md | nenhum | não | done |
| M3 | 2026-07-11 | validação de totais | compare_totais.py, diffs.md | nenhum | sim (gate abaixo) | done |

## Gates
| Etapa | Data | Veredito | Eco do humano (literal, 1-3 frases) |
|---|---|---|---|
| M3 | 2026-07-11 | ok | "Conferi a tabela de diferenças contra o painel da ANEEL: só a BA passou de 0,3% e a justificativa (duas usinas com outorga suspensa) confere com o SIGA. O recorte com flag de vencida atende o relatório." |

## Alterações de escopo
| Alteração | Motivo | Aprovado por |
|---|---|---|
| nenhuma |: |: |

## Calibração de julgamento (por gate e no fechamento)
- [x] humano consegue explicar a decisão e o resultado? (eco registrado acima)
- [x] há erros não óbvios possíveis? (mitigados pela sonda M1 e comparação M3)
- [x] a IA assumiu algo como fato? (não; data de corte confirmada no portal)
- [x] critérios validados por quem sabe julgá-los?
- [x] há risco de automação cega? (baixo; conferência externa feita)

## Status final
in_progress
