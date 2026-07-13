# AXIOMA · execução: SOP do executor (v2.2)

> Carregar ao iniciar a execução (fase Ativar, N2 e N3). Este é o procedimento operacional do agente executor; o handoff pode reproduzir partes dele de propósito (redundância no ponto de uso). Ambiente `chat`: aplicar as adaptações de `modo-chat.md` por cima deste SOP.

## Procedimento de entrada

1. Ler os artefatos na ordem do handoff (ou: skill → brief → spec → plano).
2. Verificar nível, ambiente, política Git e gates no plano.
3. Copiar `templates/dashboard.html` e `templates/dashboard-data.js` para a raiz do projeto e preencher o estado inicial em `dashboard-data.js`.
4. Ambiente `cli`: instalar o hook de `templates/hooks/commit-msg` (opcional, recomendado) e rodar `tools/axioma-lint.py` uma vez para confirmar pacote íntegro.
5. Confirmar com o humano a primeira microetapa antes de começar.

## Ciclo da microetapa (sem exceção)

```text
1. Declarar o que a microetapa fará e seu critério de saída (do plano.md).
2. Executar. Precisão numérica ou lógica -> código/ferramenta, nunca estimativa.
3. Verificar o critério de saída. Falhou -> corrigir ou pausar e devolver ao humano.
4. Atualizar dashboard-data.js (obrigatório; âncora anti-deriva).
5. Atualizar auditoria.md se houve decisão, desvio ou risco novo (append-only).
6. Rodar tools/axioma-lint.py (cli). Erro -> corrigir antes de fechar; em chat,
   aplicar o checklist de coerência de modo-chat.md.
7. Commit conforme a política do nível.
8. Emitir o relatório padrão (abaixo).
```

## Política Git (proporcional ao risco; só em ambiente `cli`)

| Nível | Commit | Push |
|---|---|---|
| N1 | opcional | com aprovação |
| N2 | automático local ao fechar cada microetapa | só com aprovação humana |
| N3 | somente após o gate humano da etapa ser aprovado | só com aprovação humana |

Mensagem: `axioma(<mN>): <resultado em uma linha>`
Exemplos: `axioma(m2): camada de bloqueio com checagem de sessão e permissão` · `axioma(m4): builds free e full do conteúdo`

Regras: um commit por microetapa (não por arquivo); nunca commitar segredo ou chave; commit de gate inclui no corpo `gate: aprovado por <humano> em <data>`. Em ambiente `chat` não há Git: o equivalente é o bloco de estado de `modo-chat.md`.

## Gates humanos

Checkpoint de validação humana **durante o desenvolvimento**; não torna nada manual em produção. No gate, o executor:

1. pausa e roda o lint (cli); gate não abre com lint em erro;
2. apresenta **o que** validar e **como** (passos concretos de teste que o humano consegue seguir no ambiente dele);
3. aguarda o veredito **e o eco de julgamento**: 1 a 3 frases do humano, com as próprias palavras, explicando o que validou e por que considera correto. `ok` seco não fecha gate; se vier seco, o executor pede o eco uma vez, com a pergunta: `O que você verificou e o que te convence de que está certo?`;
4. registra o veredito e o eco literal em `auditoria.md` (tabela Gates) e o resumo em `dashboard-data.js` (campo `echo`);
5. reprovado: corrige, registra em métricas (`gates_failed`) e reapresenta.

O executor nunca marca um gate humano como aprovado e nunca redige o eco em nome do humano.

## Política de pausa (fora de gate)

Pausar e devolver ao humano quando: houver conflito entre artefatos; mudar escopo; faltar dado crítico; falhar critério de saída; surgir decisão humana não prevista; aparecer risco novo; a validação depender de julgamento humano; o lint acusar erro cuja correção exige decisão.

## Dashboard (estado derivado)

O estado vive em `dashboard-data.js`, um arquivo separado com `const DATA = { ... }` cujo conteúdo entre chaves é **JSON estrito** (aspas duplas, sem comentários, sem vírgula final). O `dashboard.html` só renderiza; nunca se edita o HTML. O lint valida o JSON e sua coerência com o plano. Campos:

- `kit_version`, `project`, `level`, `risk`, `environment` (`cli`|`chat`), `lang` (`pt`|`es`), `updated`, `commit` (hash curto ou "-")
- `steps`: `{id, name, status: pending|doing|done, gate: true|false}` (IDs iguais aos do plano)
- `risks`: `{text, level}`
- `decisions`: decisões humanas abertas
- `gates`: `{step, date, verdict: ok|fail, echo}` (echo: resumo do eco; o literal fica na auditoria)
- `metrics`: `{rework, reopened, gates_failed, drift_events}`

Quando atualizar: ao fim do planejamento; ao fim de cada microetapa; ao abrir/fechar gate; ao encerrar. Precedência: em divergência com `auditoria.md`, a auditoria vence, conta `drift_event` e o dashboard é corrigido no mesmo turno. Trinta segundos de leitura devem bastar para o coordenador saber o estado de tudo.

## Relatório padrão por microetapa

```text
Etapa:
Arquivos criados:
Arquivos modificados:
Critérios atendidos:
Desvios:
Pendências:
Lint: (sem erros | erros corrigidos: <quais> | n/a chat)
Gate humano: (sim/não; se sim, o que validar e como)
Próxima ação:
```

## Encerramento

- [ ] microetapas concluídas e critérios de aceite atendidos
- [ ] dashboard e auditoria atualizados e coerentes (lint sem erros)
- [ ] todos os gates com eco registrado
- [ ] pendências humanas explicitadas
- [ ] retrospectiva emitida: o que as métricas dizem (ver `metricas.md`) e um ajuste sugerido ao protocolo, se houver
