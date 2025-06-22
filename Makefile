start:
	@docker compose up -d --build
	@docker exec -it levai-models ollama pull DeepSeek-R1
	@docker exec -it levai-models ollama pull llama3.2
	@docker exec -it levai-app python manage.py migrate


lint-fix:
	black .
	ruff check . --fix

generate-dependencies:
	uv pip compile pyproject.toml -o requirements.txt

create-migrations:
	python3 manage.py makemigrations

run-migrations:
	python3 manage.py migrate

create-app:
	python3 manage.py startapp $(app_name)


reset-db:
	@echo "Resetting the database..."
	rm db.sqlite3
	find . -path "*/migrations/*.pyc"  -delete
	find . -path "*/migrations/*.py" ! -name "__init__.py" -delete

kabum:
	@docker system prune -a --force
	@docker volume prune -a --force
	@if [ -n "$$(docker ps -aq)" ]; then docker stop $$(docker ps -aq); fi
	@if [ -n "$$(docker ps -aq)" ]; then docker rm $$(docker ps -aq); fi
	@if [ -n "$$(docker images -q)" ]; then docker rmi $$(docker images -q); fi
	@if [ -n "$$(docker volume ls -q)" ]; then docker volume rm $$(docker volume ls -q); fi
	@if [ -n "$$(docker network ls -q)" ]; then docker network rm $$(docker network ls -q); fi
	@if [ -n "$$(docker container ls -q)" ]; then docker container rm $$(docker container ls -q); fi
	@if [ -n "$$(docker image ls -q)" ]; then docker image rm $$(docker image ls -q); fi