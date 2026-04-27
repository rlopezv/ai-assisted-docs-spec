---
document: Data Dictionary
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.0
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - data/01_domain_model.md
  - api/01_api_spec.md
---

# Data Dictionary

## 1. Introducción

Este documento define los atributos y estructuras de datos asociadas a las entidades del dominio.

Su objetivo es:

- detallar atributos de las entidades  
- establecer nomenclatura consistente  
- facilitar integración entre componentes  
- servir como referencia para API y persistencia  

Este documento es opcional y debe utilizarse cuando el modelo de datos requiere mayor precisión en la definición de atributos o nomenclatura.

---

### Ejemplo

> La entidad Usuario incluye atributos como id, email y estado, que deben ser consistentes en todo el sistema.

---

## 2. Alcance

### Incluido

- atributos de entidades  
- tipos lógicos  
- restricciones de datos  
- valores permitidos  

### Excluido

- estructura física de base de datos  
- detalles de implementación  
- lógica de negocio  

---

## 3. Convenciones

Definir reglas de nomenclatura y formato.

---

### Ejemplo

- nombres en snake_case  
- ids como strings  
- fechas en formato ISO 8601  

---

## 4. Definición de Entidades

Cada entidad definida en el modelo de dominio puede detallarse aquí si se requiere mayor precisión en sus atributos.

---

### Entidad: <Nombre>

| Campo | Tipo lógico | Obligatorio | Descripción |
|------|-------------|-------------|-------------|

---

### Ejemplo

Entidad: Usuario

| Campo  | Tipo lógico | Obligatorio | Descripción                      |
|--------|-------------|-------------|----------------------------------|
| id     | string      | sí          | identificador único              |
| email  | string      | sí          | dirección de correo              |
| estado | string      | sí          | estado del usuario               |

---

### Notas

- Los atributos deben corresponder con las entidades definidas en `01_domain_model.md`.
- Evitar duplicar información innecesaria.
- Usar este documento solo cuando aporte claridad adicional.

---

## 5. Restricciones

Definir reglas aplicables a los datos.

---

### Ejemplo

- email debe tener formato válido  
- estado debe pertenecer a un conjunto definido  

---

## 6. Valores permitidos

Definir enumeraciones o dominios cerrados.

---

### Ejemplo

Campo: estado

- activo  
- inactivo  
- suspendido  

---

## 7. Relación con otros modelos

### Domain Model

- define entidades y relaciones  

### API

- utiliza estos atributos en requests y responses  

### Persistencia

- implementa estos atributos en almacenamiento  

---

## 8. Limitaciones y Dudas

- ...

---

## Anexo. Criterios de Uso (IA Assisted)

Este documento debe completarse cuando:

- se definan atributos adicionales  
- se requiera precisión en tipos o valores  
- existan múltiples integraciones  

No debe usarse para:

- definir lógica de negocio  
- definir estructuras físicas  
- documentar implementación  

---

## Anexo. Notas de Coworking (IA Assistant)

### Instrucciones

- mantener consistencia de naming  
- evitar duplicación  
- no introducir lógica  

---

### Riesgos

- sobre-documentación  
- inconsistencias con domain model  

---

### Dudas abiertas

- ...

### Contexto

- ...

### Inputs utilizados

- ...

### Insights clave

- ...