# Cover Letter Generator

Welcome to the **Cover Letter Generator**! This tool uses natural language processing (NLP) to automatically create a professional, personalized cover letter from a provided job description and resume. The application is built with **Streamlit** for a simple, interactive user experience.

## Features
- Automatically generates cover letters based on job descriptions and resumes.
- Option to download the generated cover letter in DOCX.
- **Dynamic Mode**: Scrapes job descriptions from dynamic web pages.
- **Static Mode**: Processes job descriptions from static web pages.
- Deployed version with support for **static web pages**.

![Cover Letter Generator - Screenshot 1](path/to/screenshot1.png)
![Cover Letter Generator - Screenshot 2](path/to/screenshot2.png)

## Deployed Version (Static Mode)
Try out the app (Static Web Pages Only) here: [Cover Letter Generator](https://cover-letter-generator-1155.streamlit.app/)

> **Note**: The deployed version only supports **static web pages** due to resource limitations. For use with dynamic web pages, please follow the instructions below to run the app locally.

---

## Installation Guide

### Prerequisites
- Python 3.8+
- Streamlit
- Selenium (for dynamic page scraping)
- Other dependencies listed in `requirements.txt`

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/cover-letter-generator.git
   cd cover-letter-generator
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: `env\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   - Create a `.streamlit/secrets.toml` file in the project root to store your API key.
   - Add your API key in the file:
     ```toml
     GROQ_API_KEY = "your_api_key_here"
     ```

5. **Set Up ChromeDriver (For Dynamic Mode)**
   - Download the ChromeDriver executable that matches your Chrome version from [here](https://sites.google.com/chromium.org/driver/).
   - Add ChromeDriver to your PATH, or specify its path in the code if needed.

---

## Run the Application

1. **Switch between Static and Dynamic Mode**
   - In the `streamlit_app.py` file, set the `LOADER_TYPE` variable to either `"static"` or `"dynamic"`:
     ```python
     LOADER_TYPE = "static"  # Change to "dynamic" if scraping dynamic web pages
     ```

2. **Run the App Locally**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access the App**
   - The app will start on `http://localhost:8501`. Open this URL in your browser to use the app.

---

## Usage Instructions

1. **Enter Job Link**: Paste the job listing URL into the designated field. (Static web pages only for deployed version.)
2. **Upload Your Resume**: Upload a PDF version of your resume.
3. **Generate Cover Letter**: Click "Generate" to create a cover letter.
4. **Download the Cover Letter**: Use the download buttons to save your cover letter as a DOCX.

---

## Screenshots

Here's a preview of the application in action:

![Cover Letter Generator - Enter Job Link](path/to/screenshot3.png)
![Cover Letter Generator - Upload Resume](path/to/screenshot4.png)
![Cover Letter Generator - Generated Cover Letter](path/to/screenshot5.png)

---

## Notes and Limitations
- **Token Limit**: The app has a limit of 6000 tokens per minute, which may affect longer cover letters.
- **Static vs. Dynamic Mode**: Dynamic mode uses Selenium to load dynamic content from web pages. To use dynamic mode, be sure to install ChromeDriver and select `LOADER_TYPE = "dynamic"`.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using the Cover Letter Generator!
