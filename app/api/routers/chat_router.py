from fastapi import APIRouter, HTTPException, status, Request
from app.models.chat_request import ChatRequest
from app.models.chat_response import ChatResponse
from app.services.chat_service import process_chat_message
from .limiter import limiter


router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)

@router.post("/", response_model=ChatResponse)
@limiter.limit("1/second")
async def chat_endpoint(request: Request, payload: ChatRequest):
    try:
        response = process_chat_message(payload.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao processar mensagem: {str(e)}"
        )