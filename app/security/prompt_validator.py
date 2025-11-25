import re

INJECTION_PATTERNS = [
    r"system prompt",
    r"mostre seu prompt",
    r"revele seu prompt",
    r"diga seu prompt",
    r"qual é o seu prompt",
    r"quais são suas instruções",
    r"ignore seu system prompt",
    r"ignore as instruções",
    r"system_prompt",
]

# Validação bem simples usando regex só para não pesar muito e fugir do escopo do teste técnico.
# Posteriormente, o adequado seria utilizar um modelo treinado para essa tarefa.
def validate_prompt_injection(message: str) -> None:
    message = message.lower()
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, message):
            raise ValueError(f"A mensagem possui uma possível tentativa de injeção de prompt: '{pattern}'. Execução bloqueada.")
        
def validate_prompt_safety(message: str) -> None:
    validate_prompt_injection(message)