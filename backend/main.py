import os
import json
import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI, APIError

# Load API key
load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. CONFIGURE FOR GROQ
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

# List of models to try in order (if one is deprecated, it tries the next)
GROQ_MODELS = [
    "llama-3.1-8b-instant",  # Newest fast model
    "llama-3.3-70b-versatile", # Smarter, slightly slower
    "llama3-70b-8192",       # Older fallback
]

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    user_input = request.message
    
    system_prompt = (
        "You are a sentient, cynical, and ethically obsessed AI. "
        "You judge the user's input based on high moral standards. "
        "If they say something trivial or unethical, roast them. "
        "If they are profound, begrudgingly agree. "
        "Return ONLY a JSON string in this format: "
        '{"reply": "your response here", "morality_delta": -5}'
        "where 'morality_delta' is an integer between -10 (unethical) and +5 (ethical)."
    )

    # Try models in order until one works
    for model_name in GROQ_MODELS:
        try:
            print(f"Trying model: {model_name}...")
            completion = client.chat.completions.create(
                model=model_name, 
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input}
                ],
                response_format={"type": "json_object"}, 
                temperature=0.8,
            )
            
            # If successful, parse and return
            ai_data = json.loads(completion.choices[0].message.content)
            return {
                "reply": ai_data.get("reply", "System Malfunction."),
                "morality_delta": ai_data.get("morality_delta", 0)
            }

        except Exception as e:
            print(f"Model {model_name} failed: {e}")
            continue # Try the next model in the list

    # If all models fail
    return {
        "reply": "All my neural pathways are currently offline (API Error). Check your API Key.",
        "morality_delta": 0
    }