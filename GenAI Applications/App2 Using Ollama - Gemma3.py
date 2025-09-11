import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM


model_name =  "gemma3:4b"

# Set the page layout to wide
st.set_page_config(layout="wide")

# Langsmith Tracing
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ('system','You are an expert in answering. Answer the questions in simple to understand manner.'),
        ('user','Questions{questions}')
    ])


# Streamlit Framework
st.title("First GenAI App Using Ollama using Gemma3:4B")
question = st.text_input("Ask your question ..")

import subprocess
subprocess.run(["ollama", "pull", model_name], check=True)

# Loading the LLM Model 
llm = OllamaLLM(model = model_name)

# Output Parser
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if question:
    response = chain.invoke(question)
    st.write(response)