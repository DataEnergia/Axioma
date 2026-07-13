# AXIOMA · modo chat: Adaptaciones para entorno sin archivos reales (v2.2)

> Cargar cuando el entorno de ejecución definido en la fase M sea `chat` (claude.ai, Proyectos, o cualquier interfaz sin Git y sin sistema de archivos persistente). El protocolo no finge paridad: este archivo declara qué cambia, qué se pierde y qué sustituye a cada mecanismo.

## Principio

En `chat`, el AXIOMA opera con fuerza plena como **planificador** (N0 y fases A a M, brief) y con fuerza reducida como **ejecutor**. Las adaptaciones siguientes mantienen las anclas anti-deriva posibles y explicitan las imposibles, para que la pérdida sea consciente, nunca silenciosa.

## Tabla de equivalencias

| Mecanismo en `cli` | Equivalente en `chat` | Qué se pierde |
|---|---|---|
| Política Git por microetapa | Ninguno. No simular commits | Reversibilidad e histórico verificable |
| `dashboard-data.js` + `dashboard.html` | Bloque de estado (abajo) reemitido en cada microetapa; opcionalmente un artifact único regenerado | Renderización estable; validación por lint |
| `tools/axioma-lint.py` | Checklist de coherencia (abajo), aplicado por el ejecutor y declarado en el informe | Garantía determinística; se vuelve autoverificación |
| Hook commit-msg | Ninguno | Bloqueo mecánico de cierre sin actualización de estado |
| Archivos de artefactos | Artefactos como bloques markdown en el chat o en el conocimiento del Proyecto | El frontmatter se sigue usando; el lint no corre |
| Carga modular bajo demanda | Todo ya está en el contexto del Proyecto | Economía de contexto; mayor riesgo de deriva: reforzar checkpoints |

## Bloque de estado (sustituto del dashboard)

Reemitir al fin de cada microetapa, siempre con la misma estructura:

```text
ESTADO AXIOMA · <proyecto> · <fecha>
Nivel: | Riesgo: | Entorno: chat | Kit: 2.2
Microetapas: <done>/<total>  [M1 done] [M2 doing] [M3 pending·GATE]
Riesgos activos: ...
Decisiones abiertas: ...
Gates: <etapa> · <veredicto> · eco: "<resumen>"
Métricas: rework= reopened= gates_failed= drift_events=
```

## Checklist de coherencia (sustituto del lint)

Aplicar al fin de cada microetapa y antes de todo gate; declarar el resultado en el informe estándar (campo Lint: "checklist aplicado, sin inconsistencias" o listar lo corregido):

- [ ] todo requisito de la spec aparece en la columna Cubre de alguna microetapa (N3)
- [ ] toda microetapa con Gate: sí declara qué valida el humano y cómo
- [ ] los IDs del bloque de estado son exactamente los del plan
- [ ] ningún gate consta como aprobado sin eco registrado
- [ ] el bloque de estado no contradice ningún registro anterior de la conversación; contradicción = drift_event, corregir y contar

## Reglas adicionales en chat

1. **Los gates siguen siendo obligatorios y el eco también.** La degradación del entorno no degrada la soberanía.
2. **Regla del determinístico adaptada:** cálculo y transformación de datos usan la herramienta de análisis/ejecución de código de la interfaz, cuando exista; sin herramienta, el ejecutor declara `estimación no verificada` junto al número y el ítem entra en decisiones abiertas.
3. **Sesiones largas:** cada 10 turnos de ejecución, o al notar cualquier señal de deriva, reemitir el bloque de estado y releer las reglas inviolables del núcleo.
4. **Portar a cli:** si el proyecto migra a Claude Code a mitad de camino, los artefactos del chat se vuelven archivos, el bloque de estado se vuelve `dashboard-data.js` y el lint corre una vez para certificar la migración.
