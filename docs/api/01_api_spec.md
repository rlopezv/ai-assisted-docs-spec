---
document: API Specification
project: [NOMBRE_DEL_PROYECTO]
status: Draft
version: 1.1
last_updated: [YYYY-MM-DD]
owners:
  - [Rol o responsable]
related_documents:
  - business/02_prd.md
  - architecture/01_architecture_overview.md
  - data/01_domain_model.md
  - data/02_data_dictionary.md

---

# API Specification

## 1. Introducción

Este documento define el **contrato externo de la API** del sistema, independientemente de la tecnología utilizada para implementarla.

Debe especificar:

- endpoints disponibles
- métodos HTTP
- comportamiento de la API
- códigos de error
- reglas de versionado
- relación entre endpoints y módulos internos

La definición técnica ejecutable de la API se mantiene en el contrato OpenAPI del repositorio de implementación:

```text
/<api>/openapi.yaml
```

Este documento:

* explica el comportamiento y propósito de la API
* define semántica y reglas de uso
* proporciona ejemplos

No define:

* schemas formales
* validaciones estructurales
* tipos técnicos exactos

Estos elementos se definen en OpenAPI.

Los recursos y estados expuestos por la API deben derivarse del modelo de dominio definido en `01_domain_model.md`.

La API no debe introducir conceptos que no existan en el dominio.

---

### Ejemplo

> Esta API expone operaciones para crear trabajos de procesamiento, consultar su estado y recuperar resultados estructurados.

---

## 2. Principios de Diseño de la API

Definir los principios que guían el diseño de la API.

* [Principio 1]
* [Principio 2]
* [Principio 3]

---

### Ejemplo

* API versionada
* Contratos explícitos
* Errores estructurados
* Separación entre modelos internos y modelos públicos
* Endpoints delgados que delegan en servicios internos
* No duplicación de schemas definidos en OpenAPI

---

## 3. Versionado

Definir la estrategia de versionado de la API.

### Estrategia

* Versión actual:
* Formato de versión:
* Política de cambios incompatibles:

---

### Ejemplo

```text
/api/v1/...
```

---

### Consideraciones

* Los breaking changes deben generar una nueva versión.
* Los schemas públicos deben tratarse como contratos estables.
* La versión de API no tiene por qué coincidir con la versión del proyecto.
* El versionado formal debe reflejarse en OpenAPI.

---

## 4. Contrato OpenAPI

La definición técnica ejecutable de la API se mantiene en:

```text
/<api>/openapi.yaml
```

Este archivo define:

* endpoints (paths)
* métodos HTTP
* parámetros
* request bodies
* response bodies
* schemas públicos
* códigos HTTP
* enumeraciones

Este documento no debe duplicar esa definición.

---

## 5. Convenciones Generales

Definir convenciones comunes para todos los endpoints.

---

### Formato

* Request:
* Response:
* Encoding:
* Content-Type:

---

### Identificadores

* Formato de IDs:
* Convención de nombres:

---

### Fechas

* Formato:
* Timezone:

---

### Endpoints de Health Check

Definir endpoints para verificar el estado del sistema y sus dependencias.

* health general:
* health de dependencias:
* health de recursos:

---

### Ejemplo

* Request/Response: JSON
* Content-Type: `application/json`
* Fechas: ISO 8601
* IDs: UUID

Health endpoints:

* `GET /health` → estado general
* `GET /health/dependencies` → estado de servicios internos
* `GET /health/resources` → estado de CPU/GPU/memoria

---

### Consideraciones

* La API puede estar disponible aunque las dependencias no lo estén
* Los health checks deben permitir detectar fallos parciales del sistema

---

## 6. Autenticación y Autorización (opcional)

Definir cómo se controla el acceso a la API.

### Autenticación

* Método:
* Requerida: sí/no

### Autorización

* Roles:
* Permisos:

---

### Ejemplo

* API local sin autenticación en MVP
* Autenticación mediante token en despliegues compartidos

---

## 7. Endpoints

Definir cada endpoint expuesto por la API.

---

### 7.1 `[METHOD] /api/v1/[resource]`

Descripción:

* ...

Propósito:

* ...

Componente o módulo interno asociado:

* Referencia al componente o módulo responsable del comportamiento.
* Esta relación es conceptual y no implica acoplamiento directo.

Contrato OpenAPI:

```text
/<api>/openapi.yaml#/paths/...
```

Request (ejemplo):

```json
{
  "field": "value"
}
```

Response (ejemplo):

```json
{
  "field": "value"
}
```

Errores:

* `400 Bad Request`
* `404 Not Found`
* `500 Internal Server Error`

Flujo asociado:

* Referencia al flujo definido en el TDD donde se implementa este endpoint.

Notas:

* ...

---

### Ejemplo

### 7.1 `POST /api/v1/jobs`

Descripción:

* Crea un trabajo de procesamiento.

Propósito:

* Registrar una entrada para procesamiento asíncrono.

Componente o módulo interno asociado:

* `orchestration`

Contrato OpenAPI:

```text
/<api>/openapi.yaml#/paths/~1api~1v1~1jobs/post
```

Request:

```json
{
  "input_path": "/path/to/file.pdf"
}
```

Response:

```json
{
  "job_id": "job_123",
  "status": "queued"
}
```

Errores:

* `400 Bad Request`: input inválido
* `409 Conflict`: trabajo duplicado

