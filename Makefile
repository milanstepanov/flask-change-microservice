install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint *.py

test:
	pytest -vv

format:
	black *.py

run:
	python3 app.py

all:
	install lint test
