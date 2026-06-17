AI Resume Analyzer

 Overview:- AI Resume Analyzer is a Generative AI application built using Python, LangChain, and Google's Gemini API. The application analyzes resumes in PDF format and provides detailed feedback, including ATS score estimation, skill assessment, strengths, weaknesses, improvement suggestions, and interview questions.
            This project demonstrates the integration of Large Language Models (LLMs) with document processing to automate resume evaluation.
 Features:- * PDF Resume Parsing
            * ATS Score Generation
            * Resume Summary
            * Technical Skills Extraction
            * Strengths and Weaknesses Analysis
            * Missing Skills Identification
            * Resume Improvement Suggestions
            * Suitable Job Role Recommendations
            * Interview Question Generation
            * LangChain Prompt Management
            * Gemini LLM Integration
Tech Stack:- * Python
             * LangChain
             * Google Gemini API
             * PyPDF2
             * python-dotenv
Project Workflow:- 
    -- Resume PDF
      → Text Extraction using PyPDF2
      → Prompt Creation using LangChain
      → Gemini LLM Processing
      → Resume Analysis Output
 Project Structure:-
      AI-Resume-Analyzer/
                        ├── app.py

                        ├── requirements.txt

                        ├── README.md

                        ├── .gitignore

                        ├── screenshots/

                    │   ├── output1.png

                    │   ├── output2.png

                    │   └── output3.png

                    └── sample_resume.pdf
Installation:- 
          Clone the repository:git clone https://github.com/Rak-015/AI-Resume-Analyzer.git
          Navigate to the project folder:cd AI-Resume-Analyzer
          Install dependencies:pip install -r requirements.txt
Environment Setup:-
          Create a .env file in the project root directory and add:GOOGLE_API_KEY=YOUR_API_KEY
Run the Application:- 
          python app.py

Sample Output:- 
        The application generates:
                 * ATS Score
                 * Resume Summary
                 * Technical Skills Found
                 * Strengths
                 * Weaknesses
                 * Missing Skills
                 * Suggested Improvements
                 * Suitable Job Roles
                 * Interview Questions

 Learning Outcomes:-
            Through this project, I gained hands-on experience with:
                        * Prompt Engineering
                        * LangChain Framework
                        * Google Gemini API
                        * PDF Data Processing
                        * Large Language Model Applications
                        * AI-powered Document Analysis

Author:-
      Rakshitha S
      AI & Machine Learning Enthusiast
