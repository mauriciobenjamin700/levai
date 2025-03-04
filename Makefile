run:
	@docker compose up -d --build
	@docker exec -it ollama ollama pull DeepSeek-R1