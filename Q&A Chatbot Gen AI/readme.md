# Q&A Chatbot Gen AI 🤖

A versatile Generative AI chatbot built with **Streamlit** and **LangChain**. This application allows users to toggle between **OpenAI's** cloud-based models and **Ollama's** local models, providing a flexible playground for testing different Large Language Models (LLMs).

## 🚀 Features

* **Dual Provider Support:** Seamlessly switch between OpenAI (GPT-3.5/GPT-4) and local Ollama models (Gemma/Llama).
* **Dynamic Configuration:** Adjust temperature, max tokens, and specific models directly from the sidebar.
* **Observability:** Integrated with **LangSmith** for real-time tracing and monitoring of LLM chains.
* **Streamlined UI:** A clean, intuitive interface powered by Streamlit.

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Orchestration:** LangChain
* **LLM Providers:** OpenAI API & Ollama (Local)
* **Tracing:** LangSmith

---

## 📋 Prerequisites

1. **Python 3.10+**
2. **Ollama** installed and running (for local models).
   - `ollama pull gemma3`
   - `ollama pull llama3`
3. **OpenAI API Key** (for GPT models).

---

## ⚙️ Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**  
   Create a `.env` file in the root directory:

   ```env
   LANGCHAIN_API_KEY=your_langsmith_key_here
   LANGCHAIN_PROJECT=your_project_name
   LANGCHAIN_TRACING_V2=true
   ```

---

## 🚀 Running the App

1. Start the Streamlit server:

   ```bash
   streamlit run app.py
   ```

2. Open the URL provided (usually http://localhost:8501).
3. Select your provider (OpenAI or Ollama) in the sidebar.
4. Enter your API key (if using OpenAI) and adjust parameters.
5. Type your question and get instant responses!

---

## 📁 Project Structure

* **app.py** — Main application logic and UI.
* **.env** — Environment variables for LangSmith tracking.
* **requirements.txt** — List of necessary Python packages.