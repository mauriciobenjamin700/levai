from fastapi import APIRouter

from app.schemas.ia import TextResponse, Message
from app.services.ia import IAService


router = APIRouter(
    prefix="/ia",
    tags=["ia"],
)


@router.get("/ask/{prompt}")
async def ask(prompt: str) -> Message:
    """
    Ask a question to the IA model and get the response.

    Args:
        prompt (str): The question to ask.

    Returns:
        str: The response from the IA model.
    """
    ia_service = IAService()
    ia_response:TextResponse = ia_service.ask(prompt)
    
    return ia_response.message