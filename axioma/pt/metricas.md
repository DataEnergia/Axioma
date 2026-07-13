# AXIOMA · métricas: Medição operacional e pesquisa comparativa (v2.2)

> Carregar quando o intake pedir medição. Dois usos: (1) operacional, quase gratuito, coletado no dashboard; (2) pesquisa, para responder "usar o AXIOMA faz diferença versus outros mecanismos?".

## 1. Métricas operacionais (coletadas no `DATA.metrics` do dashboard)

| Métrica | Definição | Sinal quando alta |
|---|---|---|
| `rework` | microetapas refeitas após concluídas | brief ou plano fracos |
| `reopened` | decisões fechadas que precisaram reabrir | fases X ou M mal fechadas |
| `gates_failed` | gates reprovados na primeira tentativa | execução divergindo do plano |
| `drift_events` | reancoragens do protocolo + divergências dashboard×auditoria detectadas | núcleo perdendo força; sessões longas demais |

Derivadas do dashboard, sem coleta extra:

| Métrica | Fórmula | Mede |
|---|---|---|
| SCR | etapas `done` / etapas totais | progresso |
| GTR | etapas com gate / etapas totais | peso de governança |
| DR | desvios registrados na auditoria / etapas executadas | estabilidade |
| AEF | itens da spec cumpridos / itens totais | fidelidade do executor |

## 2. Índices compostos (avaliação por projeto; escore 0–1 por componente)

**Nota metodológica (obrigatória em uso de pesquisa).** Os pesos abaixo são defaults de desenho, não constantes validadas. Em qualquer relato de pesquisa: (a) reportar sempre os componentes desagregados, não só o índice; (b) acompanhar o índice de uma análise de sensibilidade simples (recalcular com cada peso ±0,05, redistribuindo proporcionalmente; se o ranking entre condições mudar, a conclusão não se sustenta no índice e deve descer aos componentes); (c) registrar a versão do kit, porque mudanças de protocolo quebram comparabilidade.

### OCI: Índice de Convergência Operacional

```text
OCI = 0,30·Cd + 0,25·Cn + 0,20·Cm + 0,10·Cs + 0,15·Ca   (pesos default)
```

| Comp. | Nome | Como medir (0–1) |
|---|---|---|
| Cd | decisão sustentada | o resultado respondeu à `target_decision` do brief? (rubrica: 0 não; 0,5 parcialmente; 1 sim) |
| Cn | conformidade | critérios de aceite atendidos / totais |
| Cm | fidelidade ao plano | microetapas sem desvio / totais |
| Cs | estabilidade de escopo | 1 − (alterações de escopo / microetapas) |
| Ca | auditabilidade | artefatos atualizados ao fim / artefatos exigidos pelo nível |

### ESI: Índice de Soberania Epistêmica

```text
ESI = 0,20·Jc + 0,30·Ef + 0,20·Cr + 0,15·Ar + 0,15·Dl   (pesos default)
```

| Comp. | Nome | Como medir (0–1) |
|---|---|---|
| Jc | julgamento consciente | decisões críticas tomadas pelo humano / decisões críticas totais |
| Ef | explicabilidade | avaliada sobre os **ecos de julgamento registrados na auditoria**, não sobre autorrelato: rubrica 0 (eco ausente ou vazio), 0,5 (eco genérico, não específico ao conteúdo), 1 (eco específico: cita o que foi verificado e o porquê). Pontuável por avaliador cego |
| Cr | calibração de revisão | erros detectados pelo humano em gates / erros totais **registrados na auditoria até o fechamento** (por qualquer via: humano, lint, ferramenta, terceiro). Proxy declarado: erros nunca descobertos não entram; interpretar como piso, não como valor verdadeiro |
| Ar | autonomia apropriada | 1 se a autonomia da IA ficou dentro do nível; subtrair 0,25 por violação registrada |
| Dl | devolução de decisões | decisões novas pausadas e devolvidas / decisões novas surgidas |

### OVI: Índice de Valor Operacional

```text
HEI = tempo humano com AXIOMA / tempo humano na linha de base
OVI = (OCI × ESI) / HEI
```

HEI exige linha de base medida; quando não existir, registrar `HEI = n/d` e não calcular OVI (não estimar a linha de base de memória).

Interpretação do quadrante:

```text
OCI alto + ESI baixo  = automação cega
OCI baixo + ESI alto  = exploração sem fechamento
OCI alto + ESI alto   = decisão técnica robusta  (alvo)
OCI baixo + ESI baixo = caos operacional
```

## 3. Protocolo de pesquisa comparativa

**Pergunta:** o AXIOMA melhora convergência, soberania, auditabilidade e sucesso de execução versus outros mecanismos?

**Condições:**

| Cond. | Descrição |
|---|---|
| A | prompt livre (linha de base) |
| B | só o núcleo interativo (sem artefatos) |
| C | núcleo + brief + plano (N2) |
| D | kit completo (N3) |
| E | kit completo + dashboard + métricas ativas |

**Desenho:** mesma tarefa em todas as condições; tarefas de tipos distintos (documento técnico, pipeline de dados, cálculo/EVTE, artigo, site documental); 5 execuções por condição no piloto, 10–20 no estudo forte; variar o modelo (Claude, GPT, Gemini, DeepSeek) se o objetivo incluir generalização; fixar a versão do kit durante todo o estudo.

**Coleta por execução (uma linha de CSV):**

```text
run_id, condicao, tarefa, modelo, data, versao_kit, ambiente,
OCI, ESI, HEI, OVI, SCR, DR, AEF,
Cd, Cn, Cm, Cs, Ca, Jc, Ef, Cr, Ar, Dl,
rework, reopened, gates_failed, drift_events,
tempo_humano_min, tempo_total_min, nota_qualitativa
```

**Avaliação cega:** quando possível, um avaliador (humano ou LLM distinto) pontua Cd, Ef e a qualidade do entregável sem saber a condição. Para Ef, o avaliador recebe apenas os ecos registrados e o entregável.

**Hipótese:** condições D/E aumentam OCI, ESI e sucesso de handoff, com HEI maior (mais tempo humano); o OVI revela se o ganho compensa o custo. Se OVI(D) ≤ OVI(A) em tarefas simples, é evidência para usar N1 nelas, o que o próprio protocolo já prevê.

## 4. Retrospectiva obrigatória (todo projeto N2/N3)

Ao encerrar, o executor emite um parágrafo: o que as métricas dizem, onde o protocolo ajudou ou atrapalhou, e um ajuste sugerido ao kit, se houver. Ajustes aceitos pelo humano viram nova versão do kit, registrada no `CHANGELOG.md`.
