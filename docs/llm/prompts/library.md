# 📚 Biblioteca de Prompts del Proyecto

## 1. Prompts de Diseño y Análisis
### 1.0 Refinamiento de Documentos (Architect Mode)
**Propósito:** Desafiar un documento borrador buscando riesgos y puntos ciegos.
**Prompt:** 
"Actúa como un Senior Solution Architect. Hemos redactado este [DOCUMENTO]. Basado en mi stack... [RESTO DEL PROMPT]"

### 1.1 Refinador de Documentos de Arquitectura
**Propósito:** Activar el modo "Arquitecto Senior" para validar borradores.
**Prompt:**
> "Actúa como un Senior Solution Architect. Hemos redactado este [DOCUMENTO] para mag-intel-local. Basado en mi stack (Ollama, Python, 5060 Ti 16GB) y mi objetivo de procesar revistas:
> 1. Identifica 3 riesgos técnicos críticos (ej. gestión de memoria, límites de 7z, fallos de OCR).
> 2. Propón una restricción adicional que me ahorre problemas en la fase de implementación.
> 3. Pregúntame sobre 2 decisiones de negocio que aún faltan en el Brief (ej. manejo de duplicados, profundidad del RAG).
> Analiza el Brief y ayúdame a hacerlo más robusto antes de pasar al PRD."

## 2. Prompts de Inferencia (Runtime)
*Pendiente de definir en la fase de LLM Integration Spec*
