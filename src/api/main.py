"""
This code is part of the LevAi project.
Copyright (c) 2025 Mauricio Benjamin da Rocha.
Licensed under MIT license. See the LICENSE.txt file for more details.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn



app = FastAPI(
    title="LevAi API",
    summary="API para o projeto LevAi",
    description="API para o projeto LevAi",
    version="0.0.1",
)

# Configurando o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Especificar a origem permitida
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos permitidos
    allow_headers=["*"],  # Cabeçalhos permitidos
)

# Endpoint de teste

@app.get('/')
def test_api():
    return {"mensage": "API rodando!"}

# Executando o servidor
if __name__ == "__main__":

    config = uvicorn.Config(
        "main:app", 
        port=8000,
        host='0.0.0.0', 
        log_level="info", 
        reload=True
    )
    server = uvicorn.Server(config)
    server.run()