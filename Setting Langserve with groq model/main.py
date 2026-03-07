from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")

model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)


generic_template = "Translate the following to {language}:"

prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("user", "{text}")
])
 
parser = StrOutputParser()

chain = prompt | model | parser

app = FastAPI(title="Langserve with Groq Model by NG", version="0.1.0", description="This is a Langserve app with Groq model")
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)