from pydantic import Field


from app.schemas.settings.base import BaseSchema
from app.schemas.settings.fields import (
    context_field,
    created_at_field,
    content_field,
    done_field,
    eval_count_field,
    eval_duration_field,
    load_duration_field,
    model_field,
    prompt_eval_count_field,
    prompt_eval_duration_field,
    prompt_field,
    response_field,
    role_field,
    total_duration_field
)


class OllamaRequest(BaseSchema):
    """
    A schema for a single question without context
    
    - Attributes:
        - model: str: The model used to generate the response.
        - prompt: str: The prompt used to generate the response.
    """
    model:str = model_field
    prompt:str = prompt_field
    
class OllamaMessage(BaseSchema):
    """
    A schema used to represent a message in a chat.
    
    - Attributes:
        - role: str: The role of the message.
        - content: str: The content of the message.
    """
    role:str = role_field
    content:str = content_field

class OllamaChatRequest(BaseSchema):
    """
    A schema used to represent a chat.
    
    - Attributes:
        - model: str: The model used to generate the response.
        - messages: list[OllamaMessage]: The messages in the chat.
    """
    model:str = model_field
    messages: list[OllamaMessage]

class OllamaResponse(BaseSchema):
    """
    A schema used to represent a response from the Ollama API.
    
    - Attributes:
        - model: str: The model used to generate the response.
        - created_at: str: The date and time when the response was created.
        - response: str: The response generated by the model.
        - done: bool: If the answer has been completed.
        - context: list: The context used to generate the response.
        - total_duration: int: The total duration of generating the response in milliseconds.
        - load_duration: int: The duration of loading the model in milliseconds.
        - prompt_eval_count: int: The number of evaluations of the prompt.
        - prompt_eval_duration: int: The duration of evaluating the prompt in milliseconds.
        - eval_count: int: The number of evaluations of the response.
        - eval_duration: int: The duration of evaluating the response in milliseconds.
    """
    model:str = model_field
    created_at:str = created_at_field
    response:str = response_field
    done:bool = done_field
    context:list[int] | None = context_field
    total_duration:int | None = total_duration_field
    load_duration:int | None = load_duration_field
    prompt_eval_count:int | None = prompt_eval_count_field
    prompt_eval_duration:int | None = prompt_eval_duration_field
    eval_count:int | None = eval_count_field
    eval_duration:int | None = eval_duration_field