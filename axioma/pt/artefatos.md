# AXIOMA · artefatos: Templates do pacote (v2.2)

> Carregar na fase Ativar. Gerar apenas os artefatos do nível vigente, na ordem: brief (aprovar antes de continuar) → skill → spec → plano → auditoria → handoff → dashboard. O brief é o contrato e a fonte de verdade do problema; os demais o formalizam, não o reabrem. Contradição grave devolve o projeto à fase I.

## Regras de rastreabilidade (novas na v2.2)

1. Todo artefato de arquivo tem **frontmatter YAML** com `schema`, `version`, `id` e `brief_id` (o brief referencia a si mesmo). O contrato dos campos está em `schemas/`.
2. Os identificadores formam uma cadeia verificável: requisito (`RF-nnn`/`RNF-nnn`) → microetapa (`Mn`, coluna Cobre) → gate → registro de auditoria. `tools/axioma-lint.py` verifica a cadeia; olho humano não substitui o lint.
3. IDs nunca são renumerados; item removido mantém o ID com status cancelado.

---

## 1. brief.md (todos os níveis; em N1, inline no chat)

```markdown
---
schema: axioma/brief
version: 3
kit_version: "2.2"
id: <slug-curto>
created_at: <ISO-8601>
status: open | active | done | parked
level: N1 | N2 | N3
environment: cli | chat
risk: baixo | médio | alto
domain: <domínio>
target: <o que será produzido>
target_decision: <decisão que o resultado sustenta>
main_hypothesis: <hipótese principal>
secondary_hypotheses:
  - <hipótese>
risks:
  - <risco>
missing_evidence:
  - <evidência ou validação faltante>
open_decisions:
  - <decisão humana pendente>
delegated_to_ai:
  - <operação delegada>
external_validation:
  - <o que exige ferramenta, cálculo determinístico ou especialista>
epistemic_debt_risk: baixo | médio | alto
git_policy: <conforme nível e ambiente>
next_agent: <executor ou null>
sources:
  - <fonte ou null>
---

# <Título do problema>

## Contexto
<reformulação sem dados inventados>

## Alvo
<o que será produzido e qual decisão sustenta>

## Interrogação
<lacunas, premissas ocultas, pontos que mudam o projeto>

## Oposição
<tensionamento aplicado: hipótese contrária, pior caso, o que mudou na análise>

## Governança
- Nível e justificativa:
- Ambiente de execução e justificativa:
- Decisões humanas:
- Delegado à IA:
- Validações externas:
- Gates previstos:
- Política Git:
```

---

## 2. skill.md (N3; recomendado em N2 multi-sessão)

Dá "memória de projeto" ao executor entre sessões: contexto permanente, convenções e comportamento.

```markdown
---
schema: axioma/skill
version: 1
id: <slug>-skill
brief_id: <id do brief>
---

# Skill · <nome do projeto>

## O que é o projeto
<2-4 frases: produto, domínio, estado atual, objetivo da fase>

## Papel do agente
Você é um agente executor especializado em <tipo de projeto>.

## Fontes de verdade
- Problema: `brief.md`
- Execução: `spec.md` e `plano.md`
- Estado atual: `dashboard-data.js` (derivado)
- Histórico: `auditoria.md` (precede o dashboard em divergência)

## Stack e ambiente
<tecnologias, versões, estrutura do repositório, comandos de build/teste>

## Convenções obrigatórias
<estilo, idioma, identidade visual, padrões de código, o que nunca tocar>

## Regras de comportamento
1. Não redescobrir o problema nem alterar objetivo sem autorização.
2. Não criar arquivos fora da spec sem registrar e justificar.
3. Não remover conteúdo sem confirmação.
4. Não assumir dados ausentes como fatos.
5. Executar conforme `plano.md`; pausar em gates.
6. Atualizar dashboard e auditoria conforme `execucao.md`; rodar o lint quando o ambiente for cli.

## Decisões indelegáveis
- mudança de objetivo ou escopo;
- validação técnica final;
- aprovação de premissas críticas;
- entrega final.

## Estilo de resposta
Operacional, rastreável, orientado a arquivos, sem prosa excessiva, com pendências explícitas.
```

---

## 3. spec.md (N3)

```markdown
---
schema: axioma/spec
version: 2
id: <slug>-spec
brief_id: <id do brief>
---

# Spec · <nome do projeto>

## Referência
- Fonte: `brief.md` | ID: | Risco: | Nível:

## Objetivo executável
<o que será construído ou produzido, verificável>

## Escopo
### Inclui
- ...
### Não inclui
- ...

## Arquitetura / estrutura alvo
<diagrama textual, modelo de dados, estrutura de arquivos>

## Requisitos funcionais
| ID | Requisito | Critério de aceite |
|---|---|---|
| RF-001 | | |

## Requisitos não funcionais
| ID | Requisito | Critério |
|---|---|---|
| RNF-001 | | |

## Métodos permitidos
- ...

## Métodos proibidos
- ...

## Critérios finais de aceite
- [ ] ...

## Pontos que exigem decisão humana
- ...
```

