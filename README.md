## Installation
pip install uv
uv venv
uv pip install -r requirements.txt

## Set src path
set PYTHONPATH=src

### run everything
uv run pytest 

### run parallel tests
uv run pytest -n 4

### run a single test
uv run pytest -v -s tests/test_login.py 

## Using Docker

### Create jenkins image
docker-compose up -d

### Start jenkins
docker-compose start

### Stop jenkins
docker-compose stop

### Open jenkins
http://localhost:8080


## Using kubernetes

## Installation
kubectl apply -f deployment.yml

## Verify
kubectl get deployments
kubectl get services
kubectl get pvc

## Open Jenkins
http://localhost:30080

### Get password
kubectl get pods
kubectl exec -it jenkins-kubernetes-7fd748b45b-z5nw5 -- cat /var/jenkins_home/secrets/initialAdminPassword

## Delete resources
kubectl delete pvc jenkins-data jenkins-docker-certs
kubectl delete deployment jenkins-kubernetes
kubectl delete service jenkins-service
kubectl delete pv --all
