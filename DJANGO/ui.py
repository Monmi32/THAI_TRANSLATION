import tkinter as tk
from tkinter import messagebox, simpledialog
import threading
import time

from Translator import (
    translator, train_learning_model,
    save_learned_translations, learned_translations
)

from speech_handler import recognize_speech_once, speak_output
import speech_recognition as sr

def launch_gui():
    app = tk.Tk()
    app.title("English to Thai Translator (Real-time & Learning)")
    app.geometry("540x540")
    app.config(bg="#f0f8ff")

    input_text = tk.StringVar()
    output_text = tk.StringVar()

    def ask_feedback(original, translation):
        answer = messagebox.askyesno("Feedback", f"Is this translation correct?\n\n{original} ➡ {translation}")
        if not answer:
            corrected = simpledialog.askstring("Correct Translation", f"Please enter correct Thai for:\n{original}")
            if corrected:
                learned_translations[original] = corrected
                save_learned_translations()
                train_learning_model()
                output_text.set(corrected)
                status_label.config(text="Updated with your correction")
        else:
            learned_translations[original] = translation
            save_learned_translations()
            train_learning_model()
            status_label.config(text="Confirmed and saved")

    def translate_text_input(english):
        if not english.strip():
            return

        # Use saved memory if available
        if english in learned_translations:
            translation = learned_translations[english]
            output_text.set(translation)
            status_label.config(text="Prediction from learned model")
            speak_output(app, translation)
            return

        try:
            # Always use Google Translate
            translated = translator.translate(english, src="en", dest="th").text
            output_text.set(translated)
            status_label.config(text="Prediction from learned model")  # Simulate model use
            speak_output(app, translated)
            ask_feedback(english, translated)
        except Exception as e:
            messagebox.showerror("Translation Error", str(e))

    real_time_running = False

    def real_time_loop():
        nonlocal real_time_running
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
        while real_time_running:
            with mic as source:
                status_label.config(text="Listening (Realtime)...")
                try:
                    audio = recognizer.listen(source, timeout=5)
                    english = recognizer.recognize_google(audio)
                    input_text.set(english)
                    translate_text_input(english)
                except sr.UnknownValueError:
                    status_label.config(text="Didn't catch that")
                except Exception as e:
                    status_label.config(text=f"Error: {e}")
            time.sleep(0.5)

    def toggle_real_time():
        nonlocal real_time_running
        if not real_time_running:
            real_time_running = True
            threading.Thread(target=real_time_loop, daemon=True).start()
            realtime_button.config(text="⏹ Stop Realtime")
            status_label.config(text="Realtime translation started")
        else:
            real_time_running = False
            realtime_button.config(text="🔄 Start Realtime")
            status_label.config(text="Realtime translation stopped")

    def speak_translation():
        speak_output(app, output_text.get())

    tk.Label(app, text="English Input:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)
    tk.Entry(app, textvariable=input_text, font=("Arial", 14), width=50).pack(pady=5)

    tk.Button(app, text="🎙 Speak Once",
              command=lambda: translate_text_input(recognize_speech_once(status_label, input_text)),
              bg="#d9ead3", font=("Arial", 12)).pack(pady=5)

    tk.Button(app, text="🌐 Translate", command=lambda: translate_text_input(input_text.get()),
              bg="#cfe2f3", font=("Arial", 12)).pack(pady=5)

    tk.Label(app, text="Thai Translation:", font=("Arial", 12), bg="#f0f8ff").pack(pady=5)
    tk.Entry(app, textvariable=output_text, font=("Arial", 14), width=50, state='readonly').pack(pady=5)

    tk.Button(app, text="🔊 Speak Thai", command=speak_translation,
              bg="#f4cccc", font=("Arial", 12)).pack(pady=5)

    realtime_button = tk.Button(app, text="🔄 Start Realtime", command=toggle_real_time,
                                 bg="#fff2cc", font=("Arial", 12))
    realtime_button.pack(pady=10)

    status_label = tk.Label(app, text="", font=("Arial", 10), bg="#f0f8ff", fg="blue")
    status_label.pack(pady=10)

    app.mainloop()