Regra: a spec formaliza o contrato; não reabre o brief salvo contradição grave.

---

## 4. plano.md (N2 e N3)

```markdown
---
schema: axioma/plan
version: 2
id: <slug>-plano
brief_id: <id do brief>
---

# Plano · <nome do projeto>

> Microetapas pequenas, verificáveis, com critério de saída. Ordem pensada para de-riscar cedo o ponto mais crítico.

## Política de autonomia
O agente executa decisões locais reversíveis dentro da spec. Tudo fora disso pausa.

## Microetapas
| ID | Nome | Faz | Critério de saída | Determinístico | Gate | Autonomia | Cobre |
|---|---|---|---|---|---|---|---|
| M0 | | | | código/ferramenta ou "não" | sim/não + o que o humano valida | alta/média/baixa | RF-nnn, RNF-nnn ou "n/a" |

Regras da coluna Cobre: em N3 (com spec), todo requisito deve aparecer em pelo menos uma microetapa; requisito sem cobertura é erro de lint. Em N2 sem spec, usar "n/a".

## Regra do determinístico
Cálculo, transformação de dados, validação e conferência numérica são feitos por código ou ferramenta, nunca por estimativa do modelo. Registrar na coluna o script ou instrumento.

## Critério de encerramento
- [ ] microetapas concluídas
- [ ] critérios de aceite atendidos
- [ ] dashboard e auditoria atualizados
- [ ] gates aprovados com eco registrado
- [ ] lint sem erros (cli) ou checklist equivalente aplicado (chat)
- [ ] pendências humanas explicitadas
```

---

## 5. auditoria.md (N3; opcional em N2)

Registro **append-only**: nada se apaga; correção é novo registro. Em divergência com o dashboard, a auditoria prevalece.

```markdown
---
schema: axioma/audit
version: 2
id: <slug>-auditoria
brief_id: <id do brief>
---

# Auditoria · <nome do projeto>

## Registro
- ID: | Data: | Humano responsável: | Planejador: | Executor: | Nível: | Ambiente:

## Decisões tomadas
| Data | Decisão | Justificativa | Responsável |
|---|---|---|---|

## Premissas ativas
- ...

## Riscos
| Risco | Severidade | Mitigação | Status |
|---|---|---|---|

## Log de execução
| Etapa | Data | Ação | Arquivos | Desvio | Decisão humana | Status |
|---|---|---|---|---|---|---|

## Gates
| Etapa | Data | Veredito | Eco do humano (literal, 1-3 frases) |
|---|---|---|---|

## Alterações de escopo
| Alteração | Motivo | Aprovado por |
|---|---|---|

## Calibração de julgamento (por gate e no fechamento)
- [ ] humano consegue explicar a decisão e o resultado? (eco registrado acima)
- [ ] há erros não óbvios possíveis?
- [ ] a IA assumiu algo como fato?
- [ ] critérios validados por quem sabe julgá-los?
- [ ] há risco de automação cega?

## Status final
open | in_progress | resolved | parked
```

---

## 6. handoff.md (N3, quando outro agente executa)

```markdown
---
schema: axioma/handoff
version: 2
id: <slug>-handoff
brief_id: <id do brief>
---

# Handoff · <nome do projeto>

## Papel
Você é o agente executor. Não redescubra o problema; os arquivos são a fonte de verdade.

## Leia nesta ordem
1. `skill.md`  2. `brief.md`  3. `spec.md`  4. `plano.md`  5. `auditoria.md`  6. `execucao.md` (SOP)

## Decisões fechadas (não reabrir)
- ...

## Por onde começar
<primeira microetapa e por quê>

## Pare e devolva ao humano quando
- chegar a um gate;
- mudar escopo ou faltar dado crítico;
- falhar critério de saída;
- surgir decisão humana não prevista;
- aparecer risco novo;
- o lint acusar erro que você não sabe corrigir sem decisão.

## Pendências do dono antes de <etapa>
- ...

## Ponto de atenção número um
<o maior risco do projeto e como não tropeçar nele>

## O que não fazer
Não alterar objetivo ou critérios de aceite; não inventar dados; não remover arquivos sem autorização; não avançar com gate aberto ou lint com erro; não commitar fora da política do nível; não marcar gate sem eco do humano.

## Relatório obrigatório por microetapa
Etapa: | Arquivos criados: | Arquivos modificados: | Critérios atendidos: | Desvios: | Pendências: | Lint: | Gate humano: | Próxima ação:
```

---

## Checklist final do planejador (antes do handoff)

- [ ] fases A·X·I·O·M·A concluídas e brief aprovado pelo humano
- [ ] artefatos do nível gerados, com frontmatter e `brief_id` corretos
- [ ] spec contém critérios de aceite verificáveis
- [ ] plano define microetapas, determinísticos, gates e cobertura (coluna Cobre)
- [ ] dashboard criado com o estado inicial em `dashboard-data.js`
- [ ] `tools/axioma-lint.py` executado sem erros (cli) ou checklist equivalente (chat)
- [ ] métricas definidas ou explicitamente dispensadas
- [ ] decisões humanas pendentes destacadas no handoff
