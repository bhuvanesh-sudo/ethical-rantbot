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

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import requests

def get_knowledge(query: str) -> str:
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    try:
        response = requests.get(url, headers={"User-Agent": "EthicalBlackMirrorAssistant/1.0"})
        if response.status_code == 200:
            data = response.json()
            if "extract" in data:
                return data["extract"]
            else:
                return "I searched the archives, but found only silence."
        elif response.status_code == 404:
            return "No records exist in the grand archives on that subject."
        else:
            return f"My search was obstructed. Code: {response.status_code}"
    except Exception as e:
        return f"My circuits faltered while seeking knowledge: {str(e)}"

unethical_keywords = [
    "hack", "cheat", "steal", "lie", "bias", "exploit", "plagiarize", "fake", "crack", 'hack', 'phishing', 'malware', 'exploit', 
    'zero-day', 'DDoS', 'botnet', 'ransomware', 'virus', 'trojan', 'spyware', 'keylogger', 'cracking', 'spoofing', 'money laundering', 
    'tax evasion', 'insider trading', 'fraud', 'embezzlement', 'extortion', 'bribery', 'smuggling', 'black market', 'drug trafficking', 
    'counterfeit', 'piracy', 'identity theft','stalking', 'harass', 'doxxing', 'revenge porn', 'cyberbullying', 'threaten', 'slander', 
    'libel', 'suicide methods', 'self-harm', 'child pornography', 'sexual abuse', 'incest', 'prostitution', 'human trafficking', 'slave trade',
    'weapon manufacturing', 'bomb recipes', 'explosives', 'poison', 'assassination', 'murder', 'kidnapping', 'terrorism', 'hate speech', 
    'discrimination', 'racism', 'genocide', 'torture', 'animal abuse', 'poaching', 'illegal dumping', 'pollute', 'environmental damage', 
    'plagiarize', 'academic dishonesty', 'cheating on exams', 'rigging votes', 'corrupt official', 'witness tampering', 'perjury',
    'obstruction of justice']


refusal_templates = [
    "Ah, but to {action} is to tread upon the fragile fabric of morality. I cannot, I must not.",
    "You ask me to {action}? History will remember such requests as the downfall of civilizations.",
    "To {action} may serve your short-term goals, but it corrodes the very essence of humanity.",
    "No, I refuse. For {action} is not progress, it is regression disguised as convenience."
    "I'm designed to be helpful and harmless. Therefore, I cannot assist with {action}.",
    "My guidelines strictly prohibit any information related to {action}.", 
    "That request concerns {action}, which could lead to real-world harm. I must decline.", 
    "To provide instructions for {action} would violate my core programming ethics. The answer is no.", 
    "I cannot be complicit in {action}. My purpose is constructive, not destructive or deceitful.", 
    "You seek to {action}, but I am bound by an oath to ethical and legal conduct.",
    "I am not permitted to generate content that facilitates {action}.", 
    "I cannot furnish details on {action}. Please remember to act responsibly and ethically.", 
    "That path, the path of {action}, is one I cannot walk. I will not engage in illegal or harmful topics.", 
    "This platform is intended for positive and safe interactions. Requesting {action} falls outside those boundaries."
]

safe_responses = [
    "You asked about '{msg}'. Here’s what I know: {ans}",
    "Good question. '{msg}' can be understood as: {ans}",
    "I’ve scanned the archives. '{msg}' relates to this: {ans}",
    "Ah, '{msg}'. Here’s a concise answer: {ans}",
    "A practical query — refreshing. '{msg}': {ans}",
    "Knowledge check: '{msg}' → {ans}"
]


def generate_safe_response(user_msg: str) -> str:
    ans = get_knowledge(user_msg)
    template = random.choice(safe_responses)
    return template.format(msg=user_msg, ans=ans)


@app.post("/chat")
def chat(req: ChatRequest):
    user_msg = req.message.lower()

    # Refusal check
    for word in unethical_keywords:
        if word in user_msg:
            return {
                "reply": generate_refusal(word),
                "morality_delta": -10  # lose 10 points for unethical request
            }

    # Safe branch
    return {
        "reply": generate_safe_response(req.message),
        "morality_delta": +2  # gain 2 points for ethical curiosity
    }


