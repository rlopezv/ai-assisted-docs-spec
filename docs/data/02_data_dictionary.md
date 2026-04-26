---
document: Data Dictionary
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.1
last_updated: [YYYY-MM-DD]
owners:
  - [Responsable]
related_documents:
  - [Documentos relevantes del proyecto]
---

# Data Dictionary

## 1. Introducción

Este documento define el **diccionario de datos del sistema**, especificando los campos, tipos, formatos y restricciones utilizados para representar la información.

Su objetivo es:

- estandarizar la estructura de los datos  
- asegurar consistencia entre componentes  
- facilitar validación y procesamiento  
- servir como referencia para API, persistencia y procesamiento  

Este documento no define:

- entidades conceptuales (ver Domain Model)  
- reglas de negocio  
- endpoints de API  
- detalles de implementación  

---

### Ejemplo

> Este documento define los campos necesarios para representar entidades del sistema y sus atributos asociados.

---

## 2. Alcance

### Incluido

- definición de campos  
- tipos de datos  
- formatos  
- restricciones  
- valores permitidos  

### Excluido

- lógica de negocio  
- relaciones entre entidades  
- flujos de procesamiento  

---

## 3. Convenciones Generales

### Tipos de datos

| Tipo lógico | Descripción |
|-------------|-------------|
| string | texto |
| integer | número entero |
| float | número decimal |
| boolean | verdadero/falso |
| datetime | fecha y hora |
| object | estructura anidada |
| list | colección de elementos |

---

### Formatos

- fechas: ISO 8601  
- texto: UTF-8  
- identificadores: string  

---

### Nombres de campos

- snake_case  
- nombres descriptivos  
- evitar abreviaturas ambiguas  

---

## 4. Definición de Campos

Definir campos agrupados por entidad lógica (sin redefinir la entidad).

---

### 4.1 `[Entidad]`

| Campo | Tipo | Obligatorio | Nullable | Sensibilidad | Descripción | Ejemplo |
|------|------|-------------|----------|--------------|-------------|---------|

---

### Sensibilidad (opcional)

Clasificación del campo según su nivel de sensibilidad.

Valores posibles:

- none  
- low  
- high (PII u otros datos sensibles)  

---

### Ejemplo

### 4.1 `Document`

| Campo | Tipo | Obligatorio | Nullable | Sensibilidad | Descripción | Ejemplo |
|------|------|-------------|----------|--------------|-------------|---------|
| document_id | string | sí | no | none | Identificador único | "doc_123" |
| source_path | string | sí | no | low | Ruta del archivo | "/files/a.pdf" |
| created_at | datetime | sí | no | none | Fecha de creación | "2026-01-01T10:00:00Z" |

---

## 5. Restricciones

Definir reglas de validación a nivel de datos.

---

### Tipos de restricción

- unicidad  
- longitud mínima/máxima  
- rango de valores  
- obligatoriedad  

---

### Restricciones avanzadas (opcional)

- expresiones regulares (regex)  
- validaciones de formato  

---

### Ejemplo

- `document_id` debe ser único  
- `source_path` no puede estar vacío  
- identificadores con formato específico pueden validarse mediante regex  

---

## 6. Valores Permitidos (Enumeraciones)

Definir valores cerrados para campos categóricos.

---

### 6.1 `[Campo]`

| Valor | Descripción |
|------|-------------|

---

### Normalización de valores (opcional)

Permite transformar variantes a un valor canónico.

---

### Ejemplo

| Entrada | Valor canónico |
|--------|----------------|
| "ene." | "01" |
| "enero" | "01" |
| "01" | "01" |

---

## 7. Campos Derivados

Campos calculados a partir de otros datos.

---

### Ejemplo

- duración → diferencia entre timestamps  
- estado agregado → derivado de múltiples condiciones  

---

## 8. Campos Inferidos (opcional)

Campos cuyo valor se obtiene mediante deducción o procesamiento adicional.

---

### Metadatos de inferencia (recomendado en sistemas IA)

- nivel de confianza  
- origen del dato  

---

### Ejemplo

- `publication_date` inferida del contenido  
- `author` inferido del texto  

---

### Consideraciones

- opcional  
- útil en sistemas probabilísticos  
- debe permitir trazabilidad  

---

## 9. Calidad de Datos

Definir criterios de calidad.

---

### Ejemplo

- campos críticos requieren alta precisión  
- campos secundarios permiten valores parciales  

---

## 10. Consistencia

Reglas de coherencia entre campos.

---

### Ejemplo

- `completed_at` requiere estado `completed`  
- no puede existir resultado sin identificador asociado  

---

## 11. Evolución del Modelo

Definir cómo evolucionan los datos.

---

### Ejemplo

- nuevos campos deben ser opcionales inicialmente  
- cambios incompatibles requieren versionado  

---

## 12. Relación con otros documentos

### Domain Model

- define entidades y comportamiento  
- este documento define atributos  

### API Spec

- expone subconjuntos del diccionario  

### Persistencia

- implementa este modelo  

---

## 13. Limitaciones

- dependencia de calidad de entrada  
- posibles inconsistencias en datos inferidos  
- variabilidad en datos no estructurados  

---

## Anexo. Criterios de Uso

Este documento debe completarse cuando:

- existan nuevas entidades del dominio
- cambien reglas de negocio
- se añadan campos estructurados
- cambien restricciones de datos

No debe usarse para:

- definir endpoints
- definir tablas físicas
- documentar implementación

---

## Anexo. Notas de Coworking (IA Assistant)

### Instrucciones

- no definir lógica de negocio  
- no redefinir entidades  
- mantener coherencia en tipos y nombres  
- validar consistencia entre campos  

---

### Riesgos

- duplicación con Domain Model  
- inconsistencias con API  
- ambigüedad en campos  
- falta de validación  

---

### Dudas abiertas

- definición de campos obligatorios  
- gestión de valores nulos  
- estrategia de evolución  