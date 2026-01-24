import chromadb
import streamlit as st

@st.cache_resource
def get_collection():
    client = chromadb.Client()
    return client.get_or_create_collection(name="lecture_chunks")

def add_to_vector_store(chunks, embeddings):
    collection = get_collection()
    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[embedding.tolist()],
            ids=[str(i)]
        )

def query_vector_store(query_embedding, k=2):
    collection = get_collection()
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=k
    )
    return results["documents"][0]
