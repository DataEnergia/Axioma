# AXIOMA · CHANGELOG

## v2.2 (2026-07-11)

Origem: diagnóstico estruturado da v2.1 (fragilidades em ordem de gravidade: nada verificável por máquina; anti-deriva como instrução, não mecanismo; métricas frágeis para publicação; duas fontes de estado sem precedência; ausência de exemplo trabalhado; N0 descartando o raciocínio da exploração; dashboard frágil). A v2.2 implementa a Camada 1 da proposta de formalização (verificação determinística); SKOS/PROV-O e ontologia OWL ficam para quando houver corpus de execuções.

### Verificação por máquina (novo pilar)
- Nova regra inviolável 4 no núcleo: o que pode ser verificado por máquina é verificado por máquina.
- `tools/axioma-lint.py`: validador determinístico, stdlib pura. Verifica frontmatters, cadeia brief→spec→plano→dashboard→auditoria, cobertura de requisitos, gates com descrição e eco, JSON do estado, coerência de nível/risco/ambiente. Erro bloqueia fechamento de microetapa e abertura de gate.
- `schemas/`: contrato formal (JSON Schema) do brief, dos artefatos e do estado.
- Frontmatter YAML obrigatório em todos os artefatos, com `id` e `brief_id`.
- Plano ganha coluna **Cobre/Cubre** (rastreabilidade requisito→microetapa); requisito sem cobertura é erro de lint em N3.

### Anti-deriva: de instrução a mecanismo
- `templates/CLAUDE.md`: instalação em Claude Code que reapresenta as regras a cada sessão.
- `templates/hooks/commit-msg`: bloqueia commit com lint em erro e commit de microetapa sem estado atualizado.

### Estado
- O estado sai do HTML: agora vive em `dashboard-data.js` (JSON estrito), validável; `dashboard.html` só renderiza.
- Regra de precedência explícita no núcleo: auditoria (histórico, append-only) prevalece sobre dashboard (derivado); divergência = `drift_event`.

### Soberania: anti teatro de governança
- **Eco de julgamento**: gate só fecha com explicação do humano (1-3 frases, próprias palavras), registrada literalmente na auditoria e resumida no dashboard. O executor nunca redige o eco.

### Ambientes
- Fase M agora decide também o **ambiente de execução** (`cli` | `chat`); campo novo no intake e no brief.
- Novo módulo `modo-chat.md` / `execucion-chat.md`: equivalências declaradas (bloco de estado no lugar do dashboard, checklist no lugar do lint, sem Git), em vez de paridade fingida.

### N0
- Saída de N0 agora inclui a **trilha de exploração** (hipóteses consideradas/descartadas e por quê), anexada ao intake; a fase Interrogar não redescobre becos sem saída.

### Métricas
- Nota metodológica obrigatória: pesos são defaults, reporte desagregado, análise de sensibilidade ±0,05.
- `Ef` reancorado nos ecos registrados (avaliável por terceiro cego); `Cr` redefinido como proxy declarado (piso); `HEI` sem linha de base = `n/d`, sem OVI estimado.
- CSV de pesquisa ganha `versao_kit` e `ambiente`.

### Conteúdo e correções
- `exemplo/`: projeto N2 de referência preenchido (brief, plano, auditoria com eco, estado), que passa no lint.
- Glossário com IDs estáveis (`AX-T01`…`AX-T27`) e seis termos novos (eco de julgamento, teatro de governança, ambiente de execução, lint, trilha de exploração, precedência de estado).
- Anglicismo "contract" → "contrato"; contagem corrigida no README (7 saídas do pacote N3).

### Limitações conhecidas desta versão
- `exemplo/` disponível apenas em PT.
- Mensagens do lint em PT (o código de saída e a estrutura das linhas ERRO/AVISO são neutros).
- Validação do lint é estrutural: não detecta teatro de governança com estrutura correta; a defesa é o eco + avaliação cega de `Ef`.

## v2.1

Versão anterior: núcleo A·X·I·O·M·A, níveis N0-N3, 6 módulos por idioma (PT/ES), dashboard com estado embutido, métricas OCI/ESI/OVI, protocolo experimental.
