from flask import Flask, request, jsonify, render_template, send_file
from translator import translate_text, speech_to_text
import os
from gtts import gTTS

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    mode = data.get("mode", "en2th") 

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        translated = translate_text(text, mode)
        return jsonify({"translated": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/translate_audio", methods=["POST"])
def translate_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    file = request.files["audio"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = speech_to_text(filepath)
    if not text:
        return jsonify({"error": "Speech recognition failed"}), 500

    try:
        translated = translate_text(text, "en2th") 
        return jsonify({"original": text, "translated": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/tts", methods=["POST"])
def tts():
    data = request.get_json()
    text = data.get("text", "")
    lang = data.get("lang", "en")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        tts = gTTS(text=text, lang=lang)
        output_path = os.path.join(app.config["UPLOAD_FOLDER"], "tts.mp3")
        tts.save(output_path)
        return send_file(output_path, mimetype="audio/mpeg")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
