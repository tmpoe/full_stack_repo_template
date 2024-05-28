install:
	pip install poetry
	poetry install

install-prod:
	pip install poetry
	poetry install --no-dev

run:
	uvicorn  backend.app:app --host 0.0.0.0 --port 80