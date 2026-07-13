# AXIOMA · glossário (v2.2)

> Vocabulário controlado do protocolo. Cada termo tem ID estável (`AX-Tnn`), usado para referência cruzada entre idiomas e, futuramente, para formalização SKOS. IDs nunca são renumerados.

**AX-T01 · Direção (vetor humano):** critério, julgamento, responsabilidade e escolha do que importa. Indelegável.

**AX-T02 · Amplitude (campo IA):** espaço ampliado de possibilidades gerado pela IA: geração, variação, síntese, execução. Não é decisão.

**AX-T03 · A·X·I·O·M·A:** as fases do protocolo: Alinhar, eXplicitar, Interrogar, Opor, Modular, Ativar.

**AX-T04 · Intake:** template inicial preenchido pelo humano com contexto, objetivo, arquivos, fontes, restrições e ambiente.

**AX-T05 · Brief:** contrato auditável do problema formulado; fonte de verdade. Os demais artefatos o formalizam, não o reabrem.

**AX-T06 · Skill (de projeto):** instruções permanentes que dão ao executor memória de projeto: contexto, stack, convenções, comportamento.

**AX-T07 · Spec:** especificação executável derivada do brief, com requisitos e critérios de aceite verificáveis.

**AX-T08 · Plano:** microetapas com critério de saída, determinísticos, gates, autonomia e cobertura de requisitos.

**AX-T09 · Auditoria:** registro vivo e append-only de decisões, premissas, riscos, desvios, gates e validações. Fonte histórica: prevalece sobre o dashboard em divergência.

**AX-T10 · Handoff:** instrução de transferência para o agente executor.

**AX-T11 · Microetapa:** unidade mínima de execução, pequena e verificável, fechada com dashboard, lint, commit e relatório.

**AX-T12 · Gate humano:** checkpoint de validação humana durante o desenvolvimento. Não torna a produção manual. Só fecha com eco de julgamento.

**AX-T13 · Nível (N0/N1/N2/N3):** calibre de governança do projeto; determina artefatos, política Git e gates.

**AX-T14 · Regra do determinístico:** cálculo, transformação e validação numérica são feitos por código ou ferramenta, nunca por estimativa do modelo.

**AX-T15 · Deriva:** perda gradual de aderência ao protocolo em conversas longas. Mitigada pelas âncoras (dashboard, checkpoints, relatório padrão, lint).

**AX-T16 · Dívida epistêmica:** perda gradual da capacidade humana de julgar outputs por delegação excessiva.

**AX-T17 · Calibração de julgamento:** verificação contínua de que o humano consegue explicar, julgar e detectar erros no que foi produzido.

**AX-T18 · Automação cega:** alta convergência com baixa soberania. **AX-T19 · Exploração sem fechamento:** alta soberania com baixa convergência. **AX-T20 · Decisão técnica robusta:** ambas altas (o alvo).

**AX-T21 · OCI / ESI / OVI:** índices de convergência operacional, soberania epistêmica e valor operacional (ver `metricas.md`).

**AX-T22 · Eco de julgamento:** explicação do humano, com as próprias palavras (1 a 3 frases), do que validou em um gate e por que considera correto. Registrada literalmente na auditoria. Sem eco, gate não fecha.

**AX-T23 · Teatro de governança:** modo de falha em que o protocolo é formalmente seguido sem julgamento real por trás: artefatos preenchidos, gates carimbados, soberania nominal. O eco de julgamento é a defesa principal.

**AX-T24 · Ambiente de execução:** `cli` (Git e arquivos reais; mecanismos plenos) ou `chat` (interface conversacional; adaptações de `modo-chat.md`). Decidido na fase M.

**AX-T25 · Lint (axioma-lint):** verificação determinística da coerência do pacote: frontmatters, cadeia de rastreabilidade, cobertura de requisitos, ecos, estado do dashboard. Instrução sem mecanismo é a última linha de defesa, não a primeira.

**AX-T26 · Trilha de exploração:** anexo do intake gerado em N0: hipóteses consideradas, descartadas e por quê. Evita redescobrir becos sem saída na fase Interrogar.

**AX-T27 · Precedência de estado:** regra segundo a qual a auditoria (histórico) prevalece sobre o dashboard (estado derivado) em qualquer divergência; a divergência conta como drift_event.
