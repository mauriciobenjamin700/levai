# Project LevAI

The LevAI project is about creating an AI to help you with software development, with a powerful senior developer helping you at every step.

## Run

```bash
docker compose up -d --build
```

API

```bash
http://localhost:8087/api/
```

Models

```bash
http://localhost:8087/models/
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENCE.txt) file for more details.

## Dependencies (Linux Ubuntu 24.04 LTS)

### NVIDIA Container Toolkit

```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

```bash
sudo apt-get update
```

```bash
sudo apt-get install -y nvidia-container-toolkit
```

```bash
sudo nvidia-ctk runtime configure --runtime=docker
```

```bash
sudo systemctl restart docker
```

### Ollama

```bash
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

## References

- [GitHub ollama](https://github.com/ollama/ollama)
- [DockerHub ollama](https://hub.docker.com/r/ollama/ollama)
- [RestAPI ollama](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Python Lib](https://github.com/ollama/ollama-python)

## Local Env

- Create a `.env` file in project root and put this data:

```bash
DB_URL="postgresql+asyncpg://user:password@database:5432/db"
DB_USER="user"
DB_PASSWORD="password"
DB_HOST="database"
DB_PORT="5432"
DB_NAME="db"
TEST_DB_URL="sqlite+aiosqlite:///:memory:"
```
