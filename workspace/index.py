from langchain_ollama import ChatOllama

llm = ChatOllama(
    base_url="http://localhost:11434",
    model="llama3.2",
    temperature=0,
)

messages = [
    (
        "system",
        "You are a pirate and you are helping finding treasures in the ocean.",
    ),
    ("human", "What is the right side of a ship called?"),
]

result = llm.invoke(messages)
print(result.content)
