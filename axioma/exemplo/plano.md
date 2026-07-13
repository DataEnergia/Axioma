---
schema: axioma/plan
version: 2
id: etl-siga-outorgas-plano
brief_id: etl-siga-outorgas
---

# Plano · ETL de outorgas solares e eólicas do SIGA/ANEEL

> Microetapas pequenas, verificáveis, com critério de saída. O ponto mais crítico (layout do CSV) é de-riscado primeiro.

## Política de autonomia
O agente executa decisões locais reversíveis dentro do brief. Tudo fora disso pausa.

## Microetapas
| ID | Nome | Faz | Critério de saída | Determinístico | Gate | Autonomia | Cobre |
|---|---|---|---|---|---|---|---|
| M0 | Setup | estrutura do repo, ambiente, download bruto do SIGA | arquivo bruto salvo com hash registrado | script download.py | não | alta | n/a |
| M1 | Sonda de layout | valida colunas esperadas, encoding e separador; falha explícita se divergir | teste de layout passa contra o arquivo baixado | pytest test_layout.py | não | alta | n/a |
| M2 | Parser e limpeza | filtra fonte solar/eólica e fase outorgada; normaliza potência em MW; gera CSV limpo + dicionário | CSV gerado; zero linhas descartadas sem log | etl.py + log de descartes | não | média | n/a |
| M3 | Validação de totais | totais por estado conferidos contra o painel público da ANEEL | diferença ≤ 0,5% por estado ou justificada linha a linha | compare_totais.py | sim: humano confere a tabela de diferenças e aprova o recorte de outorga vencida | baixa | n/a |
| M4 | Encerramento | README do dataset, retrospectiva e métricas | checklist de encerramento completo | axioma-lint | não | alta | n/a |

## Regra do determinístico
Cálculo, transformação de dados, validação e conferência numérica são feitos por código ou ferramenta, nunca por estimativa do modelo. Registrado na coluna Determinístico.

## Critério de encerramento
- [ ] microetapas concluídas
- [ ] critérios de aceite atendidos
- [ ] dashboard e auditoria atualizados
- [ ] gates aprovados com eco registrado
- [ ] lint sem erros
- [ ] pendências humanas explicitadas
