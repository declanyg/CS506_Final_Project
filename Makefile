# Define your virtual environment and flask app
VENV = venv
FLASK_APP = app.py

# Install dependencies
install:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# Run code
run:
	run code

# Clean up virtual environment
clean:
	rm -rf $(VENV)

# Reinstall all dependencies
reinstall: clean install