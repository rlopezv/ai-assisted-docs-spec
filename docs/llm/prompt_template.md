---
document: Prompt Template
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.0
last_updated: [YYYY-MM-DD]
owners:

- [Responsable]
  related_documents:
- llm/02_prompt_library.md
- llm/03_output_schemas.md
- data/02_data_dictionary.md

---

# Prompt Definition

## 1. Identificación

- prompt_id:
- nombre:
- descripción:
- tipo:
- versión:

---

### Ejemplo

- prompt_id: `extract_metadata_v1`
- nombre: Extracción de metadatos
- descripción: Extrae campos clave de texto no estructurado
- tipo: extracción
- versión: 1.0

---

## 2. Propósito

Definir qué debe hacer el prompt.

---

### Ejemplo

> Extraer información estructurada a partir de texto y devolverla en formato JSON válido.

---

## 3. Definición del Prompt

---

### System Prompt

Define el rol del modelo.

---

### Ejemplo

```text id="s4q2nx"
Eres un sistema experto en extracción de datos estructurados.
```

---

### Instrucciones

Definir pasos claros y numerados.

---

### Ejemplo

```text id="c2h4bn"
1. Analiza el texto proporcionado.
2. Identifica los campos relevantes.
3. Extrae únicamente información presente en el texto.
4. No infieras datos no explícitos.
5. Devuelve el resultado en formato JSON.
```

---

### Input

Definir el contenido dinámico.

---

### Ejemplo

```text id="n8f3pw"
Input:
"{input_text}"
```

---

### Formato de salida

Definir explícitamente el formato.

---

### Ejemplo

```text id="k9t2mv"
OUTPUT: JSON literal
```

---

## 4. Variables

Definir variables utilizadas.

---

### Tabla de variables

| Variable | Descripción | Tipo | Obligatorio | Preprocesado |
| -------- | ----------- | ---- | ----------- | ------------ |

---

### Ejemplo

| Variable   | Descripción        | Tipo   | Obligatorio | Preprocesado    |
| ---------- | ------------------ | ------ | ----------- | --------------- |
| input_text | Texto a procesar   | string | Sí          | limpieza básica |
| context    | Contexto adicional | string | No          | normalización   |

---

## 5. Parámetros de Inferencia

Definir configuración del modelo.

---

- temperature:
- top_p:
- max_tokens:

---

### Ejemplo

- temperature: 0.0
- top_p: 1.0
- max_tokens: 512

---

## 6. Output Esperado

Referencia al schema definido.

---

### Ejemplo

Ver:

```text id="z6q1wf"
llm/03_output_schemas.md#[nombre_schema]
```

---

### Ejemplo de salida

```json id="k3p9vb"
{
  "title": "Documento",
  "publication_date": "2024-01-01"
}
```

---

## 7. Restricciones (Negative Constraints)

Definir qué NO debe hacer el modelo.

---

### Ejemplo

- no incluir texto explicativo
- no usar markdown
- no añadir comentarios
- no devolver múltiples objetos
- no inventar información

---

## 8. Post-procesado (opcional)

Definir limpieza o validación.

---

### Ejemplo

- eliminar bloques ```json
- validar JSON
- normalizar formatos

---

## 9. Casos de Prueba

Definir inputs y outputs esperados.

---

### Ejemplo

Input:

```text id="n2r8kc"
"Boletín Oficial
15 de abril de 1952
Número 128"
```

Output esperado:

```json id="p4k2st"
{
  "title": "Boletín Oficial",
  "publication_date": "1952-04-15",
  "issue_number": "128"
}
```

---

## 10. Versionado

Registrar cambios del prompt.

---

### Estructura

| Versión | Cambio | Fecha |
| ------- | ------ | ----- |

---

### Ejemplo

| Versión | Cambio                  | Fecha      |
| ------- | ----------------------- | ---------- |
| 1.0     | Versión inicial         | 2024-01-01 |
| 1.1     | Ajuste de instrucciones | 2024-02-01 |

---

## 11. En el caso de utilizar IA / LLM

Este documento aplica directamente.

---
## 12. Ejemplo Completo (End-to-End)

Este ejemplo muestra la ejecución completa del prompt.

---

### Input

```text
REVISTA SEMANAL
Número 42
Madrid, 12 de marzo de 1936
```

### Prompt
System Prompt
Eres un sistema experto en extracción de datos estructurados a partir de texto.
Instrucciones
1. Analiza el texto proporcionado.
2. Identifica los siguientes campos:
   - title
   - publication_date
   - issue_number
3. Extrae únicamente información presente en el texto.
4. No infieras datos no explícitos.
5. Devuelve el resultado en formato JSON válido.
6. No incluyas texto adicional.

### Input
"{input_text}"

### Output esperado
{
  "title": "Revista Semanal",
  "publication_date": "1936-03-12",
  "issue_number": "42"
}

### Consideraciones
- El output debe cumplir el schema definido en llm/03_output_schemas.md
- No debe incluir texto adicional
- No debe incluir bloques markdown

---


## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento define un prompt individual.

---

### Instrucciones

- seguir estructura definida en Prompt Library
- mantener alineación con Output Schemas
- evitar ambigüedad

---

### Riesgos

- outputs inconsistentes
- alucinaciones
- variabilidad entre ejecuciones

---

### Dudas abiertas

- ajuste de parámetros
- cobertura de edge cases
