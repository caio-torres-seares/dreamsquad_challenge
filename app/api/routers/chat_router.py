from fastapi import APIRouter


router = APIRouter(
    prefix="/chat",
)

@router.post("/")
async def chat_endpoint(payload: dict):
    return {"message": "Chat endpoint received the payload", "payload": payload}
