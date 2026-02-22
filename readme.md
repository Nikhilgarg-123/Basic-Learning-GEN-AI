# Basic OllamaChatGpt

A simple Streamlit-based ChatGPT-style web app that uses locally installed Ollama models via LangChain.

This project allows users to:
- Select any installed Ollama model from a dropdown
- Ask questions through a clean Streamlit UI
- Get responses from the selected local LLM

---

## 🚀 Features

- Dynamic Ollama model dropdown (`ollama list`)
- Streamlit web interface
- LangChain prompt chaining
- Local LLM execution (no OpenAI required)
- Environment variable support with `.env`

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- dotenv

---

## 📦 Requirements

Make sure you have:

- Python 3.9+
- Ollama installed → https://ollama.com
- At least one Ollama model pulled (example: `ollama pull qwen2.5-coder:1.5b`)

---

## 🔧 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Nikhilgarg-123/Basic-Learning-GEN-AI.git
cd "Basic OllamaChatGPT"
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a requirements file yet:

```bash
pip install streamlit langchain langchain-community python-dotenv
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="your_key_here"
LANGCHAIN_PROJECT="learning"

```

Note: Ollama runs locally, so OpenAI API keys are NOT required.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in your terminal (usually http://localhost:8501).

---

## 🧠 How It Works

1. The app fetches available models using:

```
ollama list
```

2. Models are shown in a Streamlit dropdown.
3. User selects a model.
4. Question is passed through a LangChain prompt.
5. Response is generated using the selected Ollama model.

---

## 📂 Project Structure

```
Basic OllamaChatGpt/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

- Streaming responses
- Chat history memory
- Temperature slider
- Model size display in dropdown
- Conversation export
- Multi-turn chat UI

---

## 🛑 Troubleshooting

### Ollama not found?
Make sure Ollama is installed and running:

```bash
ollama --version
```

### No models in dropdown?
Pull a model first:

```bash
ollama pull llama3
```

---

## 📜 License

This project is open-source and free to use.

---

## 🙌 Author

Created as a basic local ChatGPT alternative using Ollama and Streamlit.

---

⭐ If you like this project, consider starring the repository!