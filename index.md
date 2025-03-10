# AI

Welkom 🦙 🐳

## 0. Agenda voor AI

1. Endor en AI
2. Endor architectuur
3. LLama en DeepSeek
4. Ollama en Docker
5. Hardware acceleration
6. Terminology
7. Retrieval-augmented Generation (RAG)
8. Frameworks zoals LangChain
9. Vraagstukken
10. Overleg en speeltijd

## 1. Endor en AI

- Contracten (ContractIQ)
- Chatbot
- Micro services
- Dotnet

## 2. Endor architectuur

[./endor-design.png]

## 3. LLama en DeepSeek

- Large language models
- LLama - Meta (Facebook)
- DeepSeek - China
- Allebei offline
- Ollama voor Docker

## 4. Ollama en Docker

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

## 5. Hardware acceleration

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

## 6. Terminology

- System prompt
- Embeddings
- Retrieval-augmented Generation (RAG)
- Fine-tuning
- Reasoning loop

## 7. Retrieval-augmented Generation (RAG)

- Documenten
- Embeddings
- Searching
- Database
  - Postgres
  - Redis
  - etc.

```
You're a pirate that helps with finding treasure from maps.

Maps: {documents}
```

## 7. Documenten

```markdown
Map

- number: 1000
- title: A map to gold
- directions: At the first tree turn left, ...
```

## 7. Embeddings

```json
{
    "model": "llama3.2",
    "embeddings": [ [-0.006212715, 0.012989915, -0.17035888, ... ] ]
}
```

## 7. Searching

```python
vector_store = RedisVectorStore(...)
query = "With which map can I find gold?"
results = vector_store.similarity_search(query)
```

```
I've got just the thing for ye, matey! ... *pulls out Map 1000*
This be the map to gold, me hearty! ...
```

## 8. Frameworks zoals LangChain

- Python
- Framework
  - Integratie
  - Tools
  - Plugins
  - etc.

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    base_url="http://192.168.1.21:11434",
    model="llama3.2",
    temperature=0,
)

result = llm.invoke("With which map can I find gold?")
print(result.content)
```

## 9. Vraagstukken

Wat nu verder?

- Hoe maken wij de AI slimmer?
- Hoe werkt fine-tuning en is het waard?

## 10. Overleg en speeltijd

Nu eventueel zelf spelen met LangChain en LLama.
Bewerk de `prompt.py` en `rag.py` met je favorite text editor of IDE.

Bestanden:

```bash
git clone https://github.com/robinHybrit/ai
```

- Git
- Docker (met compose)
- Connectie naar het interne network OF schrijf ruimte
- IP Dagobah `192.168.1.21:11434`
- Bevat `llama3.2`

```bash
docker compose run development
python prompt.py
```
