---
document: Product Requirements Document (PRD)
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 2.0
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o persona responsable]
related_documents:
  - business/01_projet_brief.md
  - architecture/01_architecture_overview.md
  - llm/01_llm_integration_spec.md
  - qa/01_evaluation_plan.md
---

# Product Requirements Document (PRD)

## 1. Introducción

Este documento define los **requisitos funcionales y no funcionales del sistema**, actuando como contrato entre negocio, arquitectura, implementación y validación.

Debe permitir:
- Derivar la arquitectura del sistema  
- Definir el comportamiento esperado del sistema (incluyendo componentes LLM)  
- Establecer criterios de validación (QA)  

---

## 2. Contexto y Problema

### 2.1 Problema
- Descripción operativa del problema:
- Situación actual:
- Impacto:

### 2.2 Objetivo del Sistema
Definir el sistema como transformación:

- Input:
- Output:
- Resultado esperado:

---

## 3. Pilares del Producto (Restricciones Clave)

- Pilar 1:
- Pilar 2:
- Pilar 3:

---

## 4. Definición del Sistema

### 4.1 Inputs
- Tipo:
- Formato:
- Ejemplo:

### 4.2 Outputs
- Tipo:
- Formato:
- Ejemplo:
- Referencia a schema (si aplica):

### 4.3 Transformación Principal
Descripción clara de qué hace el sistema sin entrar en implementación.

---

## 5. Actores del Sistema

### 5.1 Roles Humanos
- Rol:
  - Responsabilidades:
  - Interacción con el sistema:

### 5.2 Componentes Automatizados
- Sistema / Agente:
  - Responsabilidades:
  - Nivel de autonomía:

---

## 6. Casos de Uso Operativos

### UC-01: [Nombre]

- Input:
- Proceso:
- Output:
- Edge cases:

### UC-02: [Nombre]
...

---

## 7. Requisitos Funcionales

### FR-01
- Descripción:
- Input:
- Output:
- Restricciones:

### FR-02
...

---

## 8. Requisitos No Funcionales

### Rendimiento
- Latencia máxima:
- Throughput:

### Fiabilidad
- Tasa de error:
- Disponibilidad:

### Coste
- Coste máximo por operación:

### Recursos
- Uso de GPU/CPU/RAM:

### Seguridad
- Restricciones (ej: offline, privacidad):

---

## 9. Comportamiento del Sistema LLM (si aplica)

### Comportamientos Permitidos
- ...

### Comportamientos No Permitidos
- ...

### Garantías de Output
- Formato:
- Estructura:
- Validación esperada:

### Modos de Fallo
- Output inválido
- Inconsistencia
- Ambigüedad

---

## 10. Modelo de Errores

### Tipos de Error
- Input inválido
- Fallo de procesamiento
- Error de modelo
- Violación de schema

### Comportamiento del Sistema
- Retry:
- Fallback:
- Fail-fast:

---

## 11. Criterios de Aceptación

### AC-01
- Given:
- When:
- Then:
- Método de validación:

### AC-02
...

---

## 12. Métricas de Éxito

### Métricas del Sistema
- % outputs válidos (schema-compliant)
- Latencia media
- Tasa de errores

### Métricas de Producto
- Tasa de éxito de tareas
- Intervención manual requerida

---

## 13. Dependencias

- Sistemas externos:
- Fuentes de datos:
- Modelos LLM:
- Infraestructura:

---

## 14. Fuera de Alcance

- Funcionalidades excluidas:
- Supuestos explícitos:

---

## 15. Trazabilidad

| PRD Item | Arquitectura | LLM Spec | QA |
|----------|-------------|----------|----|
| FR-01    |             |          |    |

---

## Anexo. Notas de Coworking (IA Assistant)

Este apartado está orientado a colaboración con sistemas de IA.

### Contexto adicional
- Decisiones de negocio relevantes:
- Supuestos:

### Dudas abiertas
- ...

### Instrucciones para el asistente IA
- Priorizar consistencia con otros documentos
- Evitar ambigüedad en outputs
- Validar alineación con schemas y tests

### Riesgos identificados
- ...