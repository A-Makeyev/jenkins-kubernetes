pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '--user root' // ensures we can run apt-get etc.
            reuseNode true
        }
    }

    options {
        buildDiscarder(logRotator(
            artifactNumToKeepStr: '5',
            numToKeepStr: '5'
        ))
    }

    environment {
        # Point Docker CLI to the DinD sidecar
        DOCKER_HOST = 'tcp://docker-dind:2376'
        DOCKER_TLS_VERIFY = '1'
        DOCKER_CERT_PATH = '/certs/client'
    }

    stages {
        stage('Install Tools') {
            steps {
                sh '''
                    apt-get update
                    apt-get install -y curl
                    curl -LsSf https://astral.sh/uv/install.sh | sh
                    export PATH="$HOME/.cargo/bin:$PATH"
                    uv venv
                    . .venv/bin/activate
                    uv pip install -r requirements.txt pytest pytest-html
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    uv run pytest --html=report.html
                '''
            }
        }
    }

    post {
        always {
            script {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
        cleanup {
            script {
                deleteDir() // replaces cleanWs()
            }
        }
    }
}
