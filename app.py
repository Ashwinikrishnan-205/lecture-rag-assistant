import streamlit as st
import os
from dotenv import load_dotenv
from src.logger import logger
from dotenv import load_dotenv

load_dotenv()

from src.transcription import transcribe
from src.chunking import chunk_text
from src.embeddings import embed_texts
from src.vector_store import add_to_vector_store, query_vector_store
from src.generation import generate_answer

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Lecture-Grounded RAG Assistant",
    layout="centered"
)

# ---------------- Reset Button ----------------
if st.button("🔄 Reset Lecture Session"):
    st.session_state.clear()
    st.rerun()

# ---- Professional Title Section ----
st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <h1 style="text-align: center; margin-bottom: 6px;">
        Lecture-Grounded Concept Clarification System
    </h1>
    <p style="text-align: center; font-size: 20px; color: #e6e6e6; margin-top: 4px;">
        A retrieval-augmented AI system for answering questions strictly from lecture content
    </p>
    """,
    unsafe_allow_html=True
)

# ---------------- Session State ----------------
if "lecture_processed" not in st.session_state:
    st.session_state.lecture_processed = False

if "vector_ready" not in st.session_state:
    st.session_state.vector_ready = False

if "qa_history" not in st.session_state:
    st.session_state.qa_history = []

if "audio_path" not in st.session_state:
    st.session_state.audio_path = None

if "chunks_count" not in st.session_state:
    st.session_state.chunks_count = 0

# ---------------- Upload Section ----------------
uploaded_file = st.file_uploader(
    "Upload lecture audio (mp3 / wav / m4a)",
    type=["mp3", "wav", "m4a"]
)

# ---------------- Audio Preview ----------------
if uploaded_file is not None:
    st.markdown("### 🎧 Source Lecture Audio")
    st.audio(uploaded_file)

# ---------------- Lecture Processing (RUN ONCE) ----------------
if uploaded_file and not st.session_state.vector_ready:
    os.makedirs("data/raw_lectures", exist_ok=True)
    os.makedirs("data/transcripts", exist_ok=True)

    audio_path = f"data/raw_lectures/{uploaded_file.name}"

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Processing lecture (one-time)..."):
        try:
           transcript_path = "data/transcripts/lecture.txt"

           if os.path.exists(transcript_path):
               with open(transcript_path, "r", encoding="utf-8") as f:
                  transcript = f.read()
           else:
               transcript = transcribe(audio_path, transcript_path)

           chunks = chunk_text(transcript)
           embeddings = embed_texts(chunks)
           add_to_vector_store(chunks, embeddings)

        except Exception as e:
            logger.error(f"Lecture processing failed: {e}")
            st.error("Failed to process lecture. Please try another file.")
            st.stop()


    # with st.spinner("Processing lecture (one-time)..."):
    #    transcript_path = "data/transcripts/lecture.txt"
       
    #    if os.path.exists(transcript_path):
    #        with open(transcript_path, "r", encoding="utf-8") as f:
    #           transcript = f.read()
    #    else:
    #        transcript = transcribe(audio_path, transcript_path)

    #    chunks = chunk_text(transcript)
    #    embeddings = embed_texts(chunks)
    #    add_to_vector_store(chunks, embeddings)


    # Store safe values in session_state
    st.session_state.audio_path = audio_path
    st.session_state.chunks_count = len(chunks)
    st.session_state.vector_ready = True
    st.session_state.lecture_processed = True

    st.success("Lecture processed successfully.")

# ---------------- Lecture Metadata (SAFE) ----------------
if st.session_state.lecture_processed:
    st.subheader("📄 Lecture Processing Summary")

    st.write(f"**Total Chunks Created:** {st.session_state.chunks_count}")
    st.write("**Embedding Status:** Successfully indexed in vector database")

# ---------------- Question Section ----------------
st.divider()

if not st.session_state.vector_ready:
    st.info("Please upload and process a lecture to begin.")
else:
    with st.form("question_form", clear_on_submit=True):
        question = st.text_input("Ask a question from the lecture")
        submitted = st.form_submit_button("Ask")

        if submitted and question.strip():
            with st.spinner("Thinking..."):
                try:
                   query_embedding = embed_texts([question])[0]
                   retrieved_chunks = query_vector_store(query_embedding)
                   answer = generate_answer(retrieved_chunks, question)

                   st.session_state.qa_history.append({
                       "question": question,
                       "answer": answer,
                       "context": retrieved_chunks
                   })

                except Exception as e:
                    logger.error(f"QA failed: {e}")
                    st.error("Something went wrong while answering. Please try again.")
                    st.stop()


        # if submitted and question.strip():
        #     with st.spinner("Thinking..."):
        #        query_embedding = embed_texts([question])[0]
        #        retrieved_chunks = query_vector_store(query_embedding)
        #        answer = generate_answer(retrieved_chunks, question)


        #     st.session_state.qa_history.append({
        #         "question": question,
        #         "answer": answer,
        #         "context": retrieved_chunks
        #     })

# ---------------- Display Q&A History ----------------
for item in reversed(st.session_state.qa_history):
    with st.container():
        st.markdown("### ❓ Question")
        st.write(item["question"])

        st.markdown("### ✅ Answer")
        st.write(item["answer"])

        if "don't have sufficient information" in item["answer"].lower():
            st.warning("The lecture does not contain enough information for this question.")
        else:
            st.success("Answer generated strictly from lecture content.")

        with st.expander("View retrieved lecture context"):
            for i, chunk in enumerate(item["context"], 1):
                st.markdown(f"**Chunk {i}:**")
                st.write(chunk)

        st.divider()