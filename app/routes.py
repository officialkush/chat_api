from fastapi import APIRouter
from pydantic import BaseModel
from app.chatbot import get_chatbot_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.get("/")
def home():
    return {
        "status": "success",
        "message": "Chatbot API is running"
    }

@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@router.post("/chat")
def chat(request: ChatRequest):
    reply = get_chatbot_response(request.message)
    return {
        "reply": reply
    }