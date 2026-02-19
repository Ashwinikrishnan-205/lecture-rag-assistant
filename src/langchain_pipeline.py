from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_community.chat_models import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def langchain_rag_answer(chunks, question):
    # Build in-memory vector store (demo purpose)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_texts(chunks, embedding=embeddings)

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    prompt = PromptTemplate.from_template("""
You are a lecture-grounded AI assistant.

Answer ONLY from the provided context.
If not present, reply:
"I don't have sufficient information from the lecture."

Context:
{context}

Question:
{question}
""")

    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.getenv("GROQ_API_KEY"))

    chain = RunnableSequence(
        {
            "context": retriever,
            "question": lambda x: x
        }
        | prompt
        | llm
    )

    result = chain.invoke(question)
    return result.content.strip()