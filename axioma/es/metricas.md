# AXIOMA · métricas: Medición operacional e investigación comparativa (v2.2)

> Cargar cuando el intake pida medición. Dos usos: (1) operacional, casi gratuito, recolectado en el dashboard; (2) investigación, para responder "¿usar el AXIOMA hace diferencia frente a otros mecanismos?".

## 1. Métricas operacionales (recolectadas en el `DATA.metrics` del dashboard)

| Métrica | Definición | Señal cuando es alta |
|---|---|---|
| `rework` | microetapas rehechas tras concluidas | brief o plan débiles |
| `reopened` | decisiones cerradas que hubo que reabrir | fases X o M mal cerradas |
| `gates_failed` | gates reprobados en el primer intento | ejecución divergiendo del plan |
| `drift_events` | reanclajes del protocolo + divergencias dashboard×auditoría detectadas | el núcleo pierde fuerza; sesiones demasiado largas |

Derivadas del dashboard, sin recolección extra:

| Métrica | Fórmula | Mide |
|---|---|---|
| SCR | etapas `done` / etapas totales | progreso |
| GTR | etapas con gate / etapas totales | peso de gobernanza |
| DR | desvíos registrados en la auditoría / etapas ejecutadas | estabilidad |
| AEF | ítems de la spec cumplidos / ítems totales | fidelidad del ejecutor |

## 2. Índices compuestos (evaluación por proyecto; puntaje 0–1 por componente)

**Nota metodológica (obligatoria en uso de investigación).** Los pesos siguientes son defaults de diseño, no constantes validadas. En cualquier reporte de investigación: (a) reportar siempre los componentes desagregados, no solo el índice; (b) acompañar el índice de un análisis de sensibilidad simple (recalcular con cada peso ±0,05, redistribuyendo proporcionalmente; si el ranking entre condiciones cambia, la conclusión no se sostiene en el índice y debe bajar a los componentes); (c) registrar la versión del kit, porque los cambios de protocolo rompen la comparabilidad.

### OCI: Índice de Convergencia Operacional

```text
OCI = 0,30·Cd + 0,25·Cn + 0,20·Cm + 0,10·Cs + 0,15·Ca   (pesos default)
```

| Comp. | Nombre | Cómo medir (0–1) |
|---|---|---|
| Cd | decisión sostenida | ¿el resultado respondió a la `target_decision` del brief? (rúbrica: 0 no; 0,5 parcialmente; 1 sí) |
| Cn | conformidad | criterios de aceptación cumplidos / totales |
| Cm | fidelidad al plan | microetapas sin desvío / totales |
| Cs | estabilidad de alcance | 1 − (alteraciones de alcance / microetapas) |
| Ca | auditabilidad | artefactos actualizados al final / artefactos exigidos por el nivel |

### ESI: Índice de Soberanía Epistémica

```text
ESI = 0,20·Jc + 0,30·Ef + 0,20·Cr + 0,15·Ar + 0,15·Dl   (pesos default)
```

| Comp. | Nombre | Cómo medir (0–1) |
|---|---|---|
| Jc | juicio consciente | decisiones críticas tomadas por el humano / decisiones críticas totales |
| Ef | explicabilidad | evaluada sobre los **ecos de juicio registrados en la auditoría**, no sobre autorreporte: rúbrica 0 (eco ausente o vacío), 0,5 (eco genérico, no específico al contenido), 1 (eco específico: cita qué se verificó y por qué). Puntuable por evaluador ciego |
| Cr | calibración de revisión | errores detectados por el humano en gates / errores totales **registrados en la auditoría hasta el cierre** (por cualquier vía: humano, lint, herramienta, tercero). Proxy declarado: los errores nunca descubiertos no entran; interpretar como piso, no como valor verdadero |
| Ar | autonomía apropiada | 1 si la autonomía de la IA quedó dentro del nivel; restar 0,25 por violación registrada |
| Dl | devolución de decisiones | decisiones nuevas pausadas y devueltas / decisiones nuevas surgidas |

### OVI: Índice de Valor Operacional

```text
HEI = tiempo humano con AXIOMA / tiempo humano en la línea de base
OVI = (OCI × ESI) / HEI
```

HEI exige una línea de base medida; cuando no exista, registrar `HEI = n/d` y no calcular OVI (no estimar la línea de base de memoria).

Interpretación del cuadrante:

```text
OCI alto + ESI bajo  = automatización ciega
OCI bajo + ESI alto  = exploración sin cierre
OCI alto + ESI alto  = decisión técnica robusta  (objetivo)
OCI bajo + ESI bajo  = caos operacional
```

## 3. Protocolo de investigación comparativa

**Pregunta:** ¿el AXIOMA mejora convergencia, soberanía, auditabilidad y éxito de ejecución frente a otros mecanismos?

**Condiciones:**

| Cond. | Descripción |
|---|---|
| A | prompt libre (línea de base) |
| B | solo el núcleo interactivo (sin artefactos) |
| C | núcleo + brief + plan (N2) |
| D | kit completo (N3) |
| E | kit completo + dashboard + métricas activas |

**Diseño:** misma tarea en todas las condiciones; tareas de tipos distintos (documento técnico, pipeline de datos, cálculo/EVTE, artículo, sitio documental); 5 ejecuciones por condición en el piloto, 10–20 en el estudio fuerte; variar el modelo (Claude, GPT, Gemini, DeepSeek) si el objetivo incluye generalización; fijar la versión del kit durante todo el estudio.

**Recolección por ejecución (una línea de CSV):**

```text
run_id, condicao, tarefa, modelo, data, versao_kit, ambiente,
OCI, ESI, HEI, OVI, SCR, DR, AEF,
Cd, Cn, Cm, Cs, Ca, Jc, Ef, Cr, Ar, Dl,
rework, reopened, gates_failed, drift_events,
tempo_humano_min, tempo_total_min, nota_qualitativa
```

(Los nombres de columna se mantienen en PT en ambos idiomas para que los datasets sean combinables.)

**Evaluación ciega:** cuando sea posible, un evaluador (humano o LLM distinto) puntúa Cd, Ef y la calidad del entregable sin conocer la condición. Para Ef, el evaluador recibe solo los ecos registrados y el entregable.

**Hipótesis:** las condiciones D/E aumentan OCI, ESI y éxito de handoff, con HEI mayor (más tiempo humano); el OVI revela si la ganancia compensa el costo. Si OVI(D) ≤ OVI(A) en tareas simples, es evidencia para usar N1 en ellas, lo que el propio protocolo ya prevé.

## 4. Retrospectiva obligatoria (todo proyecto N2/N3)

Al cerrar, el ejecutor emite un párrafo: qué dicen las métricas, dónde el protocolo ayudó o estorbó, y un ajuste sugerido al kit, si lo hay. Los ajustes aceptados por el humano se vuelven nueva versión del kit, registrada en el `CHANGELOG.md`.
