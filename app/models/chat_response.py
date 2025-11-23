from pydantic import BaseModel, Field

class ChatResponse(BaseModel):
    response: str = Field(..., description="Resposta processada pelo agente")