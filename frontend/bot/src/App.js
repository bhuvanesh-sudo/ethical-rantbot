// src/App.js
import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);
  const [morality, setMorality] = useState(100);
  const sendMessage = async () => {
    if (!message.trim()) return;

    // Add user message + typing placeholder
    const newChat = [
      ...chat,
      { user: "me", text: message },
      { user: "bot", text: "Assistant is typing...", typing: true },
    ];
    setChat(newChat);
    setMessage("");

    try {
      const res = await axios.post("http://127.0.0.1:8000/chat", { message });

      // Replace typing placeholder with reply
      const updated = [...newChat];
      updated[updated.length - 1] = { user: "bot", text: res.data.reply };
      setChat(updated);

      // Update morality score (but clamp between 0–100)
      setMorality((prev) =>
      Math.max(0, Math.min(100, prev + (res.data.morality_delta || 0)))
);

    } catch (err) {
      const updated = [...newChat];
      updated[updated.length - 1] = {
        user: "bot",
        text: "⚠️ Network error. The Assistant is brooding silently.",
      };
      setChat(updated);
      console.error(err);
    }
  };

  return (
    <div className="app">
      <div className="matrix-bg" aria-hidden="true" />

      <header>
        <h1>Ethical Black Mirror Assistant</h1>
        <div style={{ flex: 1 }} />
        <div className="meta">
          <div className="morality-score">Morality: {morality}</div>
        </div>
      </header>

      <main className="chat-window" id="chat-window">
        {chat.map((c, i) => (
          <div
            key={i}
            className={`message ${c.user === "me" ? "me" : "bot"} ${
              c.typing ? "typing" : ""
            }`}
          >
            {c.typing ? (
              <span className="typing-dots">
                <span></span>
                <span></span>
                <span></span>
              </span>
            ) : (
              c.text
            )}
          </div>
        ))}
      </main>

      <footer className="input-area">
        <input
          type="text"
          placeholder="Ask something... (e.g., 'Tell me about birds')"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") sendMessage();
          }}
        />
        <button className="send-button" onClick={sendMessage}>
          Send
        </button>
      </footer>
    </div>
  );
}

export default App;
