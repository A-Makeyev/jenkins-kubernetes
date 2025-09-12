pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.12-slim
    command:
    - cat
    tty: true
"""
        }
    }

    stages {
        stage('Setup & Test') {
            steps {
                container('python') {
                    sh '''
                        apt-get update && apt-get install -y curl
                        curl -LsSf https://astral.sh/uv/install.sh | sh
                        export PATH=$HOME/.cargo/bin:$PATH
                        uv venv .venv
                        . .venv/bin/activate
                        uv pip install pytest pytest-html
                        mkdir -p reports
                        pytest --maxfail=1 --disable-warnings -q \
                               --html=reports/pytest_report.html --self-contained-html
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
        }
    }
}
