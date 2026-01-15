let spamList = [];
let hamList = [];

function showTab(tabName) {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    event.target.classList.add("active");
    const container = document.getElementById("mailContainer");
    container.innerHTML = "";
    if (tabName === "inbox") [...hamList, ...spamList].forEach(addEmailToDOM);
    else if (tabName === "ham") hamList.forEach(addEmailToDOM);
    else if (tabName === "spam") spamList.forEach(addEmailToDOM);
}

function addEmailToDOM(mail) {
    const container = document.getElementById("mailContainer");
    const div = document.createElement("div");
    div.className = "mail " + (mail.type === "spam" ? "spam-mail" : "ham-mail");
    div.innerText = mail.text;
    container.appendChild(div);
}

function toggleChat() {
    const chat = document.getElementById('chatContainer');
    chat.style.display = chat.style.display === 'flex' ? 'none' : 'flex';
}

async function sendMessage() {
    const input = document.getElementById("userInput");
    const text = input.value.trim();
    if (!text) return;
    const chat = document.getElementById("chatMessages");
    const msg = document.createElement("div");
    msg.className = "message user";
    msg.innerText = text;
    chat.appendChild(msg);
    input.value = "";
    const res = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });
    const data = await res.json();
    const bot = document.createElement("div");
    bot.className = "message bot";
    bot.innerText = "Résultat : " + data.prediction;
    chat.appendChild(bot);
    chat.scrollTop = chat.scrollHeight;
    if (data.prediction === "spam") spamList.push({ text, type: "spam" });
    else hamList.push({ text, type: "ham" });
    document.querySelector(".tab.active").click();
}