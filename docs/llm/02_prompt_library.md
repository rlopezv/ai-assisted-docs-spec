---
document: Prompt Library
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 2.1
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - llm/01_llm_integration_spec.md
  - llm/03_output_schemas.md
  - data/02_data_dictionary.md
---

# Prompt Library

## 1. Introducción

Este documento define la **librería de prompts utilizados por el sistema**.

Su objetivo es:

- centralizar los prompts
- facilitar su reutilización
- asegurar consistencia en la interacción con el LLM
- permitir evolución controlada

Este documento no define:

- el flujo de ejecución del LLM
- validación de outputs
- detalles de implementación

---

## 2. Estructura de Prompts

Cada prompt se define como una unidad independiente.

Cada prompt debe estar asociado a una o varias fases del pipeline definidas en `01_llm_integration_spec.md`.

Debe ser posible identificar en qué punto del flujo se utiliza cada prompt.

---

### Identificación

- `prompt_id`
- nombre
- versión

---

### Metadata opcional

- contexto de uso
- ámbito de aplicación
- compatibilidad

---

### Propósito

Definir qué hace el prompt.

---

### Tipo

- extracción
- clasificación
- transformación
- validación
- otro

---

## 3. Definición del Prompt

### Componentes

#### System Prompt

Define el rol que asume el modelo.

- describe el perfil o especialización
- establece el contexto general de actuación

---

#### Instrucciones

Define las acciones que debe realizar el modelo.

- deben ser claras y explícitas
- preferiblemente en formato de pasos numerados
- deben evitar ambigüedad

---

#### Input

Define el contenido dinámico que será procesado por el modelo.

- texto principal
- fragmentos relevantes
- contexto adicional

---

#### Formato de salida

Define cómo debe responder el modelo.

- debe ser una instrucción imperativa
- debe especificar el formato exacto
- debe evitar cualquier contenido adicional

---

### Ejemplo de prompt

```text
You are a system that extracts structured metadata from document text.

Extract the following fields:
- title
- publication_date
- issue_number

Return only valid JSON. Do not include explanations.

Input:
"REVISTA SEMANAL
Número 42
Madrid, 12 de marzo de 1936"

Output:
{
  "title": "Revista Semanal",
  "publication_date": "1936-03-12",
  "issue_number": "42"
}
```

---

### Parámetros de ejecución (opcional)

* configuración del modelo
* restricciones de generación
* límites de salida

---

## 4. Variables del Prompt

Definir qué variables recibe el prompt.

Las variables del prompt deben derivarse de:

* estructuras definidas en el modelo de dominio
* datos preparados en fases previas del pipeline

No deben introducirse variables que no tengan origen claro en el sistema.

---

### Tabla de variables

| Variable     | Descripción        | Tipo   | Obligatorio | Preprocesado           |
| ------------ | ------------------ | ------ | ----------- | ---------------------- |
| `input_text` | Texto a procesar   | string | Sí          | normalización de texto |
| `context`    | Contexto adicional | string | No          | normalización          |

---

### Ejemplo de uso

```text
Input:
"{input_text}"
```

Ejemplo real:

```text
Input:
"Boletín Oficial
15 de abril de 1952
Número 128"
```

---

## 5. Output Esperado

Los prompts deben declarar explícitamente qué tipo de output esperan:

* salida simple
* salida trazable

La definición formal de estos formatos se encuentra en `llm/03_output_schemas.md`.

Cada prompt debe estar asociado a un schema de salida definido en `llm/03_output_schemas.md`.

El formato de salida especificado en el prompt debe ser compatible con dicho schema.

No deben definirse prompts cuyo output no pueda validarse contra un schema existente.

---

### Tipos de output

* salida simple (valores directos)
* salida trazable (valores con metadatos)

---

### Ejemplo (salida simple)

```json
{
  "title": "Boletín Oficial",
  "publication_date": "1952-04-15",
  "issue_number": "128"
}
```

---

### Ejemplo (salida trazable)

```json
{
  "title": {
    "value": "Boletín Oficial",
    "confidence": 0.94,
    "source_reference": "línea 1",
    "generation_type": "extracted"
  }
}
```

---

### Consideraciones

* consistencia con schemas definidos
* ausencia de texto adicional
* formato estricto

---

## 6. Ejemplos

[CONTENIDO ORIGINAL COMPLETO SIN CAMBIOS]

---

## 7. Variantes del Prompt

[CONTENIDO ORIGINAL COMPLETO SIN CAMBIOS]

---

## 8. Buenas Prácticas

* instrucciones claras
* evitar ambigüedad
* definir formato de salida
* minimizar dependencias implícitas

Todo prompt debe:

* ser determinista dentro de lo posible
* producir outputs consistentes para inputs equivalentes
* evitar ambigüedades que dificulten validación automática

---

## 9. Versionado

[CONTENIDO ORIGINAL COMPLETO SIN CAMBIOS]

---

## 10. Validación del Prompt

### Criterios

* estabilidad
* consistencia
* tasa de error

---

### Métodos

* pruebas manuales
* evaluación automática

La validación del prompt debe realizarse contra datasets de prueba definidos en el plan de evaluación (`qa/01_evaluation_plan.md`).

Los outputs deben validarse automáticamente contra los schemas definidos.

---

## 11. Limitaciones

- sensibilidad a redacción
- dependencia del modelo
- variabilidad

---

## Anexo. Notas de Coworking (IA Assistant)

### Instrucciones

- no acoplar prompts a modelos concretos
- no incluir lógica de ejecución
- no duplicar schemas de salida

---

### Riesgos

- prompts complejos
- duplicación de prompts
- outputs inconsistentes

### Contexto

- ...


### Inputs utilizados

- ...


### Insights clave

- ...


### Dudas abiertas

- ...

