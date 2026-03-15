import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate 

import os 
from dotenv import load_dotenv
load_dotenv()

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the user's question."),
    ("user", "Question:{question}")
])


def genrate_response_openai(question, api_key, llm, temperaure, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(model_name=llm, api_key=api_key, temperature=temperaure, max_tokens=max_tokens)
    OutputParser = StrOutputParser()
    chain = prompt | llm | OutputParser
    answer = chain.invoke({"question": question})
    return answer


def genrate_response_ollama(question, llm):
    llm = Ollama(model=llm)
    OutputParser = StrOutputParser()
    chain = prompt | llm | OutputParser
    answer = chain.invoke({"question": question})
    return answer

# Title of the application
st.title("Q&A Chatbot Gen AI")

# Create a sidebar
st.sidebar.title("Settings")

# Create a select box to select the company
company = st.sidebar.selectbox("Openai/Ollama", ["Openai","Ollama"])

if company=="Openai":
    api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    llm = st.sidebar.selectbox("Model", ["gpt-3.5-turbo", "gpt-4"])
    temperaure = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
    max_tokens = st.sidebar.slider("Max Tokens", min_value=1, max_value=1000, value=100)

elif company=="Ollama":
    llm = st.sidebar.selectbox("Model", ["gemma3:latest", "llama3:latest"])

st.write("Welcome to the Q&A Chatbot Gen AI!")
question = st.text_input("Your question:")

if question:
    if company=="Openai":
        answer = genrate_response_openai(question, api_key, llm, temperaure, max_tokens)
        st.write(answer)

    elif company=="Ollama":
        answer = genrate_response_ollama(question, llm)
        st.write(answer)
    
else:
    st.write("Please enter a question.")