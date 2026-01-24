from src.chunking import chunk_text
from src.embeddings import embed_texts
from src.vector_store import add_to_vector_store, query_vector_store
from src.generation import generate_answer

with open("data/transcripts/lecture.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)
embeddings = embed_texts(chunks)
add_to_vector_store(chunks, embeddings)

question = "What is trial two?"
query_embedding = embed_texts([question])[0]

retrieved_chunks = query_vector_store(query_embedding)
answer = generate_answer(retrieved_chunks, question)

print("Answer:")
print(answer)
