# LangChain Web RAG QA

This project builds a simple Retrieval-Augmented Generation (RAG) pipeline using LangChain in Python.  
It loads content from a website URL, splits the text into chunks, embeds it with OpenAI embeddings, stores it in FAISS, and then answers questions using a retrieval + document chain.

## 🧠 Overview

This repository demonstrates:

- Web document ingestion using `WebBaseLoader`
- Splitting text into chunks with `RecursiveCharacterTextSplitter`
- Creating vector embeddings using OpenAI
- Storing embeddings in FAISS vector database
- Using a retrieval chain with a document chain to answer questions

## 🚀 Features

- Web scraping + document loading
- Chunking + vector embedding
- FAISS vector search
- Retrieval + LLM generation
- Prompt customization

## 🧪 Requirements

- Python **3.10+**
- OpenAI API key
- Optional LangChain tracing configuration

## 📦 Installation

1. Create virtual environment:

```bash
python3.10 -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate


# install Dependencies 
pip install -r requirements.txt
```

you need to create a `.env` file 

```
OPENAI_API_KEY = "sk-proj-........................................................Y8aiUI3Q4PzIUQA"
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="lsv2_p----------------------------------------11"
LANGCHAIN_PROJECT="learning"
```
