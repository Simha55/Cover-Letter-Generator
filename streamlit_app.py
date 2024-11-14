import streamlit as st
from io import BytesIO
from docx import Document
from docx.shared import Inches
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from scraper import JobDescriptionScraper
from document_reader import DocumentReader
from model import Model
from dotenv import load_dotenv
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from langchain_community.document_loaders import WebBaseLoader
from datetime import datetime
from utils import TextProcessor
from docx2pdf import convert
import os

LOADER_TYPE = "static"

# Get today's date in the desired format: "November 13th, 2024"
today = datetime.today()
formatted_date = today.strftime("%B %d, %Y")

# Add the suffix to the day
day_suffix = lambda day: "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
day_with_suffix = f"{today.day}{day_suffix(today.day)}"

# Combine the formatted date with the suffix
formatted_date_with_suffix = formatted_date.replace(f"{today.day}", day_with_suffix)

# Load environment variables
load_dotenv()

st.title("Cover Letter Generator")
# Caution Message
st.warning("""
**⚠️ Caution: Use at Your Own Discretion**

Please note that usage of this tool is at your own discretion. While every effort has been made to ensure its functionality, we recommend exercising caution and verifying outputs before making decisions based on the results.
""")

# Announcement about Chrome Extension
st.markdown("""
**🚀 Upcoming Chrome Extension Launch!**

We are excited to announce that our Chrome extension will be launching soon, making it even easier to use this tool directly in your browser. Stay tuned for updates!
""")

# Token Limit Information
st.info("""
**⏳ Limitations**

Please note that this application has a **6000 tokens per minute** limit in Streamlit. This functionality is only available for static webpages. For use with dynamic webpages, **[clone the GitHub repository](https://github.com/Simha55/Cover-Letter-Generator)** and follow the provided instructions. Be mindful of this limitation to ensure uninterrupted usage.
""")


# Input for the job link
job_link = st.text_input("Enter the Job Link")

# Check if the resume is already uploaded or saved in session state
if 'resume_file' not in st.session_state:
    st.session_state.resume_file = None

# Input for uploading resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# If a file is uploaded, store it in session state
if uploaded_file is not None:
    st.session_state.resume_file = uploaded_file

# Handle the "Generate" button click
if st.button("Generate"):
    # Ensure both job link and resume are provided
    if job_link and st.session_state.resume_file:
        # Process the uploaded resume using the DocumentReader
        document_reader = DocumentReader(st.session_state.resume_file)
        resume_text = document_reader.get_processed_resume()  # Get the preprocessed resume text

        # Create a JobDescriptionScraper instance and scrape the job description (for Dynamic Webpages)
        if LOADER_TYPE == 'dynamic':
            job_desc_scraper = JobDescriptionScraper(job_link)
            job_description = job_desc_scraper.scrape_job_description()
            job_description = "Date: " + formatted_date_with_suffix + job_description

        # For Static webpages
        else:
            loader = WebBaseLoader([job_link])
            job_description = loader.load().pop().page_content
            preprocessor = TextProcessor(job_description)
            job_description = preprocessor.preprocess_text()
            job_description = "Date: " + formatted_date_with_suffix + job_description

        # Display the job description if it was successfully scraped
        if job_description:
            llm_object = Model(st.secrets["GROQ_API_KEY"])
            job_description_json = llm_object.extract_job_description(job_description)
            cover_letter = llm_object.generate_cover_letter(job_description_json.content, resume_text)

            st.subheader("Cover Letter:")

            # Store the cover letter in session state to persist across re-runs
            if 'cover_letter_text' not in st.session_state:
                st.session_state.cover_letter_text = cover_letter.content

            # Show the cover letter in an editable text box
            cover_letter_text = st.text_area("Edit your Cover Letter:", st.session_state.cover_letter_text, height=300)

            # Update session state if the user edits the text area
            st.session_state.cover_letter_text = cover_letter_text
            # Provide options to download as DOC or PDF without the need for st.button()
            def create_docx(cover_letter_text):
                doc = Document()
                sections = doc.sections
                for section in sections:
                    section.top_margin = Inches(1)
                    section.bottom_margin = Inches(1)
                    section.left_margin = Inches(1)
                    section.right_margin = Inches(1)
                doc.add_paragraph(cover_letter_text)
                byte_io = BytesIO()
                doc.save(byte_io)
                byte_io.seek(0)
                return byte_io

            # Provide download buttons for DOCX and PDF directly
            docx_file = create_docx(cover_letter_text)
            st.download_button("Download DOCX", docx_file, file_name="cover_letter.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

        else:
            st.error("Could not extract job description. Please check the job link.")
    elif not job_link:
        st.warning("Please enter a job link.")
    elif not st.session_state.resume_file:
        st.warning("Please upload your resume.")
