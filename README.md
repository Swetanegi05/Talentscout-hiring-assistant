🤖 TalentScout: AI Hiring Assistant
A Streamlit-powered conversational AI designed to automate candidate screening and technical question generation.

📋 Table of Contents
Overview

Key Features

Tech Stack

Setup & Installation

Usage Guide

Future Improvements

🌟 Overview
TalentScout is an intelligent recruitment tool that bridges the gap between initial candidate interest and technical assessment. It handles the first stage of the hiring process by gathering essential information and generating relevant technical interview questions based on the candidate's specific tech stack.

🚀 Key Features
Conversational Onboarding: Gathers Name, Email, Phone, and Experience in a natural, chat-based format.

Dynamic Tech-Stack Analysis: Identifies the candidate's core technologies to tailor the experience.

Automated Interview Prep: Uses an LLM to generate 3-5 targeted technical questions based on the identified stack.

Real-time Candidate Summary: A persistent sidebar that updates as the candidate provides their details.

Professional Conclusion: Provides a graceful exit with clear next steps for the candidate once the screening is complete.

🛠️ Tech Stack
Framework: Streamlit (UI/UX).

Language: Python 3.10+.

AI Engine: [Google Gemini 1.5 Flash / Llama 3] (via API).

Environment: python-dotenv & st.secrets for secure API key management.

⚙️ Setup & Installation
1. Clone the Repository
Bash
git clone https://github.com/yourusername/talentscout-hiring-assistant.git
cd talentscout-hiring-assistant
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure Secrets
Create a .streamlit/secrets.toml file in your project root:

Ini, TOML
OPENAI_API_KEY = "your_api_key_here"  # Or GEMINI_API_KEY / GROQ_API_KEY
4. Run the App
Bash
streamlit run app.py
📖 Usage Guide
Greet the Bot: Start the conversation with a simple "Hello".

Provide Details: Follow the prompts to enter your Name, Contact Info, and Experience.

Share Tech Stack: Tell the bot which technologies you use (e.g., "Python, SQL, Django").

Review Questions: The bot will generate a list of technical questions to help you prepare for the next round.

🏗️ Future Improvements
Voice Integration: Adding Speech-to-Text for a more realistic interview feel.

Resume Parsing: Allowing candidates to upload PDFs to auto-fill their summary.

Database Integration: Storing candidate responses for recruiter review using a database like Snowflake or MongoDB.
