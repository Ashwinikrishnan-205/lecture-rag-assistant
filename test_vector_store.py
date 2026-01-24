from src.chunking import chunk_text
from src.embeddings import embed_texts
from src.vector_store import add_to_vector_store, query_vector_store

with open("data/transcripts/lecture.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)
embeddings = embed_texts(chunks)

add_to_vector_store(chunks, embeddings)

query = "trial"
query_embedding = embed_texts([query])[0]

results = query_vector_store(query_embedding)

print("Retrieved chunk:")
print(results[0])
