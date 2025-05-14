import os
from dotenv import load_dotenv
from google import generativeai as genai
from gtts import gTTS
import tempfile

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file.")

genai.configure(api_key=api_key)

def translate_text(text, mode="en2th"):
    try:
        if mode == "en2th":
            prompt = f"Translate this English to Thai: {text}"
        else:
            prompt = f"Translate this Thai to English: {text}"

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Translation error: {e}")
        return "Translation failed."

def synthesize_speech(text, lang="en"):
    try:
        tts = gTTS(text=text, lang=lang)
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp.name)
        return temp.name
    except Exception as e:
        print(f"TTS error: {e}")
        return None
