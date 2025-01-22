from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import yaml




myurl = st.secrets['myurl']

class my_data():
    def __init__(self, url = myurl ):
        self.llm = ChatGroq(
                model_name= "llama-3.1-70b-versatile",
                temperature=0,
                groq_api_key=st.secrets["groq_api_key"]  
                )
        self.my_url = url

    def load_data(self): 
        loader = WebBaseLoader(self.my_url)
        my_data = loader.load().pop().page_content

        return my_data
    