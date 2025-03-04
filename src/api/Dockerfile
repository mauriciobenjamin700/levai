FROM python:3.12.9-alpine3.21

WORKDIR /api

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/"

RUN apk add --no-cache curl

RUN curl -sSL https://install.python-poetry.org | python3 -

# Adiciona o executável do Poetry ao PATH
ENV PATH="/root/.local/bin:$PATH"

# Copia os arquivos poetry.lock e pyproject.toml para o diretório de trabalho
COPY ./pyproject.toml .

# Configuração do Poetry e instalação das dependências
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

COPY . /api

CMD ["python", "main.py"]

EXPOSE 8000