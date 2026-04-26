---
document: Prompt Library
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 2.1
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - llm/02_prompt_library.md
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

- configuración del modelo
- restricciones de generación
- límites de salida

---

## 4. Variables del Prompt

Definir qué variables recibe el prompt.

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

- salida simple
- salida trazable

La definición formal de estos formatos se encuentra en `llm/03_output_schemas.md`.

---

### Tipos de output

- salida simple (valores directos)
- salida trazable (valores con metadatos)

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

- consistencia con schemas definidos
- ausencia de texto adicional
- formato estricto

---

## 6. Ejemplos

### Ejemplo 1 — Documento estructurado

Input:

```text
"DIARIO REGIONAL
Sevilla, 3 de junio de 1924
Núm. 15"
```

Output:

```json
{
  "title": "Diario Regional",
  "publication_date": "1924-06-03",
  "issue_number": "15"
}
```

---

### Ejemplo 2 — Documento incompleto

Input:

```text
"Revista Cultural
Edición de otoño 1987"
```

Output:

```json

  "title": "Revista Cultural",
  "publication_date": "1987",
  "issue_number": null
}
```

---

### Ejemplo 3 — Texto con ruido

Input:

```text
"REVlSTA  SEMANAL
Num3r0 42
Madr1d, 12 de marz0 de 1936"
```

Output:

```json
{
  "title": "Revista Semanal",
  "publication_date": "1936-03-12",
  "issue_number": "42"
}
```

---

## 7. Variantes del Prompt

### Tipos

- simplificada
- extendida
- estricta
- optimizada

---

### Uso

- retry
- fallback
- experimentación

---

## 8. Buenas Prácticas

- instrucciones claras
- evitar ambigüedad
- definir formato de salida
- minimizar dependencias implícitas

---

### Restricciones (Negative Constraints)

- no incluir texto fuera del JSON
- no añadir explicaciones
- no usar bloques Markdown
- no devolver múltiples objetos

---

## 9. Versionado

### Estrategia

- cambios menores
- cambios mayores

---

### Change Log

| Versión | Fecha      | Cambio                                | Motivo                                |
| ------- | ---------- | ------------------------------------- | ------------------------------------- |
| 1.0     | 2024-01-10 | Versión inicial                       | Creación del prompt                   |
| 1.1     | 2024-01-15 | Ajuste en formato de salida           | Evitar texto adicional fuera del JSON |
| 1.2     | 2024-01-20 | Mejora en instrucciones de extracción | Reducir errores en fechas             |

---

## 10. Validación del Prompt

### Criterios

- estabilidad
- consistencia
- tasa de error

---

### Métodos

- pruebas manuales
- evaluación automática

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
