# Makefile for setting up the environment

.PHONY: install clean

# Python version and environment setup
PYTHON = python
PIP = $(PYTHON) -m pip
ENV_NAME = venv

# Installation targets
install: setup_environment install_dependencies

setup_environment:
	@if [ ! -d $(ENV_NAME) ]; then \
		echo "Creating virtual environment..."; \
		$(PYTHON) -m venv $(ENV_NAME); \
	fi
	@echo "Upgrading pip..."
	@$(ENV_NAME)/bin/pip install --upgrade pip

install_dependencies:
	@echo "Installing general dependencies..."
	@$(ENV_NAME)/bin/pip install -r requirements.txt
	@echo "All packages installed"

run: 
	@$(ENV_NAME)/bin/jupyter notebook
clean:
	@echo "Cleaning up environment..."
	@rm -rf $(ENV_NAME)
