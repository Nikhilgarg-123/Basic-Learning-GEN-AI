# RAG Q&A Conversation (PDF + Chat History)

A small [Streamlit](https://streamlit.io/) app that implements **conversational RAG** over uploaded PDFs: you upload one or more PDFs, ask questions in natural language, and the assistant answers using retrieved chunks while **remembering the current session’s chat history** (history-aware retrieval + multi-turn QA).

Built with **LangChain** (classic chains), **Chroma** for the vector store, **Hugging Face** sentence embeddings, and **Groq** as the chat model.

## Features

- Upload **multiple PDF** files in the UI.
- **Session ID** so you can label or separate conversation threads (stored in Streamlit session state).
- **History-aware retriever**: follow-up questions are rewritten into standalone queries when needed.
- **Retrieval-augmented answers** grounded in the loaded documents (concise, up to three sentences in the current prompt).

## Prerequisites

- Python 3.10+ recommended  
- A [Groq](https://console.groq.com/) API key (entered in the app, or you can extend the app to read it from environment variables).  
- A [Hugging Face](https://huggingface.co/) token with access to the embedding model, set as `HF_TOKEN` (used for `HuggingFaceEmbeddings`).

## Setup

1. **Clone or copy** this project and open a terminal in the project folder.

2. **Create and activate a virtual environment** (example):

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment variables** — create a `.env` file in the project root (same folder as `app.py`):

   ```env
   HF_TOKEN=your_huggingface_token_here
   ```

   Do not commit real tokens; keep `.env` private.

## Run the app

```bash
streamlit run app.py
```

Then:

1. Paste your **Groq API key** when prompted.  
2. Optionally change the **Session ID**.  
3. **Upload PDF(s)** and wait for processing (text split → embeddings → Chroma).  
4. Type your **question** in the text box.

## Project layout

| Item | Role |
|------|------|
| `app.py` | Streamlit UI, PDF load/split, Chroma + RAG chain, chat history |
| `requirements.txt` | Python dependencies |
| `.env` | `HF_TOKEN` (and any keys you add later) |
| `temp.pdf` | Written at runtime when a PDF is uploaded (working file for the loader) |

## Stack (high level)

- **UI**: Streamlit  
- **LLM**: Groq — `llama-3.1-8b-instant`  
- **Embeddings**: Hugging Face — `all-MiniLM-L6-v2`  
- **Vector DB**: Chroma (in-memory for this app flow)  
- **PDF**: `PyPDFLoader` / `pypdf`  
- **Orchestration**: LangChain — `create_history_aware_retriever`, `create_retrieval_chain`, `RunnableWithMessageHistory`

## Notes

- Each run with new uploads rebuilds the vector store from the current PDF set in that session.  
- For production use, you would typically persist Chroma, tighten error handling, and avoid writing `temp.pdf` in the project root without cleanup.

## License

This is a learning project; add a license file if you redistribute the code.
