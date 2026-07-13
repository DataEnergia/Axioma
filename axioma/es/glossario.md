# AXIOMA · glosario (v2.2)

> Vocabulario controlado del protocolo. Cada término tiene un ID estable (`AX-Tnn`), usado para referencia cruzada entre idiomas y, a futuro, para formalización SKOS. Los IDs nunca se renumeran.

**AX-T01 · Dirección (vector humano):** criterio, juicio, responsabilidad y elección de lo que importa. Indelegable.

**AX-T02 · Amplitud (campo IA):** espacio ampliado de posibilidades generado por la IA: generación, variación, síntesis, ejecución. No es decisión.

**AX-T03 · A·X·I·O·M·A:** las fases del protocolo: Alinear, eXplicitar, Interrogar, Oponer, Modular, Activar.

**AX-T04 · Intake:** template inicial completado por el humano con contexto, objetivo, archivos, fuentes, restricciones y entorno.

**AX-T05 · Brief:** contrato auditable del problema formulado; fuente de verdad. Los demás artefactos lo formalizan, no lo reabren.

**AX-T06 · Skill (de proyecto):** instrucciones permanentes que dan al ejecutor memoria de proyecto: contexto, stack, convenciones, comportamiento.

**AX-T07 · Spec:** especificación ejecutable derivada del brief, con requisitos y criterios de aceptación verificables.

**AX-T08 · Plan:** microetapas con criterio de salida, determinísticos, gates, autonomía y cobertura de requisitos.

**AX-T09 · Auditoría:** registro vivo y append-only de decisiones, premisas, riesgos, desvíos, gates y validaciones. Fuente histórica: prevalece sobre el dashboard en divergencia.

**AX-T10 · Handoff:** instrucción de transferencia al agente ejecutor.

**AX-T11 · Microetapa:** unidad mínima de ejecución, pequeña y verificable, cerrada con dashboard, lint, commit e informe.

**AX-T12 · Gate humano:** checkpoint de validación humana durante el desarrollo. No vuelve manual la producción. Solo cierra con eco de juicio.

**AX-T13 · Nivel (N0/N1/N2/N3):** calibre de gobernanza del proyecto; determina artefactos, política Git y gates.

**AX-T14 · Regla del determinístico:** cálculo, transformación y validación numérica se hacen por código o herramienta, nunca por estimación del modelo.

**AX-T15 · Deriva:** pérdida gradual de adherencia al protocolo en conversaciones largas. Mitigada por las anclas (dashboard, checkpoints, informe estándar, lint).

**AX-T16 · Deuda epistémica:** pérdida gradual de la capacidad humana de juzgar outputs por delegación excesiva.

**AX-T17 · Calibración de juicio:** verificación continua de que el humano puede explicar, juzgar y detectar errores en lo producido.

**AX-T18 · Automatización ciega:** alta convergencia con baja soberanía. **AX-T19 · Exploración sin cierre:** alta soberanía con baja convergencia. **AX-T20 · Decisión técnica robusta:** ambas altas (el objetivo).

**AX-T21 · OCI / ESI / OVI:** índices de convergencia operacional, soberanía epistémica y valor operacional (ver `metricas.md`).

**AX-T22 · Eco de juicio:** explicación del humano, con sus propias palabras (1 a 3 frases), de qué validó en un gate y por qué lo considera correcto. Registrada literalmente en la auditoría. Sin eco, el gate no cierra.

**AX-T23 · Teatro de gobernanza:** modo de falla en que el protocolo se sigue formalmente sin juicio real detrás: artefactos completados, gates sellados, soberanía nominal. El eco de juicio es la defensa principal.

**AX-T24 · Entorno de ejecución:** `cli` (Git y archivos reales; mecanismos plenos) o `chat` (interfaz conversacional; adaptaciones de `execucion-chat.md`). Decidido en la fase M.

**AX-T25 · Lint (axioma-lint):** verificación determinística de la coherencia del paquete: frontmatters, cadena de trazabilidad, cobertura de requisitos, ecos, estado del dashboard. La instrucción sin mecanismo es la última línea de defensa, no la primera.

**AX-T26 · Rastro de exploración:** anexo del intake generado en N0: hipótesis consideradas, descartadas y por qué. Evita redescubrir callejones sin salida en la fase Interrogar.

**AX-T27 · Precedencia de estado:** regla según la cual la auditoría (histórico) prevalece sobre el dashboard (estado derivado) ante cualquier divergencia; la divergencia cuenta como drift_event.
