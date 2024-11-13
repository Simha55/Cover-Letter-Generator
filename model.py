from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

class JobDescriptionExtractor:
    def __init__(self):
        self.prompt = PromptTemplate.from_template("""
            ### Instruction:
            Extract the following fields from the job application data and format as JSON:
            - **"company"**: The name of the company.
            - **"job title"**: The job title or position.
            - **"skills"**: Required or preferred skills.
            - **"experience"**: Years or types of experience needed.
            - **"description"**: Main job responsibilities or description.
            - **"date"**: Today's date.

            Respond in valid JSON format with no additional commentary or preamble. If multiple jobs are listed, format each entry with a unique identifier.

            ### Scraped job application data:
            {page_data}
        """)

    def extract_job_description(self, page_data: str, llm):
        chain_extract = self.prompt | llm
        return chain_extract.invoke(input={'page_data': page_data})


class Model:
    def __init__(self, api_key: str):
        self.llm_description_extractor = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.5,
            max_retries=2,
            groq_api_key=api_key
        )
        self.llm_cover_letter_generator = ChatGroq(
            model="llama-3.1-70b-versatile",
            temperature=0.5,
            max_retries=2,
            groq_api_key=api_key
        )
        self.job_description_extractor = JobDescriptionExtractor()

    def generate_cover_letter(self, job_description_json: str, resume_text: str):
        prompt_letter = PromptTemplate.from_template("""
        ### Instruction:
        Write a concise and professional cover letter based on the following information:
        - The job description (provided in JSON format below) describes the role and required skills for the position.
        - The resume text provides information about the applicant’s actual experiences, skills, and projects.
        
        Your cover letter should:
        - Be realistic, based only on the content from the job description and resume.
        - Focus on the applicant’s relevant skills, experiences, and projects that align with the job role and description.
        - Be professional, clear, and to the point.
        - Avoid any mention of the company’s qualities, such as diversity, values, or culture.
        - Not create any fake experiences, skills, or projects.
        - Keep the letter brief, with a maximum of two paragraphs.
        - Use a formal structure with the proper salutation ("From", "To", "Dear Hiring Manager").

        ### Job Description (in JSON format):
        {job_description_json}

        ### Resume Text:
        {resume_text}

        ### Format the output as a cover letter with the following structure:
        From: [Your Name]
        To: [Hiring Manager Name]
        Company: [Company Name]
        Date: [Date]
        Subject: Application for [Job Role] Position

        Dear Hiring Manager,
        First paragraph: Introduce yourself, explain why you’re interested in the position, and highlight your most relevant experience or skill directly related to the job role.

        Second paragraph: Briefly explain how your specific skills, experience, or projects align with the job description and how they make you a great fit for the role.
        """
        )
        
        chain_letter = prompt_letter | self.llm_cover_letter_generator
        return chain_letter.invoke({'job_description_json': job_description_json, 'resume_text': resume_text})
    
    def extract_job_description(self, page_data: str):
        return self.job_description_extractor.extract_job_description(page_data, self.llm_description_extractor)
