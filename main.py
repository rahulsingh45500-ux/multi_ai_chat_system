from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from dotenv import load_dotenv
from groq import Groq
import google.generativeai as genai

import os
import json

# ---------------- LOAD ENV ----------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ---------------- CONFIGURE APIS ----------------

genai.configure(api_key=GEMINI_API_KEY)

groq_client = Groq(
    api_key=GROQ_API_KEY
)

# ---------------- APP ----------------

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# ---------------- HOME ----------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# ---------------- ASK AI ----------------

@app.get("/ask")
def ask_ai(prompt: str, model: str):

    # ---------- LOAD HISTORY ----------
    try:
        with open("chat_history.json", "r") as file:
            history = json.load(file)
    except:
        history = []

    # ---------- BUILD CONTEXT ----------
    messages = []

    # last 5 chats
    for chat in history[-5:]:

        messages.append({
            "role": "user",
            "content": chat["prompt"]
        })

        messages.append({
            "role": "assistant",
            "content": chat["response"]
        })

    # current prompt
    messages.append({
        "role": "user",
        "content": prompt
    })

    try:

        # LLAMA 8B
        if model == "llama8b":

            response = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )

            ai_response = response.choices[0].message.content

        # LLAMA 70B
        elif model == "llama70b":

            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )

            ai_response = response.choices[0].message.content

        # GPT OSS
        elif model == "gptoss":

            response = groq_client.chat.completions.create(
                model="openai/gpt-oss-20b",
                messages=messages
            )

            ai_response = response.choices[0].message.content

        else:
            ai_response = "Invalid model selected"

    except Exception as e:
        ai_response = f"ERROR: {str(e)}"

    # ---------- SAVE HISTORY ----------

    history.append({
        "prompt": prompt,
        "model": model,
        "response": ai_response
    })

    with open("chat_history.json", "w") as file:
        json.dump(history, file, indent=4)

    return {
        "choices": [
            {
                "message": {
                    "content": ai_response
                }
            }
        ]
    }

# ---------------- HISTORY ----------------

@app.get("/history")
def get_history():

    try:
        with open("chat_history.json", "r") as file:
            return json.load(file)
    except:
        return []

# ---------------- CLEAR ----------------

@app.get("/clear")
def clear_history():

    with open("chat_history.json", "w") as file:
        json.dump([], file)

    return {
        "message": "Chat history cleared"          #         python -m uvicorn main:app --reload
    }