# RAG Documents Q&A

Two Streamlit apps that answer questions from your PDFs using **RAG** (Retrieval-Augmented Generation) with LangChain, FAISS, and Groq.

---

## Projects Overview

| App | Description |
|-----|-------------|
| **Fixed Files** (`fixed_files_app.py`) | Uses PDFs from a fixed folder (`documents_folder/`). Best when your documents are already on disk. |
| **Dynamic Files** (`dynamic_files_app.py`) | Lets you upload PDFs in the UI (up to 2 files, 5MB each). No folder setup needed. |

Both apps use the same stack: **LangChain**, **FAISS** (vector store), **Ollama** (embeddings), and **Groq** (LLM).

---

## Prerequisites

- **Python 3.10+**
- **Ollama** installed and running (for embeddings with `all-minilm`)
- **Groq API key** ([get one here](https://console.groq.com/))

---

## Setup

1. **Clone or open this project**, then create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   # source venv/bin/activate   # macOS/Linux
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment variables**

   Create a `.env` file in the project root:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Optional (for LangSmith tracing):

   ```env
   LANGCHAIN_TRACING_V2=true
   LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
   LANGCHAIN_API_KEY=your_langsmith_key
   LANGCHAIN_PROJECT=learning
   ```

4. **For Fixed Files app only:** put your PDFs in a folder named `documents_folder` in the project root.

---

## Running the Apps

### Fixed Files App

Uses all PDFs in `documents_folder/`. No upload step.

```bash
streamlit run fixed_files_app.py
```

1. Click **Submit** to build the vector DB from `documents_folder/`.
2. Type your question and press Enter to get an answer.

### Dynamic Files App

Upload PDFs in the browser (max 2 files, 5MB each).

```bash
streamlit run dynamic_files_app.py
```

1. Upload one or two PDFs.
2. Click **Create Vector DB**.
3. Ask questions; answers are based only on the uploaded documents.

---

## Tech Stack

- **LangChain** – chains, loaders, text splitters
- **LangChain Groq** – LLM (e.g. `llama-3.1-8b-instant`)
- **LangChain Ollama** – embeddings (`all-minilm`)
- **FAISS** – in-memory vector store
- **Streamlit** – web UI
- **PyPDF** – PDF loading

---

## Project Structure

```
RAG Documents Q&A/
├── fixed_files_app.py      # RAG over PDFs in documents_folder/
├── dynamic_files_app.py   # RAG over uploaded PDFs
├── documents_folder/      # PDFs for fixed_files_app (you create this)
├── requirements.txt
├── .env                    # GROQ_API_KEY, optional LangSmith
└── readme.md
```

---

## Notes

- **Fixed app:** Embeddings and chunking use `chunk_size=100`, `chunk_overlap=20`. You can change these in the code for different document types.
- **Dynamic app:** Uses `chunk_size=500`, `chunk_overlap=50` and enforces a 5MB limit per file.
- Ensure **Ollama** is running and the `all-minilm` model is available (`ollama pull all-minilm` if needed).
