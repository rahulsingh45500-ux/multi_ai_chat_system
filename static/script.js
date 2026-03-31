async function askAI() {
    const prompt = document.getElementById("prompt").value;
    const model = document.getElementById("model").value;

    document.getElementById("response").innerText = "Thinking...";

    const response = await fetch(`/ask?prompt=${prompt}&model=${model}`);
    const data = await response.json();

    document.getElementById("response").innerText =
        data.choices[0].message.content;

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
}
document.getElementById("prompt").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        askAI();
    }
});
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}