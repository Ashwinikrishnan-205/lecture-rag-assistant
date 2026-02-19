import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()  # <-- add this line

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

import yaml
from src.logger import logger

with open("config.yaml", "r") as f:
    CFG = yaml.safe_load(f)

def generate_answer(context_chunks, question):
    if not context_chunks:
        logger.warning("No context chunks retrieved for query.")
        return "I don't have sufficient information from the lecture."

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

    try:
        response = client.chat.completions.create(
            model=CFG["model_name"],
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"LLM call failed: {e}")
        return "An internal error occurred while generating the answer."
