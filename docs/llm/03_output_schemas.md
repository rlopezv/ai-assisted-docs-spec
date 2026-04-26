---
document: Output Schemas
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 2.1
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - llm/01_llm_integration_spec.md
  - llm/02_prompt_library.md
  - data/01_domain_model.md
  - data/02_data_dictionary.md

---

# Output Schemas

## 1. Introducción

Este documento define los **schemas de salida esperados del LLM**.

Su objetivo es:

- establecer el contrato de salida
- asegurar consistencia en los datos generados
- facilitar validación e integración

Este documento no define:

- prompts
- validación runtime
- detalles de implementación

---

## 2. Principios de Diseño

- consistencia con el modelo de dominio
- alineación con el data dictionary
- simplicidad estructural
- tolerancia a valores faltantes
- trazabilidad de los datos

---

## 3. Tipos de Output

El sistema admite diferentes niveles de enriquecimiento en la salida del LLM.

Estos formatos deben ser referenciados desde `llm/02_prompt_library.md` para que cada prompt indique qué tipo de salida espera.

---

### 3.1 Salida simple

Estructura con valores directos.

```json id="1b4mcz"
{
  "title": "Revista Semanal",
  "publication_date": "1936-03-12",
  "issue_number": "42"
}
```

---

### 3.2 Salida trazable

Estructura enriquecida con metadatos por campo.

```json id="u9x6av"
{
  "title": {
    "value": "Revista Semanal",
    "confidence": 0.95,
    "source_reference": "línea 1",
    "generation_type": "extracted"
  }
}
```

---

### Consideraciones

- ambos formatos deben ser compatibles con el pipeline
- la salida trazable permite auditoría y validación avanzada
- la salida simple es más ligera y fácil de consumir

---

## 4. Definición de Campos

Cada schema debe definir sus campos en alineación con el data dictionary.

---

### Ejemplo de tabla de campos

| Campo            | Tipo lógico | Obligatorio | Descripción          |
| ---------------- | ----------- | ----------- | -------------------- |
| title            | string      | Sí          | Título del documento |
| publication_date | string      | No          | Fecha de publicación |
| issue_number     | string      | No          | Número de ejemplar   |

---

### Ejemplo de instancia

```json id="7q1xwe"
{
  "title": "Revista Semanal",
  "publication_date": "1936-03-12",
  "issue_number": "42"
}
```

---

### Consideraciones

- usar nombres consistentes
- evitar duplicación con data dictionary
- mantener claridad semántica

---

## 5. Metadatos del LLM

Definir información adicional generada por el modelo.

---

### Tipos de metadatos

- nivel de confianza (`confidence`)
- origen del dato (`source_reference`)
- tipo de generación (`generation_type`)

---

### Ejemplo

```json id="v2k9pl"
{
  "publication_date": {
    "value": "1936-03-12",
    "confidence": 0.82,
    "source_reference": "inferido a partir del contexto",
    "generation_type": "inferred"
  }
}
```

---

### Consideraciones

- deben ser opcionales
- deben ser consistentes en todos los schemas

---

## 6. Campos Inferidos

Definir cómo se representan campos no explícitos en el input.

---

### Reglas

- identificar si un campo es inferido
- asociar nivel de confianza
- asociar origen del dato

---

## 7. Estructuras Compuestas

Definir cómo se agrupan múltiples entidades.

---

### Ejemplo: lista de objetos

```json id="k8c4me"
{
  "items": [
    {
      "title": "Documento A",
      "issue_number": "1"
    },
    {
      "title": "Documento B",
      "issue_number": "2"
    }
  ]
}
```

---

### Ejemplo: estructura anidada

```json id="5r9jda"
{
  "publication": {
    "name": "Revista Semanal",
    "issues": [
      {
        "issue_number": "42"
      }
    ]
  }
}
```

---

### Consideraciones

- mantener claridad estructural
- evitar duplicación de datos
- mantener consistencia entre niveles

---

## 8. Consistencia de Datos

Definir reglas de coherencia interna.

---

### Ejemplos

- si `issue_number` existe, `publication_date` debería existir
- si `generation_type` es `inferred`, la confianza debe ser menor que 1.0

---

## 9. Manejo de Valores Faltantes

Definir cómo representar ausencia de datos.

---

### Ejemplos

```json id="g2n1zv"
{
  "issue_number": null
}
```

```json id="r6p8ke"
{
  "title": "Revista Cultural"
}
```

---

### Consideraciones

- usar `null` para valores conocidos pero ausentes
- omitir campos cuando no aplican
- evitar valores ambiguos

---

## 10. Versionado de Schemas

### Estrategia

- cambios menores
- cambios mayores

---

### Ejemplo

| Versión | Cambio                     |
| ------- | -------------------------- |
| 1.0     | Definición inicial         |
| 1.1     | Añadido campo `confidence` |

---

### Consideraciones

- compatibilidad hacia atrás
- impacto en prompts y validación

---

## 11. Validación Esperada

Definir qué se espera validar sobre el output.

Esta sección define la validación lógica esperada sobre el output.

No define la ejecución runtime de la validación, que pertenece a `llm/01_llm_integration_spec.md`.


---

### Ejemplos

- el campo `title` debe ser string
- `publication_date` debe tener formato válido
- `confidence` debe estar entre 0 y 1

---

## 12. Limitaciones

- dependencia del modelo
- variabilidad del output
- errores en inferencias

---

## Anexo. Notas de Coworking (IA Assistant)

### Instrucciones

- no duplicar el data dictionary
- no definir lógica de validación
- mantener consistencia con domain model

---

### Riesgos

- inconsistencias entre prompts y schemas
- duplicación de definiciones
- schemas demasiado rígidos
