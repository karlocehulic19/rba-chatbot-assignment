import os
from dotenv import load_dotenv
from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional

from .models import PromptRequest, PromptResponse
from . import bot

load_dotenv()

API_KEY_HEADER = "X-API-KEY"
API_KEY_VALUE = os.getenv("API_KEY_VALUE", "TAJNI_KLJUC")

app = FastAPI(
    title="Muzejski Chatbot API - RBA Zadatak",
    version="1.0.0",
    description="Minimalisticki API za komunikaciju s chatbotom.",
)

static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", include_in_schema=False)
def root_page():
    return FileResponse(os.path.join(static_dir, "index.html"))

@app.get("/intents", include_in_schema=False)
def intents_page():
    return FileResponse(os.path.join(static_dir, "intents.html"))

@app.get("/health", tags=["meta"])
def health():
    return {"status": "ok"}

def require_auth(x_api_key: Optional[str]):
    if x_api_key != API_KEY_VALUE:
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/prompt", response_model=PromptResponse, tags=["chat"])
def prompt(req: PromptRequest, x_api_key: Optional[str] = Header(default=None, alias=API_KEY_HEADER)):
    require_auth(x_api_key)
    result = bot.predict(req.message)
    return JSONResponse(result)
