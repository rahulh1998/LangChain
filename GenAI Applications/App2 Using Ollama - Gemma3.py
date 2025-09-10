import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

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

# Initializing LLM 
llm = Ollama(model = 'gemma3:4b')

# Output Parser
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if question:
    response = chain.invoke(question)
    st.write(response)


## Code to input image files
# if question:
#     # Image Input
#     uploaded_file = st.file_uploader("Upload an image...", type=['jpg', 'jpeg', 'png'])

#     if uploaded_file is not None:
#         # Process the image (This is the key change)
#         # You'll need to convert the image to a textual representation
#         # that Ollama can understand.  Here are a few options:

#         # Option 1:  Base64 Encoding (Simple, but less efficient)
#         import base64
#         image_data = uploaded_file.read()
#         image_string = base64.b64encode(image_data).decode('utf-8')

#         # Option 2:  Use a library like Pillow (PIL) to extract features
#         #  (More complex, but potentially better results)
#         # from PIL import Image
#         # image = Image.open(uploaded_file)
#         # image_string = image.summary() #or extract other features

#         # Construct the full prompt with the image data
#         full_prompt = f"Here is an image: {image_string}\nQuestion: {question}"

#         # Invoke the chain with the full prompt
#         response = chain.invoke(full_prompt)

#         # Display the response
#         st.write(response)
# else:
#     response = chain.invoke(question)
#     st.write(response)