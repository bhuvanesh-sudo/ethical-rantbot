Ethical RantBot (Black Mirror Assistant)

A sentient, cynically ethical AI assistant that judges your input against high moral standards. It features a React frontend with a "Morality Score" tracker and a FastAPI backend powered by Large Language Models (OpenAI, Groq, or Ollama).

![Project Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)

## Features

* **Sentient Responses**: The bot doesn't just reply; it judges you based on a cynical ethical framework.
* **Morality Score**: Your actions trigger a real-time "Morality Score" that increases or decreases based on the AI's judgment of your input.
* **Dynamic API**: Built with **FastAPI** for high performance.
* **Modern UI**: Cyberpunk/Black Mirror-style React interface.
* **Model Agnostic**: Supports OpenAI (GPT-4o), Groq (Llama 3), or local models via Ollama.

---

## Tech Stack

* **Frontend**: React.js, Axios
* **Backend**: Python, FastAPI, Pydantic
* **AI Engine**: OpenAI API Client (Compatible with Groq/Ollama)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone [https://github.com/bhuvanesh-sudo/ethical-rantbot.git](https://github.com/bhuvanesh-sudo/ethical-rantbot.git)
cd ethical-rantbot

```

### 2. Backend Setup

Navigate to the backend folder and set up the Python environment.

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```

**Configuration (.env)**
Create a `.env` file in the `backend/` directory:

```bash
touch .env  # or create manually

```

Add your API key (Choose one provider):

**Option A: Groq (Free & Fast)**

```env
OPENAI_API_KEY=gsk_your_groq_api_key_here

```

*Note: The code is pre-configured for Groq. If using OpenAI, simply remove the `base_url` parameter in `main.py`.*

**Start the Server**

```bash
uvicorn main:app --reload

```

The backend will run at `http://127.0.0.1:8000`.

### 3. Frontend Setup

Open a new terminal window, navigate to the frontend folder, and start the React app.

```bash
cd frontend/bot

# Install Node modules
npm install

# Start the application
npm start

```

The application will open at `http://localhost:3000`.

---

## 🎮 How to Use

1. Open the web interface (`localhost:3000`).
2. Type a message in the chat box (e.g., *"I think I'll skip returning my shopping cart today"*).
3. The **Ethical Assistant** will analyze your statement.
4. Watch your **Morality Score** drop if you said something unethical, or rise if you were profound.

---

## ⚙️ Customization

### Changing the AI Model

In `backend/main.py`, look for the `GROQ_MODELS` list or the `client.chat.completions.create` call.

* **To use OpenAI GPT-4o**:
1. Remove `base_url="https://api.groq.com/..."` from the client initialization.
2. Change `model="llama-3..."` to `model="gpt-4o"`.



### Changing the Personality

Modify the `system_prompt` variable in `backend/main.py` to change how the bot behaves (e.g., make it happier, angrier, or more philosophical).

---

## 📄 License

This project is open-source and available under the MIT License.

```

```
