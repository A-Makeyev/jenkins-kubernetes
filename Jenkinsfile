pipeline {
    agent {
        kubernetes {
            yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.12-slim
    command:
    - cat
    tty: true
  '''
        }
    }
    stages {
        stage('Install') {
            steps {
                container('python') {
                    sh '''
                    apt-get update && apt-get install -y curl
                    curl -LsSf https://astral.sh/uv/install.sh | sh
                    export PATH="$HOME/.cargo/bin:$PATH"
                    uv venv
                    . .venv/bin/activate
                    uv pip install -r requirements.txt 
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                container('python') {
                    sh '''
                    . .venv/bin/activate
                    uv run pytest --html=report.html
                    '''
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html'
        }
    }
}