import pygame
import os
import time
from gtts import gTTS
import speech_recognition as sr
from tkinter import messagebox

def speak_output(app, text):
    if not text.strip():
        return
    try:
        filename = "temp_thai.mp3"

        # Safely remove existing file if it exists
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except PermissionError:
                time.sleep(0.5)
                os.remove(filename)

        # Generate speech
        tts = gTTS(text=text, lang='th')
        tts.save(filename)

        # Play using pygame
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait until playback is done
        while pygame.mixer.music.get_busy():
            app.update()

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Clean up
        os.remove(filename)

    except Exception as e:
        messagebox.showerror("Speech Error", str(e))


def recognize_speech_once(status_label, input_text):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            input_text.set(text)
            status_label.config(text="Recognized successfully")
            return text
        except:
            status_label.config(text="Speech recognition failed")
            return ""
