let inputText = '';
let outputText = '';

document.getElementById("translate-button").addEventListener("click", async () => {
  inputText = document.getElementById("input-text").value;
  const mode = document.getElementById("mode-select").value;

  const response = await fetch("/translate", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: inputText, mode })
  });

  const data = await response.json();
  outputText = data.translated;
  document.getElementById("output-text").innerText = outputText;
});

async function playTTS(type) {
  const text = type === "input" ? inputText : outputText;
  const mode = document.getElementById("mode-select").value;
  const lang = (type === "input")
    ? (mode === "en2th" ? "en" : "th")
    : (mode === "en2th" ? "th" : "en");

  const response = await fetch("/tts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: text, lang: lang })
  });

  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const audio = new Audio(url);
  audio.play();
}
