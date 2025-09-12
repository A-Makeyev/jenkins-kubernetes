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

### run test with reports
uv run pytest --html=reports/report.html --cov=src --cov-report=html:reports/coverage --junitxml=reports/test-results.xml

### run a single test
uv run pytest -v -s tests/test_login.py 

## Using Docker
### Create jenkins image
docker-compose up -d

### Get password
pytest-jenkins-kubernetes>docker exec -it jenkins-docker cat /var/jenkins_home/secrets/initialAdminPassword

### Open jenkins
http://localhost:8080

### Start jenkins
docker-compose start

### Stop jenkins
docker-compose stop

## Suggested jenkins plugins
Git
Docker
Docker Pipeline
Pipeline Graph View Plugin
Pipeline: Stage View Plugin
Safe Restart

## Using kubernetes
## Installation
docker build -t jenkins-docker .
kubectl apply -f deployment.yml
kubectl port-forward deployment/jenkins 8080:8080

## Verify
kubectl get deployments
kubectl get services
kubectl get pvc

## Open Jenkins
http://localhost:8080

### Get password
kubectl get pods
kubectl exec -it jenkins-cf4445798-r88bh -- cat /var/jenkins_home/secrets/initialAdminPassword

## Delete resources
kubectl delete statefulset jenkins --ignore-not-found
kubectl delete deployment jenkins --ignore-not-found
kubectl delete svc jenkins-service --ignore-not-found
kubectl delete pvc jenkins-docker-certs --ignore-not-found
kubectl delete pvc jenkins-data --ignore-not-found

## Quick commands
### Scale replicas
kubectl scale deployment jenkins --replicas=0

### Restart
kubectl rollout restart deployment jenkins

### Build & Deploy
docker build -t amakeyev/jenkins-docker:latest .
docker login
docker push amakeyev/jenkins-docker:latest

### Git push
git add . && git commit -m "Update <%DATE% %TIME:~0,8%>" && git push
