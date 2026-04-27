# ai-assisted-docs-spec

Estructuras, plantillas y especificaciones para la documentación técnica en entornos de desarrollo asistidos por IA.

---

## 🎯 Propósito

Este repositorio define un **framework de documentación técnica estructurada**, diseñado para:

- actuar como única fuente de verdad del sistema
- facilitar la coherencia entre artefactos
- permitir interpretación tanto por humanos como por asistentes de IA

El objetivo es cerrar la brecha entre:

```text
documentación tradicional → documentación estructurada y operativa
```

Este repositorio define **plantillas y especificaciones**, no implementaciones concretas. Los proyectos reales deben instanciar estos documentos, adaptarlos a su contexto y evolucionarlos según sus necesidades.

---

## 🏗️ Estructura del Repositorio

```text
/
├── docs/       # Framework documental — plantillas y especificaciones
├── tools/      # Herramientas de mantenimiento y validación local
└── prompts/    # Prompts de trabajo para completar y validar plantillas (en desarrollo)
```

### Capas de documentación

La estructura completa se define en `docs/00_INDEX.md` y sigue una progresión lógica:

```text
Business → Data → Architecture → API → LLM → QA → Operations
```

| Capa | Directorio | Propósito |
| ---- | ---------- | --------- |
| Business & Strategy | `docs/business/` | Contexto, requisitos y objetivos del sistema |
| Data & Logic | `docs/data/` | Modelo de dominio y definición de datos |
| Architecture & Design | `docs/architecture/` | Diseño técnico y decisiones arquitectónicas |
| API | `docs/api/` | Contrato externo del sistema |
| LLM & AI Spec | `docs/llm/` | Integración con modelos de lenguaje (opcional) |
| QA & Validation | `docs/qa/` | Evaluación y estrategia de testing |
| Operations | `docs/operations/` | Entorno, instalación y operación del sistema |

---

## 👥 Roles

El framework está diseñado para equipos medianos donde una misma persona puede asumir varios roles simultáneamente.

| Rol | Responsabilidad principal en el framework |
| --- | ----------------------------------------- |
| **Product Owner** | Define el qué y el por qué. Propietario de la capa Business |
| **Tech Lead** | Define el cómo. Propietario de Architecture, decisiones técnicas e integración LLM |
| **Developer** | Implementa. Consume TDD, API Spec y Operations |
| **QA Engineer** | Valida. Propietario de la capa QA, consume criterios del PRD |
| **DevOps** | Despliega y opera. Propietario de la capa Operations |

### AI Coworker

El asistente de IA actúa como **copiloto transversal** a todos los roles y capas. No es un rol del equipo sino una herramienta de trabajo integrada en el flujo documental. Cada documento incluye un `## Anexo. Notas de Coworking (IA Assistant)` con instrucciones, contexto e inputs específicos para facilitar esta colaboración.

---

## 🧠 Principios del Framework

1. **Separación de responsabilidades**
   Cada documento tiene un propósito claro y no solapa con otros.

2. **Documentación estructurada**
   Formato consistente, versionable y procesable tanto por humanos como por IA.

3. **Agnosticismo tecnológico**
   Independiente del stack de implementación.

4. **Compatibilidad con IA**
   Diseñado para reducir ambigüedad y facilitar generación y validación asistida.

5. **Trazabilidad entre capas**
   Cada elemento puede relacionarse con su origen en Business y su destino en Operations.

---

## 🛠️ Herramientas (`tools/`)

Scripts Python para el mantenimiento y validación del framework en local. Todos aceptan `--dry-run` para previsualizar cambios sin aplicarlos.

| Script | Propósito |
| ------ | --------- |
| `fix_frontmatter.py` | Corrige problemas puntuales de frontmatter |
| `update_related_documents.py` | Sincroniza `related_documents` desde el mapa en `00_INDEX.md` |
| `normalize_sections.py` | Normaliza nombres de secciones comunes del Anexo |
| `update_index.py` | Regenera tabla de estado y diagrama Mermaid en `00_INDEX.md` |

### Orden de ejecución recomendado

```bash
python tools/fix_frontmatter.py
python tools/update_related_documents.py
python tools/normalize_sections.py
python tools/update_index.py
```

**Requisito:** `pip install pyyaml`

---

## 💬 Prompts (`prompts/`)

Directorio previsto para prompts de trabajo que faciliten:

- completar plantillas de cada capa
- validar coherencia entre documentos
- generar contenido específico asistido por IA

> En desarrollo. Las referencias a prompts de trabajo se registran en la sección `### Inputs utilizados` del `## Anexo. Notas de Coworking (IA Assistant)` de cada documento.

---

## 🔄 Evolución del Framework

### Fase 1 — Definición de plantillas ✅

- estructura base definida
- separación de responsabilidades establecida
- consistencia documental validada
- herramientas de mantenimiento implementadas

### Fase 2 — Aplicación en proyectos reales 🔄

- instanciación en proyecto real
- validación práctica del framework
- detección de gaps y fricciones
- ajuste iterativo de plantillas

### Fase 3 — Hardening (IA Assisted Development) ⏳

- documentación operativa para IA
- criterios de uso explícitos por documento
- validaciones cruzadas automatizadas
- generación asistida de contenido

---

## ⚠️ Estado del Proyecto

**Fase actual: transición Fase 1 → Fase 2**

El framework está estructuralmente completo como conjunto de plantillas. El siguiente paso es su validación mediante instanciación en un proyecto real, que permitirá detectar fricciones, gaps y oportunidades de mejora antes de abordar el hardening de Fase 3.
