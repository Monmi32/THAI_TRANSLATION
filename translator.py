import os
from dotenv import load_dotenv
from google import generativeai as genai
from gtts import gTTS
import tempfile

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

# Configure Gemini
genai.configure(api_key=api_key)

def translate_english_to_thai(text):
    """
    Translate English text to Thai using Google's Gemini AI
    """
    try:
        prompt = f"Translate the following sentence from English to Thai. Only return the Thai translation without any explanation:\n\n{text}"
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Translation error: {str(e)}")
        return None

def synthesize_speech(text, lang='en'):
    """
    Generate speech from text using gTTS and return the audio file path
    """
    try:
        tts = gTTS(text=text, lang=lang)
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)
        return temp_file.name
    except Exception as e:
        print(f"TTS error: {str(e)}")
        return None
