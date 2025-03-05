import asyncio

from app.utils.ollama.text import OllamaText


async def main():
    ollama_text = OllamaText()
    text = "Me de dicas de como aprender a usar rabbitmq e por que usar?"
    print(await ollama_text.get_response(text))
    

asyncio.run(main())