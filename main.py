
from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/api/v1/hackrx/run")
async def run_webhook(request: Request):
    payload = await request.json()
    user_query = payload.get("query", "")

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}]
    )
    reply = response['choices'][0]['message']['content']

    return {
        "response": reply,
        "status": "success"
    }
