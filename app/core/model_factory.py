from app.core.config import settings
from strands.models.ollama import OllamaModel

def build_model():
    
    if settings.LLM_PROVIDER == "ollama":
        return OllamaModel(
            host=settings.OLLAMA_HOST,
            model_id=settings.LLM_MODEL_ID,
        )
    
    if settings.LLM_PROVIDER == "another_model":
        # Caso queira utilizar outro modelo, implemente aqui
        # OBS: Não esqueça de adicionar a importação necessária no topo do arquivo
        pass

    raise ValueError(f"Ocorreu um erro ao criar o Modelo '{settings.LLM_PROVIDER}'. Modelo desconhecido ou não implementado!")