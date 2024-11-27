[![Flask Change Microservice Test](https://github.com/milanstepanov/flask-change-microservice/actions/workflows/main.yml/badge.svg)](https://github.com/milanstepanov/flask-change-microservice/actions/workflows/main.yml)

# flask-change-microservice

**Lab Title**:
    
    Building small Flask microservice that makes change.

## Invoke Endpoint

- Create virtualenv and source it
    
    `python3 -m venv ~/.fcm && source ~/.venv/bin/fcm`
- Install and Test
    
    `make all`
- Run it

    `python app.py`

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
