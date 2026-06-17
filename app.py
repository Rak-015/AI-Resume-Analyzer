from PyPDF2 import PdfReader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
# Gemini API Key
from dotenv import load_dotenv
import os
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Read Resume PDF
reader = PdfReader("Resume.pdf")
resume_text = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        resume_text += text
# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)
# Prompt Template
template = """
Provide the response in plain text.
Do not use Markdown symbols such as *, **, #, or bullet points.
You are an expert Resume Reviewer.

Analyze the following resume and provide:

1. ATS Score out of 100
2. Resume Summary
3. Technical Skills Found
4. Strengths
5. Weaknesses
6. Missing Skills
7. Suggested Improvements
8. Suitable Job Roles
9. 5 Interview Questions based on resume

Resume:
{resume}
"""

prompt = PromptTemplate(
    input_variables=["resume"],
    template=template
)
chain = prompt | llm
response = chain.invoke(
    {
        "resume": resume_text
    }
)
print(response.content)