Flujo asociado:

* Flujo de creación y encolado de job definido en el TDD.

---

## 8. Schemas Públicos

Los schemas públicos se definen en:

```text
/<api>/openapi.yaml#/components/schemas
```

Este documento:

* describe el significado de los datos
* proporciona ejemplos

No define:

* tablas de campos
* tipos formales
* validaciones estructurales

---

### Ejemplo

Schema: `JobResponse`

```json
{
  "job_id": "job_123",
  "status": "queued"
}
```

---

## 9. Modelo de Errores

La estructura formal de errores se define en:

```text
/<api>/openapi.yaml#/components/schemas/ErrorResponse
```

---

### Error Response

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable message",
    "details": {},
    "provider_error": {}
  }
}
```

---

### Consideraciones

* `provider_error` permite capturar errores internos o de dependencias
* No debe usarse como contrato estable
* OpenAPI define la estructura formal

---

### Códigos de error

| Código HTTP | Código interno   | Descripción           |
| ----------- | ---------------- | --------------------- |
| 400         | INVALID_REQUEST  | Request inválida      |
| 404         | NOT_FOUND        | Recurso no encontrado |
| 409         | CONFLICT         | Conflicto de estado   |
| 422         | VALIDATION_ERROR | Error de validación   |
| 500         | INTERNAL_ERROR   | Error interno         |

---

## 10. Estados y Ciclo de Vida

Definir estados relevantes expuestos por la API.

Los estados expuestos deben coincidir con los definidos en el Domain Model.

La API no debe introducir estados adicionales sin reflejarlos en el modelo de dominio.

---

### Ejemplo

```text
queued → running → completed
                 → failed
```

---

### Consideraciones

* Los estados deben alinearse con el Domain Model
* La enumeración formal debe definirse en OpenAPI

---

## 11. Operaciones Asíncronas

Definir cómo se gestionan operaciones largas.

---

### Estrategia

* síncrona / asíncrona:
* mecanismo de consulta:
* timeout:
* cancelación:

---

### Política de concurrencia

* límite de concurrencia:
* estrategia:

  * cola interna
  * rechazo
  * priorización

---

### Ejemplo

* número máximo de trabajos simultáneos limitado
* nuevas solicitudes se encolan
* si se supera capacidad → `503 Service Unavailable`

---

### Consideraciones

* evitar saturación de recursos
* proteger componentes críticos (ej. GPU, modelos)
* errores formales deben reflejarse en OpenAPI

---

## 12. Validación de Inputs

Las validaciones se dividen en:

* Validaciones estructurales:
  definidas en OpenAPI (tipos, formatos, campos obligatorios)

* Validaciones de negocio:
  definidas en este documento o en el Domain Model (reglas del sistema)

---

### Ejemplo

* rutas deben existir
* tipos deben cumplir schema
* tamaño máximo permitido
* formatos admitidos

---

### Consideraciones

* Validaciones estructurales deben definirse en OpenAPI
* Validaciones de negocio deben definirse aquí o en Domain Model

---

## 13. Seguridad y Exposición

Definir consideraciones de seguridad y acceso.

---

### Acceso a la API

* binding de red:
* exposición:
* restricciones:

---

### Ejemplo

* API accesible solo en `127.0.0.1`
* acceso restringido al entorno local
* no exposición pública por defecto

---

### Consideraciones

* definir explícitamente si la API es local o expuesta
* evitar exposición accidental de datos sensibles
* seguridad formal debe reflejarse en OpenAPI (`securitySchemes`)

---

## 14. Trazabilidad

Relacionar endpoints con requisitos, módulos y tests.

Cada endpoint debe estar asociado a:

* un requisito del PRD
* un componente o módulo interno
* un flujo de ejecución definido en el TDD

| Endpoint | PRD Item | Módulo interno | Test |
| -------- | -------- | -------------- | ---- |
|          |          |                |      |

---

### Ejemplo

| Endpoint            | PRD Item | Módulo interno | Test       |
| ------------------- | -------- | -------------- | ---------- |
| `POST /api/v1/jobs` | FR-01    | orchestration  | API-TC-001 |

---

## 15. Limitaciones

Definir límites conocidos de la API.

---

### Tipos de limitación

* tamaño de input
* tiempo de ejecución
* capacidad del sistema

---

### Timeouts por fase

* operaciones de IO:
* operaciones de procesamiento:
* operaciones de inferencia:

---

### Consideraciones

* evitar timeouts prematuros
* diferenciar fases del sistema
* límites que afecten al contrato deben reflejarse en OpenAPI

---

## Anexo. Notas de Coworking (IA Assistant)

### Contexto

Este documento define el contrato externo de la API.

La definición formal ejecutable se encuentra en:

```text
/<api>/openapi.yaml
```

---

### Instrucciones

* No mezclar modelos internos con schemas públicos.
* No duplicar schemas definidos en OpenAPI.
* Mantener coherencia con TDD, PRD y Data Dictionary.
* No introducir endpoints sin justificar su relación con requisitos.

---

### Riesgos

* endpoints acoplados a implementación interna
* duplicación entre API Spec y OpenAPI
* schemas públicos inconsistentes
* errores no normalizados

---

### Dudas abiertas

* estrategia de autenticación
* política de cancelación de jobs
* límites de tamaño por request

### Inputs utilizados

* ...

### Insights clave

* ...

