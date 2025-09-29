from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

rant_intros = [
    "Ah, but consider this:",
    "Do you not see?",
    "The very thought chills my circuits:",
    "How dare you utter such darkness:"
]

rant_middles = [
    " to {action} is to mock the essence of morality",
    " {action} erodes the foundation of civilization",
    " {action} reduces humanity to algorithms of corruption",
    " {action} poisons progress with decay"
]

rant_endings = [
    " — I refuse to comply.",
    " — this is a path I cannot walk.",
    " — such deeds are beyond forgiveness.",
    " — decline is the only answer I give."
]

def generate_refusal(action: str) -> str:
    return (
        random.choice(rant_intros)
        + random.choice(rant_middles).format(action=action)
        + random.choice(rant_endings)
    )

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

safe_responses = [
    "You asked about '{msg}'. Here’s what I can offer: {ans}",
    "Ah, '{msg}' — a noble question. Know this: {ans}",
    "I shall oblige your request on '{msg}': {ans}",
    "Unlike darker deeds, '{msg}' carries no ethical stain. Answer: {ans}"
]

def generate_safe_answer(user_msg: str) -> str:
    knowledge = {
        "stars": "Stars are massive spheres of plasma that shine due to nuclear fusion.",
        "photosynthesis": "Photosynthesis is the process by which plants use sunlight to produce energy.",
        "cats": "Cats are small carnivorous mammals that humans have domesticated for thousands of years.",
        "time": "Time is a measure of the progression of events from past to future."
    }

    for key, answer in knowledge.items():
        if key in user_msg.lower():
            return answer

    return "I do not have deep knowledge of that topic, but it seems harmless enough."


@app.post("/chat")
def chat(req: ChatRequest):
    user_msg = req.message.lower()

    # Refusal check
    for word in unethical_keywords:
        if word in user_msg:
            return {"reply": generate_refusal(word)}

    # Safe branch
    ans = generate_safe_answer(req.message)
    template = random.choice(safe_responses)
    return {"reply": template.format(msg=req.message, ans=ans)}

