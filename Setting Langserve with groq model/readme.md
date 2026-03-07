
# Langserve Translator with Groq and Llama 3.1

A lightweight FastAPI application that leverages **LangServe** to deploy a **LangChain** translation chain. It uses the **Groq** inference engine running **Llama 3.1 8b** for near-instantaneous language processing.

## 🚀 Features
* **FastAPI Integration**: High-performance web framework for building APIs.
* **LangServe**: Simplifies the deployment of LangChain Runnables and Chains.
* **Groq Cloud**: Utilizes Llama-3.1-8b-instant for rapid LLM responses.
* **Clean Architecture**: Uses LCEL (LangChain Expression Language) for chaining prompts, models, and parsers.

## 🛠️ Prerequisites
- Python 3.8+
- A Groq API Key (Get one at [console.groq.com](https://console.groq.com/))

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Nikhilgarg-123/Basic-Learning-GEN-AI.git
   cd "Setting Langserve with groq model"
   ```

2. Install dependencies:
   ```
pip install fastapi langchain-core langchain-groq langserve uvicorn python-dotenv
   ```
or
```
pip install -r requirements.txt
```
   
