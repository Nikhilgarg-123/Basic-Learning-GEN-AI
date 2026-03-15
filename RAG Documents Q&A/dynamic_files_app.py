import streamlit as st
import os
import time
import tempfile

from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

model = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_template(
"""
Answer the question only from the provided context.

<context>
{context}
</context>

Question: {input}
"""
)

def create_vectors_embedding(uploaded_files):

    docs = []

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        loader = PyPDFLoader(tmp_path)
        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    final_docs = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="all-minilm")

    st.session_state.vectors = FAISS.from_documents(
        final_docs,
        embeddings
    )


st.title("📄 RAG Documents Q&A")

uploaded_files = st.file_uploader(
    "Upload PDFs (Max 2 files, 5MB each)",
    type=["pdf"],
    accept_multiple_files=True
)

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

if uploaded_files:

    if len(uploaded_files) > 2:
        st.error("❌ Maximum 2 documents allowed.")
        st.stop()

    for file in uploaded_files:
        if file.size > MAX_FILE_SIZE:
            st.error(f"❌ {file.name} exceeds 5MB limit.")
            st.stop()


if st.button("Create Vector DB"):

    if not uploaded_files:
        st.warning("⚠️ Please upload at least one document.")
    else:
        create_vectors_embedding(uploaded_files)
        st.success("✅ Vector Database Ready!")

user_prompt = st.text_input("Ask a question from the documents")


if user_prompt and "vectors" in st.session_state:

    document_chain = create_stuff_documents_chain(model, prompt)

    retriever = st.session_state.vectors.as_retriever()

    retrieval_chain = create_retrieval_chain(
        retriever,
        document_chain
    )

    start = time.process_time()

    response = retrieval_chain.invoke({
        "input": user_prompt
    })

    print("Response time:", time.process_time() - start)

    st.write("### Answer")
    st.write(response["answer"])

    with st.expander("Document Similarity Search"):

        for i, doc in enumerate(response["context"]):
            st.write(f"Document Chunk {i+1}")
            st.write(doc.page_content)
            st.write("---")