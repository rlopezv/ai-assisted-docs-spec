---
document: Evaluation Plan
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.3
last_updated: [YYYY-MM-DD]
owners:
  - [Responsable]
related_documents:
  - business/01_project_brief.md
  - business/02_prd.md
  - architecture/02_technical_design.md

---

# Evaluation Plan

## 1. Introducción

Este documento define el **plan de evaluación del sistema**, estableciendo un marco objetivo para medir:

- calidad del output
- cumplimiento de requisitos
- comportamiento del sistema bajo distintas condiciones

Su objetivo es permitir:

- validar el sistema
- detectar regresiones
- guiar iteraciones de mejora

---

### Ejemplo

> Un sistema de extracción de datos será evaluado con un conjunto de documentos de referencia, midiendo precisión, completitud y cumplimiento del formato esperado.

---

## 2. Objetivos de Evaluación

Definir qué se quiere validar.

- validar precisión del output
- validar cumplimiento de schema
- validar comportamiento ante inputs degradados

---

### Ejemplo

- verificar que los datos extraídos coinciden con el dataset de referencia
- comprobar que todos los outputs son estructuralmente válidos
- evaluar comportamiento ante inputs incompletos

---

## 3. Dataset de Evaluación

Definir los datos utilizados para evaluar el sistema.

### Tipos de dataset

- dataset de referencia (golden dataset)
- dataset de casos reales
- dataset de edge cases

---

### Definición

- origen de los datos: archivos históricos digitalizados
- volumen: 1.000 documentos
- cobertura: múltiples formatos y calidades
- ubicación: repositorio interno versionado

---

### Ejemplo

- dataset manualmente etiquetado
- inclusión de documentos con ruido, errores y ambigüedad

---

## 4. Tipos de Evaluación

Definir los distintos enfoques de evaluación.

---

### Evaluación del sistema

- ¿el sistema cumple los requisitos?
- ¿el output cumple el schema?
- ¿el contenido es correcto?

---

### Ejemplo

- comparar resultados con dataset de referencia
- validar estructura del output generado
- revisar coherencia del contenido

---

### En el caso de utilizar IA / LLM

Evaluar:

- calidad del output
- consistencia entre ejecuciones
- presencia de alucinaciones

---

### Ejemplo

- detectar campos generados sin base en el input
- comparar resultados entre múltiples ejecuciones del mismo input

---

## 5. Métricas de Calidad

Definir qué se mide para evaluar el sistema.

---

### Métricas del sistema

- % outputs válidos
- % cumplimiento de schema
- precisión por campo
- completitud

---

### Ejemplo

- 97% de outputs válidos
- 92% de precisión en campos clave

---

### Métricas de rendimiento

- latencia
- throughput

---

### Ejemplo

- tiempo medio de procesamiento: 1.2s
- 50 documentos procesados por minuto

---

### En el caso de utilizar IA / LLM

#### Métricas del modelo

- score de confianza
- tasa de alucinación
- consistencia

---

#### Métrica de calibración

- correlación entre confianza y acierto real
- detección de sobreconfianza

---

### Ejemplo

- correlación confianza-acierto: 0.78
- 12% de outputs con confianza alta pero incorrectos

---

## 6. Metodología de Evaluación

Definir cómo se ejecuta la evaluación.

---

### Proceso

- ejecución automática tras cada cambio
- comparación con dataset de referencia
- revisión manual de casos críticos

---

### Métodos

- comparación exacta
- comparación tolerante
- evaluación asistida

---

### Ejemplo

- matching exacto para campos estructurados
- tolerancia en formatos de fecha
- revisión manual en casos ambiguos

---

### Evaluación asistida (opcional)

- validación semántica
- detección de errores complejos

---

### En el caso de utilizar IA / LLM

- uso de un modelo más avanzado como evaluador
- auditoría de coherencia semántica

---

### Ejemplo

- un modelo evalúa si el contenido extraído tiene sentido
- detección de inconsistencias no detectables por reglas

---

## 7. Escenarios de Evaluación

Definir en qué condiciones se evalúa el sistema.

---

### Tipos de escenario

- casos normales
- casos límite
- inputs inválidos
- inputs incompletos

---

### Ejemplo

- documentos completos bien estructurados
- documentos con datos faltantes
- inputs corruptos

---

### Escenario de ruido de ingesta

Evaluar el comportamiento ante datos degradados.

- texto truncado
- errores en el input
- documentos parcialmente legibles

---

### Ejemplo

- documentos con caracteres ilegibles
- texto incompleto

---

### En el caso de utilizar IA / LLM

- errores de reconocimiento
- ambigüedad semántica

---

### Ejemplo

- fechas ambiguas interpretadas de múltiples formas
- texto con errores de reconocimiento

---

## 8. Umbrales de Aceptación (Success Criteria)

Definir criterios mínimos para considerar el sistema válido.

---

### Diferenciación por criticidad

- campos críticos
- campos secundarios

---

### Ejemplo

- ≥ 98% precisión en campos críticos
- ≥ 90% en campos secundarios

---

### Consideraciones

- errores en campos críticos invalidan el resultado

---

### En el caso de utilizar IA / LLM

- umbral mínimo de confianza aceptable: 0.85
- outputs por debajo del umbral requieren revisión

---

### Ejemplo

- resultados con confianza < 0.85 se envían a revisión manual

---

## 9. Evaluación Continua

Definir cómo se integra la evaluación en el ciclo de desarrollo.

---

### Ejemplo

- ejecución automática en cada cambio
- comparación entre versiones
- detección de regresiones

---

### En el caso de utilizar IA / LLM

- comparación entre versiones de prompts
- análisis de impacto de cambios en instrucciones

---

### Ejemplo

- nueva versión del prompt reduce precisión en fechas → rollback

---

## 10. Observabilidad de la Evaluación

Definir cómo se registran los resultados.

---

### Incluye

- logs de evaluación
- métricas agregadas
- histórico de resultados

---

### Ejemplo

- dashboard con evolución de métricas
- tracking por versión del sistema

---

## 11. Limitaciones de la Evaluación

Definir qué no cubre el plan de evaluación.

---

### Tipos de limitación

- cobertura del dataset
- representatividad
- condiciones no evaluadas

---

### Sesgo de dataset (Data Drift)

- cobertura temporal
- diversidad de formatos
- variabilidad de inputs

---

### Ejemplo

- dataset centrado en un único tipo de documento
- baja variabilidad de inputs

---

### Consideraciones

- resultados no siempre extrapolables
- necesidad de actualizar dataset

---

## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento define cómo validar el sistema.

---

### Instrucciones para el asistente IA

- no proponer cambios sin evaluación
- usar métricas para justificar mejoras
- evitar optimizaciones sin medición

---

### Riesgos

- sobreajuste al dataset
- métricas engañosas
- falta de cobertura

---

### Dudas abiertas

- definición de métricas óptimas
- calidad del dataset
