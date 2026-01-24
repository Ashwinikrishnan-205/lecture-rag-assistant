from src.transcription import transcribe

text = transcribe(
    "data/raw_lectures/lecture.mp3",
    "data/transcripts/lecture.txt"
)

print(text[:500])
