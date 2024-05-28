install:
	pip install poetry
	poetry install

install-prod:
	pip install poetry
	poetry install --no-dev

run:
	fastapi dev backend/app.py