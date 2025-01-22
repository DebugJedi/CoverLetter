from langchain_groq import ChatGroq
import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import PyPDFLoader
from jobPosting import extract_jobinfo
from dotenv import load_dotenv
import yaml
from openai import OpenAI

POST = st.secrets['post_url']
class coverletter():
    def __init__(self, POST, file):
        self.file = file
        self.post = POST
        self.client = OpenAI(api_key=st.secrets["API_KEY"]) 
    

    def main(self):
        jobpost = extract_jobinfo(self.post)
        job_extract = jobpost.jobPosting()
        resume_extract = self.file
        
        return job_extract, resume_extract
    
    def letter(self, resume, page_data):

        page_data,  resume = self.main()
        
        prompt = f"""
        ## Scraped text from resume:
        {resume}

        ## INSTRUCTION:
        Scraped is the data which is a bit about my career experience and the resume.
        My name is xyz. Review the job information in {page_data}, and draft me a CoverLetter 
        exhibiting to the hiring manager that I am a good fit for this role. Do not mention my email 
        and other contact details. Never mention the names and company name.
        """

        try: 
            response  = self.client.chat.completions.create(
                model = "gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a professional cover letter generator for data scientists."},
                    {"role": "user", "content": prompt}
                ],
                temperature = 0
            )

            if response and response.choices:
                generate_response = response.choices[0].message.content

                return generate_response
            else: 
                st.error("Unexpected API response format or empty response.")
                return None

        except Exception as e:
            st.error(f"Error generating cover letter: {e}")
            return None

    def run(self):
       
        job, resume = self.main()
        generated_email = self.letter(resume, job)

        return generated_email