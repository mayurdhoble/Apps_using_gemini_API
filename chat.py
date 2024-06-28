import streamlit as st
import os
import pathlib
import textwrap

from IPython.display import display
from IPython.display import Markdown

import os
os.environ['GEMINI_API_KEY'] = ''#enter your own gemini API key


import google.generativeai as genai
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

## Function to load OpenAI model and get respones
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    
    response =chat.send_message(question,stream=True)
    return response

##initialize our streamlit app

st.set_page_config(page_title="CONVERSATIONAL BOT ")

st.header("Gemini AI LLM ")

input=st.text_input("Input: ",key="input")


submit=st.button("Answer to your question")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        print(st.write(chunk.text))
        print("_"*80)
    
    st.write(chat.history)