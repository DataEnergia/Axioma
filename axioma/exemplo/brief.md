---
schema: axioma/brief
version: 3
kit_version: "2.2"
id: etl-siga-outorgas
created_at: 2026-07-10T09:00:00-03:00
status: active
level: N2
environment: cli
risk: medio
domain: dados do setor elétrico
target: script Python reprodutível que baixa o SIGA/ANEEL, filtra usinas outorgadas de fonte solar e eólica e gera CSV limpo com dicionário de dados
target_decision: quais estados concentram capacidade outorgada ainda não construída, para priorizar a análise regional do relatório
main_hypothesis: o CSV público do SIGA é suficiente, sem necessidade de API autenticada
secondary_hypotheses:
  - o campo de fase da usina permite separar outorgada de operação sem regra manual
risks:
  - mudança silenciosa de layout do CSV da ANEEL quebra o parser
  - encoding e separador inconsistentes entre publicações
missing_evidence:
  - confirmação da data da última atualização do SIGA no portal
open_decisions:
  - manter ou não usinas com outorga vencida no recorte
delegated_to_ai:
  - estrutura do script, parser, validações, dicionário de dados
external_validation:
  - totais por estado conferidos contra o painel público da ANEEL (ferramenta, não estimativa)
epistemic_debt_risk: medio
git_policy: commit automático local por microetapa; push com aprovação
next_agent: null
sources:
  - https://dadosabertos.aneel.gov.br (SIGA)
---

# ETL de outorgas solares e eólicas do SIGA/ANEEL

## Contexto
O dono precisa de um recorte confiável das usinas solares e eólicas **outorgadas e ainda não construídas**, por estado, para um relatório regional. Existe o CSV público do SIGA; não há pipeline pronto. Tentativas anteriores em planilha quebraram por encoding e vírgula decimal.

## Alvo
Script Python + CSV limpo + dicionário de dados. Sustenta a decisão de priorização regional do relatório.

## Interrogação
Lacunas identificadas na fase I: data de corte do SIGA não confirmada; critério para outorga vencida indefinido; unidade de potência (kW vs MW) varia por coluna.

## Oposição
Pior caso tensionado: layout do CSV mudou desde a última leitura → mitigação: validação de colunas esperadas com falha explícita (nunca silenciosa). Hipótese contrária testada: "o painel público já resolve" → rejeitada: o painel não exporta o recorte com o filtro de fase necessário.

## Governança
- Nível e justificativa: N2; projeto real multi-sessão, risco médio, sem handoff externo.
- Ambiente de execução e justificativa: cli (Claude Code); precisa de Git, execução de código e lint.
- Decisões humanas: recorte de outorga vencida; aprovação dos totais contra o painel.
- Delegado à IA: parser, limpeza, dicionário, estrutura do repositório.
- Validações externas: conferência dos totais por estado contra o painel ANEEL.
- Gates previstos: M3 (validação dos totais).
- Política Git: commit local por microetapa; push com aprovação.
