---
document: LLM Integration Specification
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 2.1
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - llm/02_prompt_library.md
  - llm/03_output_schemas.md
  - data/01_domain_model.md
  - data/02_data_dictionary.md
---

# LLM Integration Specification

## 1. Introducción

Este documento define **cómo se integra un modelo de lenguaje (LLM)** dentro del sistema.

Debe describir:

- el rol del LLM
- los puntos de entrada y salida
- el flujo de ejecución
- la validación de resultados
- la gestión de errores

No define:

- prompts concretos (ver `llm/02_prompt_library.md`)
- schemas formales (ver `llm/03_output_schemas.md`)
- detalles de implementación (ver TDD)

---

## 2. Rol del LLM en el Sistema

Definir qué responsabilidades tiene el LLM.

### Ejemplo

- transformación de texto no estructurado a datos estructurados
- inferencia de información incompleta
- normalización semántica de contenido

---

### Exclusiones

Definir qué NO hace el LLM:

- persistencia de datos
- control de flujo del sistema
- lógica de negocio crítica

---

## 3. Pipeline de Integración

Definir el flujo completo de interacción con el LLM.

### Estructura general

```text
Input → Preprocesado → Construcción de Prompt → Inferencia → Post-procesado → Validación → Normalización → Output
```

---

### Fases

1. Preparación del input
2. Construcción del prompt
3. Ejecución del modelo
4. Procesado de la respuesta
5. Post-procesado de la respuesta
6. Validación
7. Normalización del output
8. Integración en el sistema

---

### Gestión de contexto

Definir cómo se maneja el tamaño del input cuando supera la capacidad del modelo.

- segmentación del input
- procesamiento por fragmentos
- agregación de resultados
- priorización de contenido relevante

---

## 4. Activación del LLM

Definir cuándo se utiliza el LLM.

### Tipos de activación

- obligatoria
- condicional
- fallback

---

### Ejemplo

- activar solo si faltan datos críticos
- activar si el input no cumple ciertos criterios de calidad

---

## 5. Inputs al LLM

Definir qué información recibe el modelo.

### Tipos de input

- texto no estructurado
- datos estructurados previos
- contexto adicional

---

### Consideraciones

- tamaño máximo de input
- limpieza y normalización
- priorización de contenido

---

## 6. Diseño de Prompts

Referencia:

- `llm/02_prompt_library.md`

---

### Elementos

- system prompt
- instrucciones
- contexto
- formato esperado de salida

---

### Construcción dinámica del prompt

- datos de entrada
- resultados de fases previas
- contexto adicional
- configuración de ejecución

---

## 7. Outputs Esperados

Referencia:

- `llm/03_output_schemas.md`

---

### Tipos de output

- JSON estructurado
- texto enriquecido
- clasificación

---

### Formatos admitidos

El sistema puede trabajar con dos formatos de salida:

- salida simple: valores directos
- salida trazable: valores enriquecidos con metadatos por campo

Ambos formatos deben estar definidos en `llm/03_output_schemas.md`.

---

### Normalización de output

Antes de integrar la salida en el sistema, el pipeline debe normalizar el resultado al formato interno esperado.

La normalización debe preservar, cuando existan:

- `confidence`
- `source_reference`
- `generation_type`

---

### Post-procesado de salida

- eliminación de texto no estructurado
- extracción de bloques relevantes
- normalización del formato esperado

---

### Metadatos recomendados

- nivel de confianza (`confidence`)
- trazabilidad (`source_reference`)
- tipo de generación (`generation_type`)

---

## 8. Validación de Salida

### Tipos de validación

- sintáctica (formato)
- estructural (schema)
- semántica (consistencia)

---

### Resultado

- válido
- inválido
- válido con advertencias

---

## 9. Gestión de Errores

### Tipos de error

- respuesta inválida
- timeout
- salida inconsistente

---

### Estrategias

- retry
- degradación funcional
- fallback

---

### Estrategia de reintento

- configuración del modelo
- prompt
- input
- contexto

---

## 10. Estrategia de Fallback

- ejecución sin LLM
- uso de lógica heurística
- uso de fuentes de contexto adicionales

---

## 11. Gestión de Confianza

### Métricas

- score de confianza
- consistencia interna
- validación cruzada

---

### Uso

- aceptación automática
- revisión manual
- reintento

---

## 12. Trazabilidad

Cada dato generado debe poder rastrearse mediante:

- segmento de origen (`source_reference`)
- nivel de confianza (`confidence`)
- tipo de generación (`generation_type`)

Los metadatos de trazabilidad deben preservarse durante:

- post-procesado
- validación
- normalización
- integración posterior

No deben descartarse salvo decisión explícita documentada.

---

## 13. Consideraciones de Rendimiento

- latencia de inferencia
- uso de recursos
- tamaño de contexto

---

## 14. Limitaciones

- dependencia del modelo
- variabilidad de resultados
- sensibilidad al input

---

## Anexo. Notas de Coworking (IA Assistant)

### Instrucciones

- no acoplar a modelos concretos
- no introducir detalles de implementación
- mantener separación entre prompt, schema e integración

---

### Riesgos

- acoplamiento a herramientas específicas
- duplicación con otros documentos
- falta de validación estructural
