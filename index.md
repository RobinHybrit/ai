# AI

Welkom 🦙 🐳

## 0. Agenda voor AI

1. Bestanden
2. Endor en AI
3. Endor architectuur
4. LLama en DeepSeek
5. Ollama en Docker
6. Hardware acceleration
7. Retrieval Argumentation Generation (RAG)
8. Terminology
9. LangChain
10. Vraagstukken
11. Speeltijd

## 1. Bestanden

Benodigdheden:

- Git
- Docker (met compose)
- Connectie naar het interne network OF schrijf ruimte

Bestanden:

```bash
git clone https://github.com/robinHybrit/ai
```

## 2. Endor en AI

- Contracten (ContractIQ)
- Chatbot
- Micro services
- Dotnet

## 3. Endor architectuur

[./endor-design.png]

## 4. LLama en DeepSeek

- Large language models
- LLama - Meta (Facebook)
- DeepSeek - China
- Allebei offline
- Ollama voor Docker

## 5. Ollama en Docker

Te gebruiken op de Dagobah server OF via Docker:

```yml
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
```

```bash
docker compose up -d ollama
docker compose exec -it ollama ollama run llama3.2
docker compose down -v ollama
```

## 6. Hardware acceleration

1. Docker installeren
2. NVIDIA Container Toolkit
3. GPU koppelen

```bash
docker run --rm -it --runtime=nvidia --gpus all  ubuntu:latest nvidia-smi
```

```yml
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - "11434:11434"
    volumes:
      - ollama:/root/.ollama
    environment:
      - OLLAMA_HOST=0.0.0.0
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

## 7. Terminology

- System prompt
- Embeddings
- Retrieval Argumentation Generation (RAG)
- Fine-tuning
- Reasoning loop

## 8. Retrieval Argumentation Generation (RAG)

- Documenten
- Embeddings
- Vectorizing
- Searching
- Database
  - Postgres
  - Redis
  - etc.

## 9. LangChain

- Python
- System prompt
- Tools

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    base_url="http://192.168.1.21:11434",
    model="llama3.2",
    temperature=0,
)

result = llm.invoke("Test")
print(result.content)
```

## 10. Vraagstukken

- Hoe verbeteren wij de resultaten
- Hoe we een reasoning loop implementeren

## 11. Speeltijd

Nu zelf spelen met LangChain en LLama.
Bewerk de `index.py` met je favorite text editor of IDE.

- IP Dagobah `192.168.1.21:11434`
- Bevat `llama3.2`

```bash
docker compose run development
python index.py
```
