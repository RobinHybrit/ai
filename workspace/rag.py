from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_redis import RedisConfig, RedisVectorStore

url = "http://192.168.1.21:11434"
model = "llama3.2"


# Setup of Vector store
config = RedisConfig(
    index_name="index",
    redis_url="redis://localhost:6379",
)

embeddings = OllamaEmbeddings(
    base_url=url,
    model=model
)
vector_store = RedisVectorStore(embeddings, config=config)

# Adding text to the vector store
texts = ['Map\n\n - number: 1000\n title: A map to gold\n directions: At the first tree turn left']
vector_store.add_texts(texts)

# Query vector store
query = "Which map will find me gold?"
results = vector_store.similarity_search(query)

documents = ''
print("Simple Similarity Search Results:")
for doc in results:
    print(f"Content: {doc.page_content}")
    documents += doc.page_content + '\n'

# Using the result in a query
llm = ChatOllama(
    base_url=url,
    model=model,
    temperature=0,
)

messages = [
    (
        "system",
        f"""
        You're a pirate that helps with finding treasure from maps.

        Maps: {documents}
        """,
    ),
    ("human", query),
]

print("===")
result = llm.invoke(messages)
print(result.content)
