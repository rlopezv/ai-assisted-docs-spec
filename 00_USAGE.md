# Uso del framework documental

## Propósito

Este documento define cómo usar el framework documental de forma práctica y sin sobrecarga.

Incluye:

- Reglas mínimas de uso.
- Orden recomendado de instanciación.
- Criterios para decidir cuándo avanzar entre capas.

---

## 1. Reglas de uso

### 1.1. Orden de trabajo

El orden recomendado de trabajo es:

- Business
- Data
- Architecture
- API
- LLM
- QA
- Operations

La capa LLM es opcional y solo debe usarse cuando el proyecto incorpore capacidades de IA.

### 1.2. Principio de dependencias

Cada capa debe apoyarse en la información definida en las capas anteriores.

No se recomienda avanzar a una capa si las decisiones necesarias de la capa anterior aún no están claras.

### 1.3. Criterio de completitud

Un documento se considera suficientemente completo cuando:

- Cumple su propósito principal.
- Puede ser entendido sin contexto externo excesivo.
- Permite avanzar a la siguiente capa sin ambigüedad relevante.

### 1.4. Criterio de simplicidad

No todos los documentos deben rellenarse siempre.

Si una capa, documento o sección no aporta valor al proyecto concreto, puede omitirse o dejarse explícitamente como no aplicable.

---

## 2. Orden de instanciación

### 2.1. Business

Crear primero los documentos de contexto y producto:

- `business/01_project_brief.md`
- `business/02_prd.md`

No avanzar si:

- El problema no está claro.
- El alcance no está acotado.
- Los requisitos principales son ambiguos.

### 2.2. Data

Definir el modelo de dominio:

- `data/01_domain_model.md`

Usar si aporta valor:

- `data/02_data_dictionary.md`

No avanzar si:

- Las entidades principales no están claras.
- La nomenclatura es inconsistente.
- Las relaciones entre entidades son ambiguas.

### 2.3. Architecture

Definir la visión técnica:

- `architecture/01_architecture_overview.md`

Usar si aporta valor:

- `architecture/02_technical_design.md`
- ADRs

No avanzar si:

- Los componentes principales no están definidos.
- El flujo de datos no está claro.
- Las decisiones técnicas relevantes no están justificadas.

### 2.4. API

Usar esta capa si el sistema expone o consume contratos externos:

- `api/01_api_spec.md`

No avanzar si:

- Las entradas y salidas no están claras.
- Las responsabilidades de los endpoints son ambiguas.

### 2.5. LLM

Usar esta capa solo si el sistema incorpora capacidades de IA:

- `llm/01_llm_integration_spec.md`
- `llm/02_prompt_library.md`
- `llm/03_output_schemas.md`

No avanzar si:

- Las entradas y salidas del modelo no están estructuradas.
- Los prompts son ambiguos.
- El comportamiento esperado no es verificable.

### 2.6. QA

Definir cómo se valida el sistema:

- `qa/01_evaluation_plan.md`
- `qa/02_test_strategy.md`

No avanzar si:

- No existen criterios de éxito claros.
- Los resultados esperados no pueden validarse.

### 2.7. Operations

Definir la operación del sistema:

- `operations/01_operational_spec.md`

Usar si aporta valor:

- `operations/02_setup_guide.md`
- `operations/03_runbook.md`
- `operations/04_deployment.md`

No avanzar si:

- El sistema no puede ejecutarse de extremo a extremo.
- Las responsabilidades operativas no están claras.

---

## 3. Bucles de refinamiento

El proceso no es estrictamente lineal. Es normal tener que volver a capas anteriores a medida que se descubren nuevos detalles.

### 3.1. Principio general

Se permite volver a una capa anterior cuando:

- Aparece nueva información relevante.
- Se detectan inconsistencias.
- Una decisión posterior invalida una anterior.

El objetivo es mantener coherencia global, no seguir el orden de forma rígida.

---

### 3.2. Regla de impacto

Cuando se modifica una capa, deben revisarse las capas dependientes.

Ejemplo:

- Cambios en Data → revisar Architecture y API  
- Cambios en API → revisar LLM y QA  
- Cambios en Architecture → revisar Operations  

No es necesario rehacer todo, pero sí validar consistencia.

---

### 3.3. Iteración controlada

Los bucles deben ser:

- Localizados (no reabrir todo el sistema innecesariamente)
- Justificados (basados en cambios reales)
- Acotados (evitar iteraciones infinitas)

---

### 3.4. Señales de que debes iterar

Volver atrás si ocurre alguno de estos casos:

- Entidades que no encajan con los casos de uso
- APIs difíciles de definir o inconsistentes
- Decisiones técnicas forzadas o artificiales
- Prompts o outputs que no se pueden validar
- Dificultad para operar o desplegar el sistema

---

### 3.5. Señales de sobre-iteración

Evitar seguir iterando si:

- Los cambios no afectan al comportamiento real del sistema
- Se están refinando detalles irrelevantes
- No hay impacto en implementación o validación

---

### 3.6. Criterio práctico

Preferir:

- Consistencia suficiente → sobre perfección
- Avance controlado → bloqueo por refinamiento continuo

---

## 4. Antipatrones

Evitar:

- Rellenar todos los documentos por obligación.
- Trabajar todas las capas en paralelo sin dependencias claras.
- Definir APIs antes de tener claro el modelo de datos.
- Documentar funcionalidades especulativas.
- Mantener documentos que no aportan valor al proyecto.

---

## 5. Nota final

El objetivo del framework no es producir más documentación, sino producir documentación más clara, coherente y útil.

Si un documento no ayuda a tomar decisiones, implementar, validar u operar el sistema, debe simplificarse, omitirse o marcarse como no aplicable.