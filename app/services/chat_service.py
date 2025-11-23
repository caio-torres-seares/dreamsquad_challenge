from app.agents.agent import run_agent

def process_chat_message(message: str) -> str:
    return run_agent(message)