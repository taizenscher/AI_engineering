# AI Engineering Base Project

## Objetivo

Construir un framework de agentes desde cero mientras se aprenden los fundamentos de AI Engineering.

El foco del proyecto es comprender la arquitectura detrás de:

- Agentes
- Conversaciones
- LLMs
- Memoria
- Herramientas
- Sistemas multiagente

## Estado
- ✅ Sprint 0 — Estructura del proyecto
- ✅ Sprint 1 — Configuración y cliente LLM
- ✅ Sprint 2 — BaseAgent
- ✅ Sprint 3 — Modelo de conversación

## Arquitectura actual
```app.py -> BaseAgent -> Conversation -> LLMClient -> Ollama```

## Componentes implementados
```
config/
    Settings
logging/
    Logging centralizado
llm/
    LLMClient
agents/
    BaseAgent
models/
    Message
    Conversation
```

## Flujo actual
Usuario -> Message(role="user") -> Conversation -> LLMClient -> Ollama -> Message(role="assistant") -> Conversation

## Roadmap
✅ Configuración
✅ Cliente LLM
✅ Agente base
✅ Conversación
⏳ System Prompt
⏳ Historial completo
⏳ Memory
⏳ Tools
⏳ RAG
⏳ Multi-Agent
⏳ Workflows

## Tecnologías
- Python
- Ollama
- dotenv
- Logging
- Git
