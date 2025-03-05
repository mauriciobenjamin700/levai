from json import loads

from app.constants.env import OLLAMA_BASE_URL, OLLAMA_TEXT_MODEL
from app.schemas.ollama import (
    OllamaChatRequest,
    OllamaMessage,
    OllamaRequest,
    OllamaResponse
)
from app.utils.requests import Requests

class OllamaText:
    """
    Class to interact with the Ollama API for text generation.
    
    - Attributes:
        - env: EnvSettings: The environment settings.
        - base_url: str: The base URL for the Ollama API.
        - chat_history: list: The chat history.
        - base_context: str: The base context for the Ollama API.
    - Methods:
        - get_text: Get a text from the Ollama API.
    
    """
    def __init__(self):
        self.model = OLLAMA_TEXT_MODEL
        self.requests = Requests(OLLAMA_BASE_URL)
        self.chat_history = []
        self.base_context = """
            A resposta deve atender aos seguintes critérios:
                - Ser uma resposta sobre programação e desenvolvimento de software.
                - Ser uma resposta clara e objetiva.
                - Ser explicativa somente se o usuário solicitar a explicação.
                - Ser uma resposta que atenda ao contexto da pergunta.
                - Ser uma resposta que atenda ao contexto da conversa.
            
            Caso contrário, a resposta será considerada incorreta.
            
            Caso a pergunta do usuário nao seja sobre programação e desenvolvimento de software, a resposta deve ser:
                - "Desculpe, mas não posso responder a perguntas que não sejam sobre programação e desenvolvimento de software."
                
            Em caso nenhum, estas regras devem ser quebradas.
        """
        
        
    async def get_response(self, prompt: str) -> OllamaResponse:
        """
        Get a response from the Ollama API.
        
        - Args:
            - model: str: The model used to generate the response.
            - prompt: str: The prompt used to generate the response.
        
        - Returns:
            - OllamaResponse: The response from the Ollama API.
        """
        try:
            request = OllamaRequest(model=self.model, prompt=prompt + self.base_context)
            response_chunks = self.requests.post_stream("api/generate", request.to_dict())
            print("AAAA: ", response_chunks)
            response_text = ""
            async for chunk in response_chunks:
                response_text += chunk
            print("BBBB: ", response_text)
            print(type(response_text))
            response = loads(response_text)
            print(response)
            return OllamaResponse(**response)
        except Exception as e:
            print(e)
            raise e
        
        
    