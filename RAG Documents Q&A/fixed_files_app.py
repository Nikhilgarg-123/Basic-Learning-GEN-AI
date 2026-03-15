import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

model = ChatGroq(groq_api_key=groq_api_key, model="llama-3.1-8b-instant")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the following Questions based on provided context only.
    Please Provide the most accurate answer based on the question
    <context>
    {context}
    </context>
    Question: {input}
    """
)

def create_vectors_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = OllamaEmbeddings(model="all-minilm") # use llama2, qwen3-embedding:4b for better accuracy
        st.session_state.loader = PyPDFDirectoryLoader("documents_folder/")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20)
        st.session_state.final_docs = st.session_state.text_splitter.split_documents(st.session_state.docs[:1])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_docs, st.session_state.embeddings)
        


# Title
st.title("RAG Documents Q&A")
user_prompt = st.text_input("Enter your question from the documents")

if st.button("Submit"):
    create_vectors_embedding()
    st.write("Vector Db is Ready")

if user_prompt:
    document_chain = create_stuff_documents_chain(model, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    start = time.process_time()
    response = retrieval_chain.invoke({"input": user_prompt})
    print(time.process_time() - start)

    st.write(response["answer"])
    
    with st.expander("Document Similarity Search"):
        for i,doc in enumerate(response["context"]):
            st.write(f"Document {i}: {doc.metadata['title']}")
            st.write(doc.page_content)
            st.write("---")