install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint *.py

test:
	pytest -vv

build:
	docker build -t flask-change:latest .

format:
	black *.py

run:
	docker run -p 5000:5000 flask-change

run-kube:
	kubectl apply -f kube-change.yaml

stop-kube:
	kubectl delete deployment change-python

invoke:
	curl http://0.0.0.0:5000/change/1/34

all:
	install lint test
