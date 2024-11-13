from langchain.document_loaders import PyMuPDFLoader
from io import BytesIO
import tempfile
from utils import TextProcessor

class DocumentReader:
    def __init__(self, uploaded_file):
        # uploaded_file is the file object directly received from Streamlit's file uploader
        self.uploaded_file = uploaded_file
        self.pdf_path = self.save_temp_pdf(self.uploaded_file)
        self.loader = PyMuPDFLoader(self.pdf_path)

    def save_temp_pdf(self, uploaded_file):
        """
        Save the uploaded file to a temporary file and return the file path.
        """
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.getvalue())  # Write the uploaded file content to temp file
            return temp_file.name

    def load_resume_text(self):
        documents = self.loader.load()
        resume_text = " ".join([doc.page_content for doc in documents])
        return resume_text

    def resume_preprocess_text(self, text: str):
        process = TextProcessor(text)
        # Call to utils.preprocess_text method (assuming it's imported in your script)
        return process.preprocess_text()

    def get_processed_resume(self):
        resume_text = self.load_resume_text()
        return self.resume_preprocess_text(resume_text)
