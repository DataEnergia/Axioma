# AXIOMA · artefactos: Templates del paquete (v2.2)

> Cargar en la fase Activar. Generar solo los artefactos del nivel vigente, en orden: brief (aprobar antes de continuar) → skill → spec → plan → auditoría → handoff → dashboard. El brief es el contrato y la fuente de verdad del problema; los demás lo formalizan, no lo reabren. Una contradicción grave devuelve el proyecto a la fase I.

## Reglas de trazabilidad (nuevas en la v2.2)

1. Todo artefacto de archivo tiene **frontmatter YAML** con `schema`, `version`, `id` y `brief_id` (el brief se referencia a sí mismo). El contrato de los campos está en `schemas/`.
2. Los identificadores forman una cadena verificable: requisito (`RF-nnn`/`RNF-nnn`) → microetapa (`Mn`, columna Cubre) → gate → registro de auditoría. `tools/axioma-lint.py` verifica la cadena; el ojo humano no sustituye al lint.
3. Los IDs nunca se renumeran; un ítem eliminado mantiene el ID con estado cancelado.

Nota de compatibilidad: los nombres de archivo del paquete son los mismos en ambos idiomas (`plano.md`, `auditoria.md`, etc.) para que el lint funcione sin configuración. El encabezado de la tabla de microetapas puede usar "Cobre" o "Cubre"; el lint acepta ambos.

---

## 1. brief.md (todos los niveles; en N1, inline en el chat)

```markdown
---
schema: axioma/brief
version: 3
kit_version: "2.2"
id: <slug-corto>
created_at: <ISO-8601>
status: open | active | done | parked
level: N1 | N2 | N3
environment: cli | chat
risk: bajo | medio | alto
domain: <dominio>
target: <qué se producirá>
target_decision: <decisión que el resultado sostiene>
main_hypothesis: <hipótesis principal>
secondary_hypotheses:
  - <hipótesis>
risks:
  - <riesgo>
missing_evidence:
  - <evidencia o validación faltante>
open_decisions:
  - <decisión humana pendiente>
delegated_to_ai:
  - <operación delegada>
external_validation:
  - <lo que exige herramienta, cálculo determinístico o especialista>
epistemic_debt_risk: bajo | medio | alto
git_policy: <según nivel y entorno>
next_agent: <ejecutor o null>
sources:
  - <fuente o null>
---

# <Título del problema>

## Contexto
<reformulación sin datos inventados>

## Objetivo
<qué se producirá y qué decisión sostiene>

## Interrogación
<lagunas, premisas ocultas, puntos que cambian el proyecto>

## Oposición
<tensión aplicada: hipótesis contraria, peor caso, qué cambió en el análisis>

## Gobernanza
- Nivel y justificación:
- Entorno de ejecución y justificación:
- Decisiones humanas:
- Delegado a la IA:
- Validaciones externas:
- Gates previstos:
- Política Git:
```

---

## 2. skill.md (N3; recomendado en N2 multi-sesión)

Da "memoria de proyecto" al ejecutor entre sesiones: contexto permanente, convenciones y comportamiento.

```markdown
---
schema: axioma/skill
version: 1
id: <slug>-skill
brief_id: <id del brief>
---

# Skill · <nombre del proyecto>

## Qué es el proyecto
<2-4 frases: producto, dominio, estado actual, objetivo de la fase>

## Rol del agente
Eres un agente ejecutor especializado en <tipo de proyecto>.

## Fuentes de verdad
- Problema: `brief.md`
- Ejecución: `spec.md` y `plano.md`
- Estado actual: `dashboard-data.js` (derivado)
- Histórico: `auditoria.md` (precede al dashboard en divergencia)

## Stack y entorno
<tecnologías, versiones, estructura del repositorio, comandos de build/test>

## Convenciones obligatorias
<estilo, idioma, identidad visual, estándares de código, qué no tocar nunca>

## Reglas de comportamiento
1. No redescubrir el problema ni alterar el objetivo sin autorización.
2. No crear archivos fuera de la spec sin registrar y justificar.
3. No eliminar contenido sin confirmación.
4. No asumir datos ausentes como hechos.
5. Ejecutar conforme `plano.md`; pausar en gates.
6. Actualizar dashboard y auditoría conforme `execucao.md`; correr el lint cuando el entorno sea cli.

## Decisiones indelegables
- cambio de objetivo o alcance;
- validación técnica final;
- aprobación de premisas críticas;
- entrega final.

## Estilo de respuesta
Operacional, trazable, orientado a archivos, sin prosa excesiva, con pendientes explícitos.
```

---

## 3. spec.md (N3)

```markdown
---
schema: axioma/spec
version: 2
id: <slug>-spec
brief_id: <id del brief>
---

# Spec · <nombre del proyecto>

## Referencia
- Fuente: `brief.md` | ID: | Riesgo: | Nivel:

## Objetivo ejecutable
<qué se construirá o producirá, verificable>

## Alcance
### Incluye
- ...
### No incluye
- ...

## Arquitectura / estructura objetivo
<diagrama textual, modelo de datos, estructura de archivos>

## Requisitos funcionales
| ID | Requisito | Criterio de aceptación |
|---|---|---|
| RF-001 | | |

## Requisitos no funcionales
| ID | Requisito | Criterio |
|---|---|---|
| RNF-001 | | |

## Métodos permitidos
- ...

## Métodos prohibidos
- ...

## Criterios finales de aceptación
- [ ] ...

## Puntos que exigen decisión humana
- ...
```

