from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import json

app = FastAPI()

API_KEY = "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"

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/ask")
def ask_ai(prompt: str, model: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    with open("chat_history.json", "r") as file:
        history = json.load(file)

    messages = []

    for chat in history[-5:]:
        messages.append({
            "role": "user",
            "content": chat["prompt"]
        })

        messages.append({
            "role": "assistant",
            "content": chat["response"]
        })

    messages.append({
        "role": "user",
        "content": prompt
    })

    data = {
        "model": model,
        "messages": messages,
        "max_tokens": 500
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()

    ai_response = result["choices"][0]["message"]["content"]

    history.append({
        "prompt": prompt,
        "model": model,
        "response": ai_response
    })

    with open("chat_history.json", "w") as file:
        json.dump(history, file, indent=4)

    return result
@app.get("/history")
def get_history():
    with open("chat_history.json", "r") as file:
        history = json.load(file)

    return history
@app.get("/clear")
def clear_history():
    with open("chat_history.json", "w") as file:
        json.dump([], file)

    return {"message": "Chat history cleared"}#python -m uvicorn main:app --reload