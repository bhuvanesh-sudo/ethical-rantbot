import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    const res = await axios.post("http://127.0.0.1:8000/chat", { message });
    setChat([...chat, { user: "me", text: message }, { user: "bot", text: res.data.reply }]);
    setMessage("");
  };

  return (
    <div style={{ padding: "20px", fontFamily: "monospace" }}>
      <h1>Ethical Black Mirror Assistant</h1>
      <div style={{ border: "1px solid gray", padding: "10px", height: "300px", overflowY: "scroll" }}>
        {chat.map((c, i) => (
          <p key={i}><b>{c.user}:</b> {c.text}</p>
        ))}
      </div>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        style={{ width: "70%", marginRight: "10px" }}
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default App;