Regla: la spec formaliza el contrato; no reabre el brief salvo contradicción grave.

---

## 4. plano.md (N2 y N3)

```markdown
---
schema: axioma/plan
version: 2
id: <slug>-plano
brief_id: <id del brief>
---

# Plan · <nombre del proyecto>

> Microetapas pequeñas, verificables, con criterio de salida. Orden pensado para des-riesgar temprano el punto más crítico.

## Política de autonomía
El agente ejecuta decisiones locales reversibles dentro de la spec. Todo lo demás pausa.

## Microetapas
| ID | Nombre | Hace | Criterio de salida | Determinístico | Gate | Autonomía | Cubre |
|---|---|---|---|---|---|---|---|
| M0 | | | | código/herramienta o "no" | sí/no + qué valida el humano | alta/media/baja | RF-nnn, RNF-nnn o "n/a" |

Reglas de la columna Cubre: en N3 (con spec), todo requisito debe aparecer en al menos una microetapa; un requisito sin cobertura es error de lint. En N2 sin spec, usar "n/a".

## Regla del determinístico
Cálculo, transformación de datos, validación y verificación numérica se hacen por código o herramienta, nunca por estimación del modelo. Registrar en la columna el script o instrumento.

## Criterio de cierre
- [ ] microetapas concluidas
- [ ] criterios de aceptación cumplidos
- [ ] dashboard y auditoría actualizados
- [ ] gates aprobados con eco registrado
- [ ] lint sin errores (cli) o checklist equivalente aplicado (chat)
- [ ] pendientes humanos explicitados
```

---

## 5. auditoria.md (N3; opcional en N2)

Registro **append-only**: nada se borra; la corrección es un registro nuevo. En divergencia con el dashboard, la auditoría prevalece.

```markdown
---
schema: axioma/audit
version: 2
id: <slug>-auditoria
brief_id: <id del brief>
---

# Auditoría · <nombre del proyecto>

## Registro
- ID: | Fecha: | Humano responsable: | Planificador: | Ejecutor: | Nivel: | Entorno:

## Decisiones tomadas
| Fecha | Decisión | Justificación | Responsable |
|---|---|---|---|

## Premisas activas
- ...

## Riesgos
| Riesgo | Severidad | Mitigación | Estado |
|---|---|---|---|

## Log de ejecución
| Etapa | Fecha | Acción | Archivos | Desvío | Decisión humana | Estado |
|---|---|---|---|---|---|---|

## Gates
| Etapa | Fecha | Veredicto | Eco del humano (literal, 1-3 frases) |
|---|---|---|---|

## Alteraciones de alcance
| Alteración | Motivo | Aprobado por |
|---|---|---|

## Calibración de juicio (por gate y al cierre)
- [ ] ¿el humano puede explicar la decisión y el resultado? (eco registrado arriba)
- [ ] ¿hay errores no obvios posibles?
- [ ] ¿la IA asumió algo como hecho?
- [ ] ¿criterios validados por quien sabe juzgarlos?
- [ ] ¿hay riesgo de automatización ciega?

## Estado final
open | in_progress | resolved | parked
```

---

## 6. handoff.md (N3, cuando otro agente ejecuta)

```markdown
---
schema: axioma/handoff
version: 2
id: <slug>-handoff
brief_id: <id del brief>
---

# Handoff · <nombre del proyecto>

## Rol
Eres el agente ejecutor. No redescubras el problema; los archivos son la fuente de verdad.

## Lee en este orden
1. `skill.md`  2. `brief.md`  3. `spec.md`  4. `plano.md`  5. `auditoria.md`  6. `execucao.md` (SOP)

## Decisiones cerradas (no reabrir)
- ...

## Por dónde empezar
<primera microetapa y por qué>

## Detente y devuelve al humano cuando
- llegues a un gate;
- cambie el alcance o falte un dato crítico;
- falle un criterio de salida;
- surja una decisión humana no prevista;
- aparezca un riesgo nuevo;
- el lint acuse un error que no sabes corregir sin decisión.

## Pendientes del dueño antes de <etapa>
- ...

## Punto de atención número uno
<el mayor riesgo del proyecto y cómo no tropezar con él>

## Qué no hacer
No alterar objetivo ni criterios de aceptación; no inventar datos; no eliminar archivos sin autorización; no avanzar con gate abierto o lint con error; no commitear fuera de la política del nivel; no marcar gate sin eco del humano.

## Informe obligatorio por microetapa
Etapa: | Archivos creados: | Archivos modificados: | Criterios cumplidos: | Desvíos: | Pendientes: | Lint: | Gate humano: | Próxima acción:
```

---

## Checklist final del planificador (antes del handoff)

- [ ] fases A·X·I·O·M·A concluidas y brief aprobado por el humano
- [ ] artefactos del nivel generados, con frontmatter y `brief_id` correctos
- [ ] la spec contiene criterios de aceptación verificables
- [ ] el plan define microetapas, determinísticos, gates y cobertura (columna Cubre)
- [ ] dashboard creado con el estado inicial en `dashboard-data.js`
- [ ] `tools/axioma-lint.py` ejecutado sin errores (cli) o checklist equivalente (chat)
- [ ] métricas definidas o explícitamente dispensadas
- [ ] decisiones humanas pendientes destacadas en el handoff
