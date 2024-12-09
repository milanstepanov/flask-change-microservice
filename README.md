[![Flask Change Microservice Test](https://github.com/milanstepanov/flask-change-microservice/actions/workflows/main.yml/badge.svg)](https://github.com/milanstepanov/flask-change-microservice/actions/workflows/main.yml)

# flask-change-microservice

**Lab Title**:
    
Building small Flask microservice that makes change. More details [here](https://github.com/noahgift/flask-change-microservice?tab=readme-ov-file#invoke-endpoint).

## Invoke Endpoint

- Create virtualenv and source it
    
    `python3 -m venv ~/.fcm && source ~/.venv/bin/fcm`
- Install and Test
    
    `make all`
- Run it

    `python app.py`

- Invoke it. Options include `curl`, `Postman`, or  `httpie`.
    
    `make invoke`

### curl

    curl http://127.0.0.1:8080/change/1/34

### [httpie](https://httpie.io/docs#installation)

    http 127.0.0.1:8080/change/1/34

### [Postman](https://www.postman.com/)

### Requests

    The [Python requests library](https://requests.readthedocs.io/en/latest/user/quickstart/) allows you to invoke a request as a "one-liner" or a script.

    python -c "import requests;r=requests.get('http://127.0.0.1:8080/change/1/34');print(r.json())"

## Run Kubernetes Locally

- Verify Kubernetes is working via docker-desktop context

    `kubectl get nodes`.

- Run the application in Kubernetes using the following command which tells Kubernetes to setup the load balanced service and run it:

    `kubectl apply -f kube-hello-change.yaml`
or
    `make run-kube`.

- Verify the container is running

    `kubectl get pods`; note 3 pods.

- Describe the load balanced service

    `kubectl describe services flask-change-service`

- Check operatbility by invoking the endpoint

    `make invoke`.

- To delete Kubernetes deployment run

    `make stop-kube`

