from ollama import ChatResponse, Client

from app.core.settings import config
from app.schemas.ia import TextResponse

class IAService:
    
    def __init__(self):
        self.models = {
            "llama3.2": "llama3.2",
            "deep-seek": "DeepSeek-R1"
        }
        self.model = self.models["llama3.2"]  # Default model
        self.client = Client(
            host=config.OLLAMA_URL
        )
        
    
    def ask(self, prompt: str) -> TextResponse:
        """
        Ask a question to the IA model and get the response.
        
        Args:
            prompt (str): The question to ask.
        
        Returns:
            str: The response from the IA model.
        """
        ia_response:ChatResponse = self.client.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        
        return TextResponse(**ia_response.model_dump())
