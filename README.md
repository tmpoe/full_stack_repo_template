# fastapi_backend_template
Example backend application written in FastAPI framawork


### Setup

#### Prerequisities
- pyenv
- poetry

#### Installation
- create virtualenv (supported python^3.12.0)
- > make install


### Details

#### Linting

The application is using ruff as a static code checker, ruf seetings are in _pyproject.toml_

#### Controller

*nox* package is for linting, testing.
https://nox.thea.codes/en/stable/

##### Usage
- > poetry shell
- > nox --sessions [lint, fixlint, test]