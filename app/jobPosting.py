from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
import streamlit as st
from dotenv import load_dotenv
import yaml


class extract_jobinfo():

    def __init__(self, job_url):
        self.job_url = job_url
        self.llm = ChatGroq(
                        model_name= "llama-3.1-70b-versatile",
                        temperature=0,
                        groq_api_key=st.secrets["groq_api_key"]  
                )
   
    def jobPosting(self):
        loader = WebBaseLoader(self.job_url)
        page_data = loader.load().pop().page_content
        # print(page_data)

        prompt_extract = PromptTemplate.from_template(
            """
            ## Scrapped text from Website:
            {page_data}
            ## INSTRUCTION:
            The scraped text is from the career's page of a website.
            You job is to extract the job postions and return them in JSON format containg
            following keys: 'role', 'experience', 'skills' and 'description'.
            only return the valid JSON.
            ## VAILD JSON (NO PREAMBLE):

        """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data': page_data})
        Json_parser = JsonOutputParser()
        json_res = Json_parser.parse(res.content)
        return json_res
