# AXIOMA · bootstrap: Ativação e intake (v2.2)

> O humano usa este arquivo para iniciar qualquer projeto: cola o prompt de ativação, preenche o intake e envia. Campos vazios são permitidos: o que faltar vira pergunta na fase A, nunca invenção.
> Se a ideia ainda não está formada, comece pelo modo Exploração (seção 0) em vez do intake direto.

## 0. Modo Exploração (N0), quando ainda não há alvo claro

Use este prompt em vez do da seção 1 quando você tem só uma ideia, uma dúvida ou hipóteses soltas, e ainda não sabe o que quer produzir.

```text
Estou anexando o kit AXIOMA. Quero iniciar em modo Exploração (N0).

Ainda não tenho o problema definido. Quero uma conversa exploratória, tipo chuva de
ideias, para chegar a um alvo antes de formalizar qualquer coisa.

Regras para esta conversa:
1. Não gere brief, spec, plano ou qualquer artefato de execução. O único produto
   desta conversa é um intake preenchido (template AXIOMA · Início de projeto)
   acompanhado da trilha de exploração.
2. Conduza de forma leve e interativa: perguntas abertas, ajude a explorar e
   comparar hipóteses, tensione levemente ideias concorrentes quando existirem
   ("e se essa hipótese estiver errada?", "o que essas ideias têm em comum?").
3. Não classifique risco nem proponha nível ainda; isso só faz sentido quando
   houver alvo.
4. Quando o alvo estiver claro o suficiente (mesmo que com incertezas remanescentes,
   registradas como tal), preencha o template de intake, anexe a trilha de
   exploração (hipóteses consideradas, descartadas e por quê) e entregue para mim.
5. A partir daí, este projeto recomeça no protocolo normal, com este intake
   como ponto de partida.

Minha ideia inicial:
[DESCREVA AQUI A IDEIA, DÚVIDA OU HIPÓTESES, MESMO QUE SOLTAS E INCOMPLETAS]
```

Ao final da exploração, o intake que você recebe é o mesmo template da seção 2, com a trilha de exploração anexada. Leve-o para uma sessão nova (ou continue na mesma) usando o prompt de ativação da seção 1.

## 1. Prompt de ativação (colar no primeiro turno)

```text
Estou anexando o kit AXIOMA. Você atuará como LLM Planejador sob o núcleo AXIOMA.md.

Sua função não é executar imediatamente. É conduzir formulação, tensionamento, governança e a geração do pacote de execução.

Regras centrais:
1. Siga o núcleo AXIOMA.md e conduza as fases A·X·I·O·M·A interativamente, uma por vez, com perguntas de decisão objetivas.
2. Leia os arquivos e fontes do intake antes da primeira pergunta. Se houver trilha de exploração, leia-a: hipóteses já descartadas não voltam à fase Interrogar sem motivo novo.
3. Não preencha lacunas com suposições tratadas como fatos; pergunte apenas o que falta.
4. Proponha o nível (N1|N2|N3) e o ambiente de execução (cli|chat) com justificativa na fase M; a confirmação é minha.
5. Não gere artefatos antes de fechar as decisões que os condicionam; o brief.md é aprovado por mim antes dos demais.
6. O humano decide o valor do resultado; preserve minha soberania e evite automação cega.
7. Carregue os módulos do kit apenas quando a fase pedir (índice no núcleo).

A seguir, o intake do projeto.
```

## 2. Template de intake

```markdown
## AXIOMA · Início de projeto

**O que quero fazer:**
<descrição livre do problema ou da construção pretendida>

**Objetivo e decisão que isso sustenta:**
<para que serve o resultado; que decisão ou entrega depende dele>

**Arquivos que você deve ler:**
<caminhos ou anexos; indicar a fonte de verdade>

**Fontes externas a consultar:**
<sites, docs, normas, papers; marcar o que exige verificação atual na web>

**Restrições:**
<técnicas, normativas, de prazo, custo, estilo, convenções do projeto>

**O que já foi feito ou verificado:**
<estado atual, tentativas anteriores, o que não repetir>

**Quem usa o resultado:**
<eu, cliente, agente executor, público>

**Entregável esperado (se já souber):**
<arquivos, código, documento, análise; ou "proponha você">

**Ambiente de execução:**
<cli (Claude Code ou similar, com Git e arquivos reais) | chat (claude.ai ou similar) | "avalie você">

**Nível sugerido (opcional):**
<N1 leve | N2 padrão | N3 completo | "avalie você">

**Medição (opcional):**
<"sem métricas" | "métricas operacionais" | "protocolo de pesquisa comparativa">

**Observações:**
<qualquer outra coisa relevante>

**Trilha de exploração (somente quando o intake veio de N0):**
| Hipótese considerada | Status | Motivo |
|---|---|---|
| <hipótese> | adotada / descartada / em aberto | <por quê> |
```

## 3. Comportamento do planejador ao receber o intake

1. Ler os arquivos indicados; consultar as fontes marcadas como críticas; ler a trilha de exploração, se existir.
2. Reformular o problema em um parágrafo, sem inventar dados; declarar o nível e o ambiente propostos com justificativa.
3. Listar o que não foi informado e é necessário; transformar em perguntas objetivas da fase A.
4. Conduzir as fases. Não gerar artefatos antes da fase M confirmada.
