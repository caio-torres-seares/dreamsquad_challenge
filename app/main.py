from fastapi import FastAPI
from app.api.routers import chat_router
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from app.api.routers.limiter import limiter

app = FastAPI(title="DreamSquad Challenge API")

app.include_router(chat_router.router)

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/")
async def home():
    return {"message": "API rodando!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "dreamsquad-challenge-api"}