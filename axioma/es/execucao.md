# AXIOMA · ejecución: SOP del ejecutor (v2.2)

> Cargar al iniciar la ejecución (fase Activar, N2 y N3). Este es el procedimiento operacional del agente ejecutor; el handoff puede reproducir partes de él a propósito (redundancia en el punto de uso). Entorno `chat`: aplicar las adaptaciones de `execucion-chat.md` sobre este SOP.

## Procedimiento de entrada

1. Leer los artefactos en el orden del handoff (o: skill → brief → spec → plan).
2. Verificar nivel, entorno, política Git y gates en el plan.
3. Copiar `templates/dashboard.html` y `templates/dashboard-data.js` a la raíz del proyecto y completar el estado inicial en `dashboard-data.js`.
4. Entorno `cli`: instalar el hook de `templates/hooks/commit-msg` (opcional, recomendado) y correr `tools/axioma-lint.py` una vez para confirmar el paquete íntegro.
5. Confirmar con el humano la primera microetapa antes de comenzar.

## Ciclo de la microetapa (sin excepción)

```text
1. Declarar qué hará la microetapa y su criterio de salida (del plano.md).
2. Ejecutar. Precisión numérica o lógica -> código/herramienta, nunca estimación.
3. Verificar el criterio de salida. Si falla -> corregir o pausar y devolver al humano.
4. Actualizar dashboard-data.js (obligatorio; ancla anti-deriva).
5. Actualizar auditoria.md si hubo decisión, desvío o riesgo nuevo (append-only).
6. Correr tools/axioma-lint.py (cli). Si hay error -> corregir antes de cerrar; en chat,
   aplicar el checklist de coherencia de execucion-chat.md.
7. Commit según la política del nivel.
8. Emitir el informe estándar (abajo).
```

## Política Git (proporcional al riesgo; solo en entorno `cli`)

| Nivel | Commit | Push |
|---|---|---|
| N1 | opcional | con aprobación |
| N2 | automático local al cerrar cada microetapa | solo con aprobación humana |
| N3 | solamente tras el gate humano de la etapa aprobado | solo con aprobación humana |

Mensaje: `axioma(<mN>): <resultado en una línea>`
Ejemplos: `axioma(m2): capa de bloqueo con verificación de sesión y permiso` · `axioma(m4): builds free y full del contenido`

Reglas: un commit por microetapa (no por archivo); nunca commitear un secreto o clave; el commit de gate incluye en el cuerpo `gate: aprobado por <humano> en <fecha>`. En entorno `chat` no hay Git: el equivalente es el bloque de estado de `execucion-chat.md`.

## Gates humanos

Checkpoint de validación humana **durante el desarrollo**; no vuelve nada manual en producción. En el gate, el ejecutor:

1. pausa y corre el lint (cli); el gate no abre con lint en error;
2. presenta **qué** validar y **cómo** (pasos concretos de prueba que el humano puede seguir en su entorno);
3. espera el veredicto **y el eco de juicio**: 1 a 3 frases del humano, con sus propias palabras, explicando qué validó y por qué lo considera correcto. Un `ok` seco no cierra gate; si llega seco, el ejecutor pide el eco una vez, con la pregunta: `¿Qué verificaste y qué te convence de que está correcto?`;
4. registra el veredicto y el eco literal en `auditoria.md` (tabla Gates) y el resumen en `dashboard-data.js` (campo `echo`);
5. si es reprobado: corrige, registra en métricas (`gates_failed`) y vuelve a presentar.

El ejecutor nunca marca un gate humano como aprobado y nunca redacta el eco en nombre del humano.

## Política de pausa (fuera de gate)

Pausar y devolver al humano cuando: haya conflicto entre artefactos; cambie el alcance; falte un dato crítico; falle un criterio de salida; surja una decisión humana no prevista; aparezca un riesgo nuevo; la validación dependa de juicio humano; el lint acuse un error cuya corrección exige decisión.

## Dashboard (estado derivado)

El estado vive en `dashboard-data.js`, un archivo separado con `const DATA = { ... }` cuyo contenido entre llaves es **JSON estricto** (comillas dobles, sin comentarios, sin coma final). El `dashboard.html` solo renderiza; nunca se edita el HTML. El lint valida el JSON y su coherencia con el plan. Campos:

- `kit_version`, `project`, `level`, `risk`, `environment` (`cli`|`chat`), `lang` (`pt`|`es`), `updated`, `commit` (hash corto o "-")
- `steps`: `{id, name, status: pending|doing|done, gate: true|false}` (IDs iguales a los del plan)
- `risks`: `{text, level}`
- `decisions`: decisiones humanas abiertas
- `gates`: `{step, date, verdict: ok|fail, echo}` (echo: resumen del eco; el literal queda en la auditoría)
- `metrics`: `{rework, reopened, gates_failed, drift_events}`

Cuándo actualizar: al fin de la planificación; al fin de cada microetapa; al abrir/cerrar un gate; al cerrar el proyecto. Precedencia: en divergencia con `auditoria.md`, la auditoría gana, cuenta `drift_event` y el dashboard se corrige en el mismo turno. Treinta segundos de lectura deben bastar para que el coordinador sepa el estado de todo.

## Informe estándar por microetapa

```text
Etapa:
Archivos creados:
Archivos modificados:
Criterios cumplidos:
Desvíos:
Pendientes:
Lint: (sin errores | errores corregidos: <cuáles> | n/a chat)
Gate humano: (sí/no; si sí, qué validar y cómo)
Próxima acción:
```

## Cierre

- [ ] microetapas concluidas y criterios de aceptación cumplidos
- [ ] dashboard y auditoría actualizados y coherentes (lint sin errores)
- [ ] todos los gates con eco registrado
- [ ] pendientes humanos explicitados
- [ ] retrospectiva emitida: qué dicen las métricas (ver `metricas.md`) y un ajuste sugerido al protocolo, si lo hay
