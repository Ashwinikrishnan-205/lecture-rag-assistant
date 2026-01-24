<h1 align="center">Lecture-Grounded Concept Clarification System</h1>

<p align="center">
<b>A Retrieval-Augmented Generation (RAG) System for Lecture-Based Question Answering</b><br>
Deep Learning–driven AI assistant that answers questions strictly from lecture audio content, preventing hallucinations.
</p>

---

## 1. Overview

The **Lecture-Grounded Concept Clarification System** is an end-to-end **Retrieval-Augmented Generation (RAG)** application designed to answer user questions **exclusively from lecture content**.

Unlike generic QA systems, this solution enforces **strict grounding**.  
If relevant information is not present in the lecture, the system explicitly refuses to answer, thereby **preventing hallucinations**.

The system processes lecture audio, converts it into text, semantically indexes the content, retrieves only the most relevant segments, and generates answers using a controlled large language model.

---

## 2. Key Features

- Lecture-grounded question answering (no external knowledge)
- Speech-to-text transcription using Whisper
- Text chunking with overlap for contextual continuity
- Semantic embedding generation using Sentence Transformers
- Vector-based similarity search with ChromaDB
- Retrieval-Augmented Generation using Llama 3.1 (Groq API)
- Explicit hallucination control with refusal responses
- One-time lecture processing with cached models
- Interactive Streamlit-based user interface
- Modular, production-oriented architecture

---

## 3. Technologies Used

| **Category** | **Details** |
|--------------|-------------|
| Speech-to-Text | OpenAI Whisper |
| Embeddings | Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database | ChromaDB |
| LLM | Llama 3.1 (8B Instant via Groq API) |
| Deep Learning | PyTorch |
| Web Interface | Streamlit |
| Programming Language | Python 3.x |

---

## 4. System Architecture

The system follows a standard **Retrieval-Augmented Generation (RAG)** pipeline:

1. Lecture audio ingestion and transcription  
2. Text chunking with overlap  
3. Embedding generation and vector indexing  
4. Semantic retrieval at query time  
5. Grounded answer generation with hallucination control  

---

## 5. Project Structure

<pre>
Lecture_RAG_Assistant/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw_lectures/
│   └── transcripts/
│
├── notebooks/
│
├── src/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── generation.py
│   ├── retrieval.py
│   ├── transcription.py
│   └── vector_store.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_generation.py
│   ├── test_transcription.py
│   └── test_vector_store.py
│
└── Model_Architecture.png
</pre>

---

## 6. Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ashwinikrishnan-205/lecture-rag-assistant.git
cd lecture-rag-assistant
```

### Step 2: Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variable
```bash
set GROQ_API_KEY=your_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

Open the browser at:  
http://localhost:8501

---

## 7. Output Behavior

- **Grounded Answers**  
  Responses are generated strictly from lecture content.

- **Hallucination Control**  
  If information is missing, the system responds:  
  *"I don't have sufficient information from the lecture."*

- **Explainability**  
  Retrieved lecture chunks are visible for transparency.

---

## 8. Use Cases

- Concept clarification from recorded lectures  
- Academic study assistance  
- Lecture revision and exam preparation  
- Demonstration of production-grade RAG systems  
- Research on hallucination mitigation in LLMs  

---

## 9. Limitations

- Performance depends on transcription accuracy  
- Very long lectures increase processing time  
- Designed for single-lecture sessions  
- Requires internet access for LLM inference  

---

## 10. Developer Information

<p align="justify">
<b>Author:</b> Ashwini Krishnan<br>
<b>Year:</b> 2026<br>
<b>Focus Areas:</b> Deep Learning · NLP · Retrieval-Augmented Generation<br>
<b>GitHub:</b> <a href="https://github.com/Ashwinikrishnan-205" target="_blank">Ashwinikrishnan-205</a>
</p>

---

## 11. License

<p align="justify">
This project is developed for educational and professional demonstration purposes.  
All rights reserved © 2026 <b>Ashwini Krishnan</b>.
</p>
