---
document: Roadmap
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.0
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - business/01_project_brief.md
  - business/02_prd.md
---

# Roadmap

## 1. Introducción

Este documento describe la **evolución prevista del sistema** a lo largo del tiempo, organizando el trabajo en fases con objetivos y criterios de progresión claros.

Su objetivo es:

- comunicar la dirección del producto
- establecer prioridades y dependencias entre fases
- definir criterios de entrada y salida de cada fase

Este documento no define:

- requisitos funcionales detallados (ver `02_prd.md`)
- diseño técnico (ver `architecture/`)
- tareas de implementación concretas

---

### Ejemplo

> El sistema evoluciona desde un MVP funcional hasta una solución completa, priorizando la estabilidad antes de añadir capacidades avanzadas.

---

## 2. Principios del Roadmap

Definir los criterios que guían la planificación.

- [Principio 1]
- [Principio 2]

---

### Ejemplo

- MVP primero: priorizar funcionalidad básica estable antes que capacidades avanzadas
- Dependencia de hitos: no iniciar una fase sin validar los criterios de salida de la anterior
- Flexibilidad: el roadmap se ajusta según hallazgos técnicos en cada fase

---

## 3. Fases

### Fase 1 — [Nombre]

Objetivo:

- ...

Entregables principales:

- ...

Criterios de entrada:

- ...

Criterios de salida:

- ...

---

### Ejemplo

### Fase 1 — Cimientos (MVP)

Objetivo:

- construir la base funcional del sistema
- validar el flujo completo de extremo a extremo con datos reales

Entregables principales:

- ingesta de datos funcional
- procesamiento básico
- persistencia de resultados

Criterios de entrada:

- entorno configurado
- datos de prueba disponibles

Criterios de salida:

- flujo completo ejecutado sin errores en dataset de prueba
- tasa de éxito ≥ umbral definido en QA

---

### Fase 2 — [Nombre]

Objetivo:

- ...

Entregables principales:

- ...

Criterios de entrada:

- Fase 1 completada

Criterios de salida:

- ...

---

### Ejemplo

### Fase 2 — Enriquecimiento

Objetivo:

- incorporar capacidades de análisis avanzado
- mejorar calidad del output mediante procesamiento inteligente

Entregables principales:

- integración con motor de análisis
- validación estructurada de outputs
- pipeline de degradación funcional

Criterios de entrada:

- Fase 1 completada y validada

Criterios de salida:

- precisión del output ≥ umbral definido en QA
- tasa de errores por debajo del umbral aceptable

---

### Fase 3 — [Nombre]

(Repetir estructura)

---

## 4. Dependencias entre Fases

Definir qué bloquea el inicio de cada fase.

| Fase | Depende de | Criterio |
| ---- | ---------- | -------- |
| Fase 2 | Fase 1 | criterios de salida validados |
| Fase 3 | Fase 2 | criterios de salida validados |

---

## 5. Backlog

Este backlog es orientativo y no sustituye a herramientas de gestión de tareas. Su objetivo es recoger ideas o capacidades candidatas a futuras fases. Contiene las ideas y funcionalidades identificadas pero no planificadas en las fases actuales.

- [Idea 1]
- [Idea 2]

---

### Ejemplo

- soporte multilingüe avanzado
- interfaz gráfica de visualización
- exportación a formatos adicionales
- integración con sistemas externos

---

### Criterios para incorporar al roadmap

- validación de necesidad real en uso del sistema
- estimación de impacto vs esfuerzo
- no bloquear fases activas

---

## 6. Trazabilidad

| Elemento | Documento Relacionado |
| -------- | --------------------- |
| Requisitos | PRD |
| Visión estratégica | Project Brief |

---

## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento define la evolución prevista del sistema por fases.

---

### Instrucciones

- no definir tareas de implementación concretas
- no duplicar requisitos del PRD
- mantener criterios de salida medibles y verificables
- registrar cambios de planificación en el historial

---

### Historial de cambios de planificación

| Fecha | Cambio | Motivo |
| ----- | ------ | ------ |

---

### Riesgos

- fases sin criterios de salida claros
- dependencias no documentadas entre fases
- backlog sin criterios de priorización

---

### Dudas abiertas

- duración estimada de cada fase
- recursos disponibles por fase
- criterios de éxito definitivos por fase

### Inputs utilizados

- ...


### Insights clave

- ...

