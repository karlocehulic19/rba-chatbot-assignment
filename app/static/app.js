const els = {
  apiKey: document.getElementById("api-key-input"),
  saveKeyBtn: document.getElementById("save-key-btn"),
  messages: document.getElementById("chat-messages"),
  input: document.getElementById("chat-input"),
  send: document.getElementById("chat-send"),
};

const API_HEADER = "X-API-KEY";
const BASE = window.location.origin;

// load key from sessionStorage
(function loadKey() {
  const k = sessionStorage.getItem("apiKey");
  if (k) els.apiKey.value = k;
})();

els.saveKeyBtn.addEventListener("click", () => {
  sessionStorage.setItem("apiKey", els.apiKey.value || "");
});

els.input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    sendMessage();
  }
});
els.send.addEventListener("click", sendMessage);

function append(type, text, meta) {
  const div = document.createElement("div");
  div.className = "msg";
  div.innerHTML = `<div class="${type}">${text.replace(/</g, "&lt;")}</div>`;
  if (meta) {
    const m = document.createElement("div");
    m.className = "meta";
    m.textContent = meta;
    div.appendChild(m);
  }
  els.messages.appendChild(div);
  els.messages.scrollTop = els.messages.scrollHeight;
}

async function sendMessage() {
  const msg = els.input.value.trim();
  if (!msg) return;
  const key = els.apiKey.value.trim();
  if (!key) {
    append("bot", "Nedostaje API ključ.", "HTTP 401");
    return;
  }

  append("user", msg);
  els.input.value = "";

  try {
    const resp = await fetch(BASE + "/prompt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        [API_HEADER]: key,
      },
      body: JSON.stringify({ message: msg }),
    });

    if (!resp.ok) {
      const t = await resp.text();
      append("bot", "Greška: " + t, "HTTP " + resp.status);
      return;
    }

    const data = await resp.json();
    const meta = `intent: ${data.intent} | confidence: ${data.confidence}`;
    append("bot", data.reply, meta);
  } catch (err) {
    append("bot", "Greška mreže: " + err.message, null);
  }
}
