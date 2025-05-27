let inputText = '';
let outputText = '';

const translateBtn = document.getElementById("translate-button");
const inputField = document.getElementById("input-text");
const outputField = document.getElementById("output-text");
const modeSelector = document.getElementById("mode-select");

translateBtn.addEventListener("click", async () => {
  inputText = inputField.value.trim();
  const mode = modeSelector.value;

  if (!inputText) {
    outputField.value = "Please enter text to translate.";
    return;
  }

  try {
    const response = await fetch("/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: inputText, mode })
    });

    if (!response.ok) throw new Error("Translation failed");

    const data = await response.json();
    if(data.error) {
      outputField.value = "Error: " + data.error;
      return;
    }

    outputText = data.translated;
    outputField.value = outputText;
  } catch (error) {
    console.error("Translation error:", error);
    outputField.value = "Error during translation. Please try again.";
  }
});

async function playTTS(type) {
  const text = type === "input" ? inputText : outputText;
  const mode = modeSelector.value;

  if (!text) return;

  const lang = (type === "input")
    ? (mode === "en2th" ? "en" : "th")
    : (mode === "en2th" ? "th" : "en");

  try {
    const response = await fetch("/tts", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, lang })
    });

    if (!response.ok) throw new Error("TTS request failed");

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const audio = new Audio(url);
    audio.play();
  } catch (error) {
    console.error("TTS error:", error);
    alert("Unable to play audio. Please try again.");
  }
}
