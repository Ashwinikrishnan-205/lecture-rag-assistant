import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(context_chunks, question):
    context = "\n\n".join(context_chunks)

    prompt = f"""
You are a lecture-grounded AI assistant.

Answer the question using ONLY the lecture context below.
If the answer is not present, say:
"I don't have sufficient information from the lecture."

Lecture Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()
