install:
	pip install poetry
	poetry install

install-prod:
	pip install poetry
	poetry install --no-dev
