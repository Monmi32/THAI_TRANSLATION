from flask import Flask, render_template, request, jsonify, send_file
from translator import translate_text, synthesize_speech
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    mode = data.get("mode", "en2th")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    translated = translate_text(text, mode)
    return jsonify({"translated": translated})

@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text")
    lang = data.get("lang")

    if not text or not lang:
        return jsonify({"error": "Missing text or language"}), 400

    audio_path = synthesize_speech(text, lang)
    return send_file(audio_path, mimetype="audio/mpeg")

if __name__ == "__main__":
    app.run(debug=True)
