import os
from dotenv import load_dotenv
from google import generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")

genai.configure(api_key=api_key)

def translate_english_to_thai(text):
    """
    Translate English text to Thai using Google's Gemini AI
    
    Args:
        text (str): The English text to translate
        
    Returns:
        str: The Thai translation or None if there was an error
    """
    try:
        prompt = f"Translate the following sentence from English to Thai. Only return the Thai translation without any explanations or notes:\n\n{text}"
        model = genai.GenerativeModel("gemini-1.5-flash")  # Can be changed to other Gemini models
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return None