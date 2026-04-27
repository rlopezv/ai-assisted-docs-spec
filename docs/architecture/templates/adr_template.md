---
document: Architecture Decision Record (ADR)
id: [NNN]
title: [Título breve de la decisión]
status: Draft
adr_status: Proposed | Accepted | Deprecated | Superseded
date: [YYYY-MM-DD]
deciders:
  - [Rol o responsable]
related_documents:
  - architecture/01_architecture_overview.md
  - architecture/02_technical_design.md
---

# ADR-[NNN]: [Título de la decisión]

## 1. Contexto

Describir el problema que requiere una decisión.

Debe incluir:

- situación actual  
- restricciones relevantes  
- objetivos a cumplir  
- contexto técnico o de negocio  

---

### Ejemplo

> El sistema requiere realizar inferencia con modelos LLM. Se debe decidir entre usar un modelo local o un servicio externo, considerando restricciones de privacidad y latencia.

---

## 2. Decisión

Describir claramente la decisión tomada.

Debe ser:

- específica  
- verificable  
- no ambigua  

---

### Ejemplo

> Se utilizará un modelo LLM local ejecutado mediante un motor de inferencia local.

---

## 3. Alternativas Consideradas

Listar las opciones evaluadas.

Para cada alternativa:

- breve descripción  
- ventajas  
- desventajas  

---

### Ejemplo

**Alternativa 1: API externa**

- Ventajas:
  - mayor capacidad de modelo  
- Desventajas:
  - dependencia de red  
  - exposición de datos  

**Alternativa 2: Modelo local**

- Ventajas:
  - privacidad  
  - control  
- Desventajas:
  - mayor uso de recursos  

---

## 4. Justificación

Explicar por qué se ha tomado la decisión.

Debe incluir:

- criterios de evaluación  
- trade-offs  
- razones principales  

---

### Ejemplo

> Se prioriza privacidad y ejecución offline sobre capacidad máxima del modelo, lo que hace preferible el uso de un modelo local.

---

## 5. Consecuencias

Describir el impacto de la decisión.

Incluir:

- efectos positivos  
- efectos negativos  
- implicaciones futuras  

---

### Ejemplo

- Positivo:
  - control total del sistema  
- Negativo:
  - mayor consumo de GPU  
- Implicación:
  - necesidad de optimización de recursos  

---

## 6. Estado y Evolución

Indicar el estado actual de la decisión.

Estados posibles:

- Proposed  
- Accepted  
- Deprecated  
- Superseded  

---

### Ejemplo

> Estado: Accepted  
> Esta decisión será revisada si cambian las capacidades de los modelos locales.

---

## 7. Referencias

Enlaces a documentos relacionados:

- PRD  
- Architecture Overview  
- TDD  
- otros ADR  

---

### Ejemplo

- architecture/02_technical_design.md  
- architecture/01_architecture_overview.md  

---

## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento registra decisiones técnicas del sistema.

---

### Instrucciones

- No duplicar decisiones en otros documentos  
- Referenciar ADRs desde TDD o arquitectura  
- Mantener consistencia con decisiones existentes  
- No proponer soluciones que contradigan ADRs aceptados  

---

### Riesgos

- decisiones inconsistentes  
- falta de trazabilidad  
- duplicación de decisiones  

---

### Dudas abiertas

- cuándo revisar decisiones  
- criterios para deprecación  
### Inputs utilizados

- ...


### Insights clave

- ...

