# business_review.md

## Estado general

- Capa bien estructurada y usable.
- Ejemplos presentes y útiles.
- No hay problemas graves de diseño.
- Requiere ajustes menores para mejorar coherencia y claridad.

---

## 1. 01_project_brief.md

### Correcto

- Define bien el contexto del proyecto.
- Claridad en problema, objetivos y restricciones.
- Ejemplos útiles para entender el contenido esperado.

### Problema

- Incluye contenido demasiado técnico para esta capa:
  - Estrategia de procesamiento
  - Niveles como parsing, LLM o RAG

Esto rompe el nivel de abstracción esperado en Business.

### Ajuste necesario

- Hacer la sección más conceptual y menos técnica.
- Mantener el ejemplo pero sin referencias tecnológicas explícitas.

---

## 2. 02_prd.md

### Correcto

- Buena estructura de requisitos.
- Incluye casos de uso, requisitos y validación.
- Trata LLM como opcional de forma correcta.

### Problema

- Falta de ejemplos en comparación con otros documentos.
- Menor capacidad de guía para el usuario.

### Ajuste necesario

Añadir ejemplos en:

- Casos de uso
- Requisitos funcionales
- Criterios de aceptación

---

## 3. 03_roadmap.md

### Correcto

- Documento claro y bien delimitado.
- Uso adecuado de ejemplos.
- No mezcla planificación con implementación técnica.

### Problema

- El backlog puede interpretarse como un sistema de gestión de tareas.

### Ajuste necesario

Añadir una aclaración indicando que:

- El backlog es orientativo
- No sustituye herramientas de gestión de tareas

---

## 4. Ejemplos (visión transversal)

### Correcto

- Facilitan la comprensión de las plantillas.
- Ayudan a reducir ambigüedad.

### Riesgos

- Pueden interpretarse como caso por defecto.
- Falta de consistencia en su formato.

### Ajuste necesario

Estandarizar el formato:

### Ejemplo

Y aplicar las siguientes reglas:

- Ejemplos breves
- Ejemplos concretos
- No prescriptivos
- No vinculados a un único tipo de proyecto

---

## Resultado esperado

Tras aplicar los ajustes:

- Mejor separación entre niveles (Business vs técnico)
- Mayor consistencia entre documentos
- Plantillas más fáciles de usar
- Ejemplos más homogéneos