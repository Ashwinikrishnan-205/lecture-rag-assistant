<h1 align="center">Lecture-Grounded Concept Clarification System</h1>

<p align="center">
<b>A Retrieval-Augmented Generation (RAG) System for Lecture-Based Question Answering</b><br>
An AI assistant that answers questions strictly from lecture audio using a retrieval-augmented pipeline with large language models, reducing hallucinations.
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
- Modular, production-style architecture

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

Configuration parameters such as chunk size and retrieval settings can be adjusted via a configuration file, while secrets are managed using environment variables.

---

## 4. System Architecture

The system follows a standard **Retrieval-Augmented Generation (RAG)** pipeline:

1. Lecture audio ingestion and transcription  
2. Text chunking with overlap  
3. Embedding generation and vector indexing  
4. Semantic retrieval at query time  
5. Grounded answer generation with hallucination control  

---

## 5.Evaluation

The system was manually evaluated using 20 lecture-grounded questions derived from the lecture transcript.

- Top-3 retrieval frequently surfaced relevant context for answerable questions during manual evaluation.
- Manual review confirmed grounded responses when information was present.
- The system correctly refused to answer questions not supported by the lecture content, demonstrating hallucination control.

This evaluation focuses on qualitative grounding and retrieval coverage rather than benchmark accuracy.

---

## 6. Project Structure

<pre>
Lecture_RAG_Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── config.yaml
├── app.log
├── Model_Architecture.png
│
├── data/
│   ├── raw_lectures/
│   └── transcripts/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── generation.py
│   ├── retrieval.py
│   ├── transcription.py
│   ├── vector_store.py
│   ├── logger.py
│   └── langchain_pipeline.py
│
├── tests/
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_generation.py
│   ├── test_transcription.py
│   └── test_vector_store.py
</pre>

---

## 7. Installation and Setup

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

### Step 4: Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
GROQ_API_KEY=your_api_key_here
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

Open the browser at:  
http://localhost:8501

---

## 8. Output Behavior

- **Grounded Answers**  
  Responses are generated strictly from lecture content.

- **Hallucination Control**  
  If information is missing, the system responds:  
  *"I don't have sufficient information from the lecture."*

- **Explainability**  
  Retrieved lecture chunks are visible for transparency.

---

## 9. Use Cases

- Concept clarification from recorded lectures  
- Academic study assistance  
- Lecture revision and exam preparation  
- Demonstration of production-grade RAG systems  
- Research on hallucination mitigation in LLMs  

---

## 10. Limitations

- Performance depends on transcription accuracy  
- Very long lectures increase processing time  
- Designed for single-lecture sessions  
- Requires internet access for LLM inference  

---

## 11.Performance Notes

- Initial lecture indexing time depends on audio length and runs on CPU.
- Query latency varies based on model inference time and network conditions.
- Suitable for offline lecture processing and interactive querying for small to medium lecture lengths.


## 12. Developer Information

<p align="justify">
<b>Author:</b> Ashwini Krishnan<br>
<b>Year:</b> 2026<br>
<b>Focus Areas:</b> Deep Learning · NLP · Retrieval-Augmented Generation<br>
<b>GitHub:</b> <a href="https://github.com/Ashwinikrishnan-205" target="_blank">Ashwinikrishnan-205</a>
</p>

---

## 13. License

<p align="justify">
This project is developed for educational and professional demonstration purposes.  
All rights reserved © 2026 <b>Ashwini Krishnan</b>.
</p>
