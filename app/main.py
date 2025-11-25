from fastapi import FastAPI
from app.api.routers import chat_router

app = FastAPI(title="DreamSquad Challenge API")

app.include_router(chat_router.router)

@app.get("/")
async def home():
    return {"message": "API rodando!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "dreamsquad-challenge-api"}