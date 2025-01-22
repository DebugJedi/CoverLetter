# from langchain_groq import ChatGroq
import streamlit as st
# from langchain_community.document_loaders import PyPDFLoader
import yaml
from PyPDF2 import PdfReader


resume_file  = st.secrets['resume']

class extract_resume():
        # https://boards.greenhouse.io/benchling/jobs/6270990
        def __init__(self):
                # self.llm = ChatGroq(
                #         model_name= "llama-3.1-70b-versatile",
                #         temperature=0,
                #         groq_api_key=st.secrets["groq_api_key"]  
                # )
                return None
                
        def load(self, file):

                pdfreader = PdfReader(file)
                count = len(pdfreader.pages)
                all_page_text = ""
                for i in range(count):
                        page = pdfreader.pages[i]
                        all_page_text +=page.extract_text()
                
                return all_page_text
        
        

