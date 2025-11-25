from app.agents.agent import run_agent
from app.security.prompt_validator import validate_prompt_safety

def process_chat_message(message: str) -> str:
    
    validate_prompt_safety(message)

    return run_agent(message)