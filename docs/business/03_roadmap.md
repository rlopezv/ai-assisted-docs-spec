---
document: Roadmap
status: Draft
last_refined_by: AI-Coworker
version: 1.0
---
# Roadmap: mag-intel-local

## 1. Introducción
[Define el propósito de este documento: trazar la evolución del sistema desde un prototipo funcional hasta una solución completa de inteligencia documental. Debe explicar que el roadmap es flexible y se ajustará según los hallazgos técnicos en cada fase].

## 2. Puntos Clave
- [Punto 1, ej: Enfoque en "MVP Primero": priorizar la extracción sobre la búsqueda avanzada].
- [Punto 2, ej: Dependencia de hitos: no pasar a la Fase X hasta que la tasa de acierto del OCR sea >90%].

## 3. Fase 1: Cimientos e Ingesta (MVP)
[Define el objetivo de la primera etapa. Describe las tareas de desarrollo base: configuración de Python, gestión de archivos 7z, extracción de texto nativo y guardado básico en SQLite].

## 4. Fase 2: Enriquecimiento con IA (Inferencia)
[Define el salto a la inteligencia. Describe la integración con Ollama, la implementación del pipeline de degradación (Heurística -> LLM) y la validación de metadatos con Pydantic].

## 5. Fase 3: Capacidad Semántica (RAG)
[Define la optimización de búsqueda. Describe la implementación de LanceDB, la vectorización de contenidos y la capacidad de realizar consultas en lenguaje natural sobre la hemeroteca].

## 6. Fase 4: Optimización y UI
[Define la madurez del sistema. Describe la implementación de SAG (Speculative Automated Generation) para velocidad, refinamiento de prompts y, opcionalmente, una interfaz de usuario para visualización].

## 7. Backlog de Ideas Futuras
[Define el "cementerio de ideas" o mejoras no críticas. Describe funcionalidades que podrían ser útiles pero no están en el plan actual, como multilingüismo avanzado, detección de imágenes/anuncios o exportación a otros formatos].

## Anexo. Notas de Coworking
[Define el registro de por qué se movieron fechas o prioridades, qué dificultades técnicas obligaron a pivotar una fase y el historial de hitos alcanzados con éxito].