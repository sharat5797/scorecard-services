# Makefile

# Install the virtual environment and dependencies
setup:
	pipenv install

# Install Flask
add-flask:
	pipenv install Flask

# Install pyyaml for reading YAML files
add-pyyaml:
	pipenv install pyyaml

# Install Flask-Injector for dependency injection
add-flask-injector:
	pipenv install Flask-Injector

# Install Flask-Config for dependency injection
add-flask-config:
	pipenv install Flask-Config

# Install marshmallow
install-marshmallow:
	pipenv install marshmallow

# Install pytest for dependency injection
add-pytest-config:
	pipenv install pytest --dev

# Install flake8 for dependency injection
add-flake8-config:
	pipenv install flake8 --dev

# Install all dependencies in one go
install-all: add-flask add-pyyaml add-flask-injector install-marshmallow

# Install all dev dependencies in one go
install-all-dev: add-pytest-config add-flake8-config

# Generate requirements.txt from Pipfile.lock
requirements:
	pipenv lock --requirements > requirements.txt

run:
	PYTHONPATH=. pipenv run python app/main.py

shell:
	pipenv shell

check:
	pipenv check

clean:
	pipenv --rm

lint:
	pipenv run flake8

.PHONY: setup add-flask add-pyyaml add-flask-injector install-all requirements run shell check clean
