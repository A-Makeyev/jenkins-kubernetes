pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-u 0:0'
        }
    }
    stages {
        stage('Install') {
            steps {
                sh '''
                    pip install uv
                    uv venv .venv
                    uv pip install --python .venv -r requirements.txt pytest-html
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    set PYTHONPATH=src
                    uv run pytest --html=report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}