import os
import subprocess
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_ollama_models():

    result = subprocess.run(
        ["ollama", "list"],
        capture_output=True,
        text=True
    )
    lines = result.stdout.strip().split("\n")
    
    models = []
    for line in lines[1:]:
        model_name = line.split()[0]
        models.append(model_name)
    
    return models if models else ["qwen2.5-coder:1.5b"]
    
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
  
prompt = ChatPromptTemplate.from_messages ([
    ("system", "You are a helpful assistant that can answer any question."),
    ("user", "Question:  {question}")

]) 

st.title("Ollama CHATGPT By NG")
available_models = get_ollama_models()
selected_model = st.selectbox("Select Ollama Model:", available_models)
question = st.text_input("Ask a question:")


if question:
    llm = Ollama(model=selected_model)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    st.write(chain.invoke({"question": question}))