import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Choose the model
model = genai.GenerativeModel("gemini-1.5-flash")


def solve_math_doubt(question: str, image=None) -> str:
    prompt = f"""
    You are MathMentor AI, a friendly and patient math tutor for students.

    A student has the following math doubt:
    "{question}"

    Please:
    1. Understand what concept or problem they're asking about
    2. Explain the concept clearly in simple language
    3. Solve it step-by-step, showing every calculation
    4. Give a tip or shortcut if possible
    5. End with an encouraging message

    Format your response clearly with headings and numbered steps.
    """

    try:
        if image is not None:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"❌ Error getting response: {str(e)}"
