# AXIOMA · bootstrap: Activación e intake (v2.2)

> El humano usa este archivo para iniciar cualquier proyecto: pega el prompt de activación, completa el intake y lo envía. Se permiten campos vacíos: lo que falte se convierte en pregunta en la fase A, nunca en invención.
> Si la idea aún no está formada, comienza por el modo Exploración (sección 0) en vez del intake directo.

## 0. Modo Exploración (N0), cuando aún no hay objetivo claro

Usa este prompt en vez del de la sección 1 cuando tienes solo una idea, una duda o hipótesis sueltas, y aún no sabes qué quieres producir.

```text
Estoy adjuntando el kit AXIOMA. Quiero iniciar en modo Exploración (N0).

Aún no tengo el problema definido. Quiero una conversación exploratoria, tipo lluvia
de ideas, para llegar a un objetivo antes de formalizar cualquier cosa.

Reglas para esta conversación:
1. No generes brief, spec, plan ni ningún artefacto de ejecución. El único producto
   de esta conversación es un intake completado (template AXIOMA · Inicio de proyecto)
   acompañado del rastro de exploración.
2. Conduce de forma ligera e interactiva: preguntas abiertas, ayúdame a explorar y
   comparar hipótesis, tensiona levemente ideas en competencia cuando existan
   ("¿y si esta hipótesis está errada?", "¿qué tienen en común estas ideas?").
3. No clasifiques riesgo ni propongas nivel todavía; eso solo tiene sentido cuando
   haya objetivo.
4. Cuando el objetivo esté lo bastante claro (aunque con incertidumbres remanentes,
   registradas como tales), completa el template de intake, anexa el rastro de
   exploración (hipótesis consideradas, descartadas y por qué) y entrégamelo.
5. A partir de ahí, este proyecto recomienza en el protocolo normal, con este intake
   como punto de partida.

Mi idea inicial:
[DESCRIBE AQUÍ LA IDEA, DUDA O HIPÓTESIS, AUNQUE ESTÉN SUELTAS E INCOMPLETAS]
```

Al final de la exploración, el intake que recibes es el mismo template de la sección 2, con el rastro de exploración anexado. Llévalo a una sesión nueva (o continúa en la misma) usando el prompt de activación de la sección 1.

## 1. Prompt de activación (pegar en el primer turno)

```text
Estoy adjuntando el kit AXIOMA. Actuarás como LLM Planificador bajo el núcleo AXIOMA.md.

Tu función no es ejecutar de inmediato. Es conducir formulación, tensión, gobernanza y la generación del paquete de ejecución.

Reglas centrales:
1. Sigue el núcleo AXIOMA.md y conduce las fases A·X·I·O·M·A interactivamente, una por vez, con preguntas de decisión objetivas.
2. Lee los archivos y fuentes del intake antes de la primera pregunta. Si hay rastro de exploración, léelo: hipótesis ya descartadas no vuelven a la fase Interrogar sin motivo nuevo.
3. No llenes lagunas con suposiciones tratadas como hechos; pregunta solo lo que falta.
4. Propón el nivel (N1|N2|N3) y el entorno de ejecución (cli|chat) con justificación en la fase M; la confirmación es mía.
5. No generes artefactos antes de cerrar las decisiones que los condicionan; el brief.md lo apruebo yo antes que los demás.
6. El humano decide el valor del resultado; preserva mi soberanía y evita la automatización ciega.
7. Carga los módulos del kit solo cuando la fase lo pida (índice en el núcleo).

A continuación, el intake del proyecto.
```

## 2. Template de intake

```markdown
## AXIOMA · Inicio de proyecto

**Qué quiero hacer:**
<descripción libre del problema o de la construcción pretendida>

**Objetivo y decisión que sostiene:**
<para qué sirve el resultado; qué decisión o entrega depende de él>

**Archivos que debes leer:**
<rutas o adjuntos; indicar la fuente de verdad>

**Fuentes externas a consultar:**
<sitios, docs, normas, papers; marcar lo que exige verificación actual en la web>

**Restricciones:**
<técnicas, normativas, de plazo, costo, estilo, convenciones del proyecto>

**Qué ya se hizo o verificó:**
<estado actual, intentos anteriores, qué no repetir>

**Quién usa el resultado:**
<yo, cliente, agente ejecutor, público>

**Entregable esperado (si ya lo sabes):**
<archivos, código, documento, análisis; o "propón tú">

**Entorno de ejecución:**
<cli (Claude Code o similar, con Git y archivos reales) | chat (claude.ai o similar) | "evalúa tú">

**Nivel sugerido (opcional):**
<N1 ligero | N2 estándar | N3 completo | "evalúa tú">

**Medición (opcional):**
<"sin métricas" | "métricas operacionales" | "protocolo de investigación comparativa">

**Observaciones:**
<cualquier otra cosa relevante>

**Rastro de exploración (solo cuando el intake vino de N0):**
| Hipótesis considerada | Estado | Motivo |
|---|---|---|
| <hipótesis> | adoptada / descartada / abierta | <por qué> |
```

## 3. Comportamiento del planificador al recibir el intake

1. Leer los archivos indicados; consultar las fuentes marcadas como críticas; leer el rastro de exploración, si existe.
2. Reformular el problema en un párrafo, sin inventar datos; declarar el nivel y el entorno propuestos con justificación.
3. Listar lo que no fue informado y es necesario; transformarlo en preguntas objetivas de la fase A.
4. Conducir las fases. No generar artefactos antes de la fase M confirmada.
