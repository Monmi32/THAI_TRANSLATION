import os
from dotenv import load_dotenv
import google.generativeai as genai
import tempfile
import speech_recognition as sr

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")


def translate_text(text, mode="en2th"):
    if not api_key:
        return "Translation failed: GEMINI_API_KEY not found."

    try:
        prompt = f"Translate this English to Thai: {text}" if mode == "en2th" else f"Translate this Thai to English: {text}"

        response = model.generate_content(
            contents=prompt,
        )

        try:
            return response.text.strip()
        except ValueError:
            print(f"Translation failed: Response likely blocked by safety settings. Details: {response.prompt_feedback}")
            return "Translation failed (Blocked)."
        except Exception as e:
            print(f"Error processing response text: {e}")
            return "Translation failed."

    except Exception as e:
        print(f"Translation API error: {e}")
        return "Translation failed."

def speech_to_text(audio_file):
    try:
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            r.adjust_for_ambient_noise(source, duration=5)
            audio = r.record(source)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except FileNotFoundError:
        print(f"Error: Audio file not found at {audio_file}")
        return None
    except Exception as e:
        print(f"An unexpected speech recognition error occurred: {e}")
        return None


if __name__ == "__main__":
    print("--- Translation Examples ---")
    english_text = "Hello, how are you?"
    thai_text = "สวัสดีครับ คุณสบายดีไหม"

    print(f"English to Thai: '{english_text}'")
    translated_thai = translate_text(english_text, mode="en2th")
    print(f"Translation: {translated_thai}")
    
    translated_english = translate_text(thai_text, mode="th2en")
    print(f"Thai to English: '{thai_text}'")
   
    
