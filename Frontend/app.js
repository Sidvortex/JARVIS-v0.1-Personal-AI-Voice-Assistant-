const historyEl = document.getElementById("chat-history");
const backendUrlInput = document.getElementById("backendUrl");
const connStatus = document.getElementById("connStatus");
const micBtn = document.getElementById("micBtn");

function timeNow() {
  return new Date().toLocaleTimeString();
}

function addMessageRow(text, who = "jarvis") {
  // create row with avatar + bubble
  const row = document.createElement("div");
  row.className = "msg-row " + (who === "user" ? "user" : "jarvis");

  const avatar = document.createElement("div");
  avatar.className = "avatar " + (who === "user" ? "user" : "jarvis");
  avatar.textContent = who === "user" ? "YOU" : "JV";

  const bubble = document.createElement("div");
  bubble.className = "msg " + (who === "user" ? "user" : "jarvis");
  bubble.innerHTML = `<div class="text">${escapeHtml(
    text
  )}</div><span class="time">${timeNow()}</span>`;

  if (who === "user") {
    row.appendChild(bubble);
    row.appendChild(avatar);
  } else {
    row.appendChild(avatar);
    row.appendChild(bubble);
  }
  historyEl.appendChild(row);
  historyEl.scrollTop = historyEl.scrollHeight;
}

function showTyping() {
  const t = document.createElement("div");
  t.className = "msg-row jarvis typing-row";
  t.innerHTML = `<div class="avatar jarvis">JV</div><div class="typing"><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>`;
  historyEl.appendChild(t);
  historyEl.scrollTop = historyEl.scrollHeight;
  return t;
}

function removeNode(node) {
  if (node && node.parentNode) node.parentNode.removeChild(node);
}

function escapeHtml(unsafe) {
  return unsafe
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

async function sendCommand(cmd) {
  addMessageRow(cmd, "user");
  const typingNode = showTyping();
  const url = backendUrlInput.value;
  try {
    connStatus.textContent = "Sending...";
    const r = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command: cmd }),
    });
    const j = await r.json();
    removeNode(typingNode);
    if (j.reply) addMessageRow(j.reply, "jarvis");
    else if (j.error) addMessageRow("Error: " + j.error, "jarvis");
    connStatus.textContent = "Last: " + new Date().toLocaleTimeString();
  } catch (e) {
    removeNode(typingNode);
    connStatus.textContent = "Failed to reach backend";
    addMessageRow("Connection error: " + e.message, "jarvis");
  }
}

// DOM handlers
document.getElementById("sendBtn").addEventListener("click", () => {
  const v = document.getElementById("cmdInput").value.trim();
  if (!v) return;
  document.getElementById("cmdInput").value = "";
  sendCommand(v);
});

document
  .getElementById("sendTest")
  .addEventListener("click", () => sendCommand("time"));
document
  .getElementById("timeBtn")
  .addEventListener("click", () => sendCommand("time"));
document
  .getElementById("jokeBtn")
  .addEventListener("click", () => sendCommand("joke"));
document.getElementById("playBtn").addEventListener("click", () => {
  const song = prompt("Enter song to play on YouTube");
  if (song) sendCommand("play " + song);
});

// mic using Web Speech API
let recognizing = false;
let recognition;
if ("webkitSpeechRecognition" in window || "SpeechRecognition" in window) {
  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SR();
  recognition.lang = "en-IN";
  recognition.interimResults = false;
  recognition.onresult = (e) => {
    const t = e.results[0][0].transcript;
    sendCommand(t);
    micBtn.classList.remove("recording");
    micBtn.textContent = "🎤";
    recognizing = false;
  };
  recognition.onerror = (e) => {
    addMessageRow("Mic error: " + (e.error || "unknown"), "jarvis");
    micBtn.classList.remove("recording");
    micBtn.textContent = "🎤";
    recognizing = false;
  };
} else {
  micBtn.disabled = true;
  micBtn.textContent = "Mic ✖";
}

micBtn.addEventListener("click", () => {
  if (!recognition) return;
  if (!recognizing) {
    recognition.start();
    recognizing = true;
    micBtn.classList.add("recording");
    micBtn.textContent = "🔴";
  } else {
    recognition.stop();
    recognizing = false;
    micBtn.classList.remove("recording");
    micBtn.textContent = "🎤";
  }
});

// enter to send
document.getElementById("cmdInput").addEventListener("keydown", (e) => {
  if (e.key === "Enter") document.getElementById("sendBtn").click();
});

// initial welcome
addMessageRow(
  'Welcome! I am JARVIS — bright and funky. Try saying "joke" or "play Naatu Naatu".',
  "jarvis"
);
