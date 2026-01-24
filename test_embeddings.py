from src.chunking import chunk_text
from src.embeddings import embed_texts

with open("data/transcripts/lecture.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)
embeddings = embed_texts(chunks)

print("Number of chunks:", len(chunks))
print("Embedding vector length:", len(embeddings[0]))
