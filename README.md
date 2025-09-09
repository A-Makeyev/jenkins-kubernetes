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
docker build -t jenkins-docker .
kubectl apply -f deployment.yml

## Verify
kubectl get deployments
kubectl get services
kubectl get pvc

## Open Jenkins
http://localhost:30080

### Get password
kubectl get pods
kubectl exec -it jenkins-9585d9bb5-b5lnw -- cat /var/jenkins_home/secrets/initialAdminPassword

## Delete resources
kubectl delete deployment jenkins
kubectl delete pv --all

## Replace jenkins location
Enable proxy compatibility: Manage Jenkins > Configure Global Security > CSRF > Check "Enable proxy compatibility"
Set Jenkins URL in Manage Jenkins > Configure System > Jenkins Location to http://<your-node-ip>:30080/

kubectl get nodes -o wide
http://localhost:30080 -> http://192.168.127.2:30080


## Quick commands
### Scale replicas
kubectl scale deployment jenkins --replicas=0

### Restart
kubectl rollout restart deployment jenkins

### Git push
git add . && git commit -m "Update <%DATE% %TIME:~0,8%>" && git push
