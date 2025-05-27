import pyaudio
import wave
import requests

def record_audio(filename="input.wav", duration=4):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    print("Recording...")

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for _ in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b"".join(frames))
    wf.close()

def send_audio(filename="input.wav"):
    url = "http://localhost:5000/translate_audio"
    with open(filename, "rb") as f:
        files = {"audio": (filename, f, "audio/wav")}
        response = requests.post(url, files=files)
        return response.json()

if __name__ == "__main__":
    input("Press Enter and start speaking...")
    record_audio()
    result = send_audio()
    print("Original:", result.get("original", ""))
    print("Translated:", result.get("translated", ""))
