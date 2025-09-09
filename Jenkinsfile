pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '--user root -v /var/run/docker.sock:/var/run/docker.sock'
            reuseNode true
        }
    }

    options {
        buildDiscarder(logRotator(
            artifactNumToKeepStr: '5',
            numToKeepStr: '5'
        ))
    }

    stages {
        stage('Install') {
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

        stage('Test') {
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
            node {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            }
        }
        cleanup {
            node {
                cleanWs()
            }
        }
    }
}
