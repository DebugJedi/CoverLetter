import streamlit as st
from CoverLetter import coverletter
from PIL import Image
import streamlit_shadcn_ui as ui
from resume_extract import extract_resume

st.set_page_config(
        page_title= "Cover Letter",
        page_icon= "✉️",
        layout="wide"
    )

col1, col2, col3 = st.columns([1,2,1], gap= 'small', vertical_alignment='center')

# Image to display
img = Image.open('app/resources/photos/Email-Generator.jpg')
# st.image(img, width= 500)
with col1:
     pass
with col2:
    st.image(img, width= 500)
with col3:
     pass
with open("assets/style.css") as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# Title
st.markdown(" ### Cover Letter ✉️")

doc_file = st.file_uploader("Resume/CV (PDF)",
                            type=["pdf"])

jobPosting = st.text_input("Enter a job URL:", value = "https://careers.airbnb.com/positions/6356217/" )
try:
    if st.button("submit"):
        
        with st.spinner("wait for it...."):
            extractor_func = extract_resume()
            st.spinner(text="uploading...")
            document = extractor_func.load(doc_file)
            # st.write(document)
            cl = coverletter(jobPosting, document)
            generated_email = cl.run()
            st.write("<span class = 'ai generated_email'>{}</span>".format(generated_email), unsafe_allow_html=True)
except AttributeError as e:
     st.write(f"Please upload a file...{e}")
except Exception as e:
     st.write(f"An error occured: {e}")
     




    
    



