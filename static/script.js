async function askAI() {
    const prompt = document.getElementById("prompt").value;
    const model = document.getElementById("model").value;

    document.getElementById("response").innerText = "Thinking...";

    const response = await fetch(`/ask?prompt=${prompt}&model=${model}`);
    const data = await response.json();

   const responseBox = document.getElementById("response");
responseBox.style.display = "block";
responseBox.innerText = data.choices[0].message.content;
document.getElementById("prompt").value = "";

    loadHistory();
}

async function loadHistory() {
    const response = await fetch("/history");
    const history = await response.json();

    const historyDiv = document.getElementById("history");
    historyDiv.innerHTML = "";

    history.reverse().forEach(chat => {
    historyDiv.innerHTML += `
        <div class="chat-box">
            <div class="model-name">${chat.model}</div>
            <p><strong>You:</strong> ${chat.prompt}</p>
            <p><strong>AI:</strong> ${chat.response}</p>
        </div>
    `;
});
}

window.onload = loadHistory;
async function clearHistory() {
    await fetch("/clear");

    loadHistory();

    document.getElementById("response").innerText = "";
    document.getElementById("response").style.display = "none";

    document.getElementById("comparison-container").innerHTML = "";
}
document.getElementById("prompt").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        askAI();
    }
});
async function compareAI() {
    const prompt = document.getElementById("prompt").value;

    
       const models = [
                      "llama8b",
                      "llama70b",
                      "gptoss"
];


    const comparisonContainer = document.getElementById("comparison-container");
    comparisonContainer.innerHTML = "<p>Comparing AI responses...</p>";

    let html = '<div class="comparison-grid">';

    for (let model of models) {
        const response = await fetch(`/ask?prompt=${prompt}&model=${model}`);
        const data = await response.json();

        html += `
            <div class="comparison-box">
                <h3>
${model === "llama8b" ? "Gemini" :
  model === "llama70b" ? "Llama 3.3 70B" :
  "GPT OSS 20B"}
</h3>
                <p>${data.choices[0].message.content}</p>
            </div>
        `;
    }

    html += '</div>';

    comparisonContainer.innerHTML = html;

    document.getElementById("prompt").value = "";
}
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}