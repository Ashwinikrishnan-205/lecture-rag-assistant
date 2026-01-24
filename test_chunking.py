from src.chunking import chunk_text

with open("data/transcripts/lecture.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = chunk_text(text)

print("Total chunks:", len(chunks))
print("\nFirst chunk:\n")
print(chunks[0][:500])
