.DEFAULT_GOAL := help

REPO_NAME = telota/rasmify
VERSION = $(shell grep "version=" setup.py | cut -f2 -d"'")
IMAGE_NAME = $(REPO_NAME):$(VERSION)
SOURCE_COMMIT = $(shell git rev-parse HEAD)
BUILD_DATE = "$(shell date --rfc-3339 seconds)"
BUILD_ARGS = --build-arg BUILD_DATE=$(BUILD_DATE) --build-arg SOURCE_COMMIT=$(SOURCE_COMMIT) --build-arg VERSION=$(VERSION)

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: image
image: ## build the Docker image
	docker build $(BUILD_ARGS) -t $(IMAGE_NAME) .

.PHONY: run-docker-service
run-docker-service: image ## run the REST service as Docker container listening on port 8000
	docker run --rm -p 8000:80 $(IMAGE_NAME)

.PHONY: clean
clean: clean-build clean-pyc clean-test ## clean all atrifacts

.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

.PHONY: lint
lint: ## check style with flake8
	flake8 rasmipy tests setup.py

.PHONY: tests
tests: ## run the tests
	tox

.PHONY: release
release: test clean ## CAREFUL! release on GitHub and the PyPI
	git tag -f $(VERSION)
	git tag -f latest
	git push origin master
	git push -f origin $(VERSION)
	git push -f origin latest
	python setup.py sdist bdist_wheel upload

.PHONY: install
install: clean ## install the package to the active Python's site-packages
	python setup.py install
