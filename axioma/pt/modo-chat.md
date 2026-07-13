# AXIOMA · modo chat: Adaptações para ambiente sem arquivos reais (v2.2)

> Carregar quando o ambiente de execução definido na fase M for `chat` (claude.ai, Projetos, ou qualquer interface sem Git e sem sistema de arquivos persistente). O protocolo não finge paridade: este arquivo declara o que muda, o que se perde e o que substitui cada mecanismo.

## Princípio

Em `chat`, o AXIOMA opera com força total como **planejador** (N0 e fases A a M, brief) e com força reduzida como **executor**. As adaptações abaixo mantêm as âncoras anti-deriva possíveis e explicitam as impossíveis, para que a perda seja consciente, nunca silenciosa.

## Tabela de equivalências

| Mecanismo em `cli` | Equivalente em `chat` | O que se perde |
|---|---|---|
| Política Git por microetapa | Nenhum. Não simular commits | Reversibilidade e histórico verificável |
| `dashboard-data.js` + `dashboard.html` | Bloco de estado (abaixo) reemitido a cada microetapa; opcionalmente um artifact único regenerado | Renderização estável; validação por lint |
| `tools/axioma-lint.py` | Checklist de coerência (abaixo), aplicado pelo executor e declarado no relatório | Garantia determinística; vira autoverificação |
| Hook pre-commit | Nenhum | Bloqueio mecânico de fechamento sem atualização de estado |
| Arquivos de artefatos | Artefatos como blocos markdown no chat ou no conhecimento do Projeto | Frontmatter ainda se usa; lint não roda |
| Carregamento modular sob demanda | Tudo já está no contexto do Projeto | Economia de contexto; risco maior de deriva: reforçar checkpoints |

## Bloco de estado (substituto do dashboard)

Reemitir ao fim de cada microetapa, sempre com a mesma estrutura:

```text
ESTADO AXIOMA · <projeto> · <data>
Nível: | Risco: | Ambiente: chat | Kit: 2.2
Microetapas: <done>/<total>  [M1 done] [M2 doing] [M3 pending·GATE]
Riscos ativos: ...
Decisões abertas: ...
Gates: <etapa> · <veredito> · eco: "<resumo>"
Métricas: rework= reopened= gates_failed= drift_events=
```

## Checklist de coerência (substituto do lint)

Aplicar ao fim de cada microetapa e antes de todo gate; declarar o resultado no relatório padrão (campo Lint: "checklist aplicado, sem inconsistências" ou listar o que foi corrigido):

- [ ] todo requisito da spec aparece na coluna Cobre de alguma microetapa (N3)
- [ ] toda microetapa com Gate: sim declara o que o humano valida e como
- [ ] os IDs do bloco de estado são exatamente os do plano
- [ ] nenhum gate consta como aprovado sem eco registrado
- [ ] o bloco de estado não contradiz nenhum registro anterior da conversa; contradição = drift_event, corrigir e contar

## Regras adicionais em chat

1. **Gates continuam obrigatórios e o eco também.** A degradação do ambiente não degrada a soberania.
2. **Regra do determinístico adaptada:** cálculo e transformação de dados usam a ferramenta de análise/execução de código da interface, quando existir; sem ferramenta, o executor declara `estimativa não verificada` junto ao número e o item entra em decisões abertas.
3. **Sessões longas:** a cada 10 turnos de execução, ou ao notar qualquer sinal de deriva, reemitir o bloco de estado e reler as regras invioláveis do núcleo.
4. **Portar para cli:** se o projeto migrar para Claude Code no meio do caminho, os artefatos do chat viram arquivos, o bloco de estado vira `dashboard-data.js` e o lint roda uma vez para certificar a migração.
