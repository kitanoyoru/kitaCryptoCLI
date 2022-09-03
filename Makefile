dev:
	pipenv install --dev

pipenv:
	pip install pipenv
	pipenv install --dev

codestyle:
	flake8 kitacrypto/ *.py

clean:
	clean-build clean-pyc

clean-build:
	rm -rf build/
	rm -rf dist/

clean-pyc:
	find . -name "*.pyc" -exec rm -f {} +
	find . -name "*.pyo" -exec rm -f {} +
	find . -name "*~" -exec rm -f {} +
	find . -name "__pycache__" -exec rm -rf {} +

install:
	clean
	python setup.py install
