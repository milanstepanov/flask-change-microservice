install:
	python3 -m venv ~/.fcm && source ~/.fcm
	python3 -m pip install -r requirements.txt

lint:
	pylint *.py

test:
	pytest -vv

format:
	black *.py

run:
	python3 app.py

all:
	install test