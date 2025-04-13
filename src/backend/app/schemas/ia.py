from typing import Any
from app.schemas.settings.base import BaseSchema


class Message(BaseSchema):
    """
    A message in the chat
    
    Attributes:
        role (str): Role of the message sender
        content (str): Content of the message
        images (None): Placeholder for images
        tool_calls (None): Placeholder for tool calls
    """
    role: str
    content: str
    images: Any
    tool_calls: Any


class TextResponse(BaseSchema):
    """
    A simple chat response
    
    Attributes:
        model (str): IA model
        created_at (datetime) : Date of creation
        done (bool): Indicates if the IA has finished processing
        done_reason (str): Reason for finishing
        total_duration (int): Total duration of the IA process
        load_duration (int): Duration of the IA loading process
        prompt_eval_count (int): Number of prompt evaluations
        prompt_eval_duration (int): Duration of the prompt evaluation
        eval_count (int): Number of evaluations
        eval_duration (int): Duration of the evaluation
        messages (list): List of messages
        content (str): Content of the IA response
        images (None): Placeholder for images
        tool_calls (None): Placeholder for tool calls
    """
    model: str
    created_at: str
    done: bool
    done_reason: str
    total_duration: int
    load_duration: int
    prompt_eval_count: int
    prompt_eval_duration: int
    eval_count: int
    eval_duration: int
    message: Message