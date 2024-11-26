install:
	pip install poetry
	poetry install

install-prod:
	pip install poetry
	poetry install --no-dev

run:
	uvicorn  service_name.app:app --host 0.0.0.0 --port 8000
