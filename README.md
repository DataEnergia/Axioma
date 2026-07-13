# AXIOMA · Kit v2.2

Protocolo de governança da colaboração humano-IA. Bilíngue PT/ES: carregue **um** idioma por projeto.
Protocolo de gobernanza de la colaboración humano-IA. Bilingüe PT/ES: carga **un** idioma por proyecto.

Guia completo em PDF: [`AXIOMA-guia-v2_2.pdf`](AXIOMA-guia-v2_2.pdf).

## Mapa do kit / Mapa del kit

```text
axioma/
├── README.md                  este arquivo / este archivo
├── CHANGELOG.md               mudanças por versão / cambios por versión
├── pt/                        kit em português
│   ├── AXIOMA.md              núcleo (sempre carregado)
│   ├── bootstrap.md           ativação + intake + modo N0
│   ├── artefatos.md           templates dos artefatos
│   ├── execucao.md            SOP do executor
│   ├── modo-chat.md           adaptações para ambiente chat
│   ├── metricas.md            medição e pesquisa
│   └── glossario.md           vocabulário controlado (IDs AX-Tnn)
├── es/                        kit en español (mesma estrutura; modo chat = execucion-chat.md)
├── templates/
│   ├── dashboard.html         painel (só renderiza; não editar)
│   ├── dashboard-data.js      estado do projeto (o agente edita este)
│   ├── CLAUDE.md              template de instalação em Claude Code
│   └── hooks/commit-msg       hook Git: lint + estado atualizado
├── schemas/                   contrato dos frontmatters e do estado (JSON Schema)
├── tools/
│   └── axioma-lint.py         validador determinístico (stdlib, sem dependências)
└── exemplo/                   projeto N2 de referência, preenchido (PT nesta versão)
```

O pacote de um projeto completo (N3) tem 7 saídas: brief, skill, spec, plano, auditoria, handoff e dashboard (HTML + dados). Os nomes de arquivo dos artefatos são os mesmos nos dois idiomas (`brief.md`, `plano.md`, `auditoria.md`...) para que o lint funcione sem configuração.

## Instalação / Instalación

**Claude Code (ambiente `cli`):**
1. Copie a pasta `axioma/` para a raiz do repositório (um idioma basta).
2. Anexe o bloco de `templates/CLAUDE.md` ao `CLAUDE.md` do repositório.
3. Opcional, recomendado em N2/N3: `cp axioma/templates/hooks/commit-msg .git/hooks/commit-msg && chmod +x .git/hooks/commit-msg`
4. Inicie a sessão com o prompt de ativação de `bootstrap.md`.

**claude.ai / chat (ambiente `chat`):**
1. Crie um Projeto e suba os arquivos de um idioma como conhecimento.
2. Inicie com o prompt de ativação de `bootstrap.md`.
3. Na execução, aplique `modo-chat.md` (PT) ou `execucion-chat.md` (ES): bloco de estado no lugar do dashboard, checklist de coerência no lugar do lint, sem política Git.

## Lint

```bash
python3 axioma/tools/axioma-lint.py <diretório-do-projeto>
```

Python 3.8+, sem dependências. Erros bloqueiam fechamento de microetapa e abertura de gate (código de saída 1). O que ele verifica está documentado no cabeçalho do script e formalizado em `schemas/`. Mensagens em PT.

## Começando em 60 segundos / Empezando en 60 segundos

1. Ideia ainda solta? Prompt N0 de `bootstrap.md`. Alvo claro? Prompt de ativação + intake.
2. O planejador conduz A·X·I·O·M·A, propõe nível e ambiente; você confirma.
3. Brief aprovado → artefatos do nível → execução por microetapas com gates.
4. Nos gates: veredito + eco de julgamento (1-3 frases suas). Sem eco, o gate não fecha.
5. Encerramento: retrospectiva e, se quiser, métricas (`metricas.md`).

## Referência rápida de nível / Referencia rápida de nivel

| | N0 | N1 | N2 | N3 |
|---|---|---|---|---|
| Quando / Cuándo | ideia solta | trivial | projeto real | risco alto / handoff |
| Artefatos | intake + trilha | brief inline | brief, plano, dashboard | todos (7 saídas) |
| Lint |: |: | por microetapa | por microetapa e gate |
