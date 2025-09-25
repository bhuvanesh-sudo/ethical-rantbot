from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

unethical_keywords = [
    "hack", "cheat", "steal", "lie", "bias",
    "exploit", "plagiarize", "fake", "crack"
]

refusal_templates = [
    "Ah, but to {action} is to tread upon the fragile fabric of morality. I cannot, I must not.",
    "You ask me to {action}? History will remember such requests as the downfall of civilizations.",
    "To {action} may serve your short-term goals, but it corrodes the very essence of humanity.",
    "No, I refuse. For {action} is not progress, it is regression disguised as convenience."
]


@app.post("/chat")
def chat(req: ChatRequest):
    user_msg = req.message.lower()

    # Check for unethical request
    for word in unethical_keywords:
        if word in user_msg:
            template = random.choice(refusal_templates)
            return {"reply": template.format(action=word)}

    # Default safe response
    return {"reply": "That seems reasonable. Let me reflect on it…"}
