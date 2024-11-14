# Cover-Letter-Generator
Welcome to the Cover Letter Generator! This tool uses natural language processing (NLP) to automatically create a professional, personalized cover letter from a provided job description and resume. The application is built with Streamlit for a simple, interactive user experience.

Features
Automatically generates cover letters based on job descriptions and resumes.
Option to download the generated cover letter in DOCX or PDF format.
Dynamic Mode: Scrapes job descriptions from dynamic web pages.
Static Mode: Processes job descriptions from static web pages.
Deployed version with support for static web pages.

Deployed Version (Static Mode)
Try out the app (Static Web Pages Only) here: Cover Letter Generator

Note: The deployed version only supports static web pages due to resource limitations. For use with dynamic web pages, please follow the instructions below to run the app locally.

Installation Guide
Prerequisites
Python 3.8+
Streamlit
ChromeDriver (for dynamic page scraping)
Other dependencies listed in requirements.txt
Setup Instructions
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/cover-letter-generator.git
cd cover-letter-generator
Create a Virtual Environment

bash
Copy code
python -m venv env
source env/bin/activate  # On Windows: `env\Scripts\activate`
Install Required Packages

bash
Copy code
pip install -r requirements.txt
Configure API Key

Create a .streamlit/secrets.toml file in the project root to store your API key.
Add your API key in the file:
toml
Copy code
GROQ_API_KEY = "your_api_key_here"
Set Up ChromeDriver (For Dynamic Mode)

Download the ChromeDriver executable that matches your Chrome version from here.
Add ChromeDriver to your PATH, or specify its path in the code if needed.
Run the Application
Switch between Static and Dynamic Mode

In the streamlit_app.py file, set the LOADER_TYPE variable to either "static" or "dynamic":
python
Copy code
LOADER_TYPE = "static"  # Change to "dynamic" if scraping dynamic web pages
Run the App Locally

bash
Copy code
streamlit run streamlit_app.py
Access the App

The app will start on http://localhost:8501. Open this URL in your browser to use the app.
Usage Instructions
Enter Job Link: Paste the job listing URL into the designated field. (Static web pages only for deployed version.)
Upload Your Resume: Upload a PDF version of your resume.
Generate Cover Letter: Click "Generate" to create a cover letter.
Download the Cover Letter: Use the download buttons to save your cover letter as a DOCX or PDF.
Screenshots
Here's a preview of the application in action:


Notes and Limitations
Token Limit: The app has a limit of 6000 tokens per minute, which may affect longer cover letters.
Static vs. Dynamic Mode: Dynamic mode uses Selenium to load dynamic content from web pages. To use dynamic mode, be sure to install ChromeDriver and select LOADER_TYPE = "dynamic".
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Thank you for using the Cover Letter Generator!
