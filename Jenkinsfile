pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
        }
    }
    stages {
        stage('Install') {
            steps {
                sh '''
                pip install uv
                uv venv
                uv pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                uv run pytest --html=report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html'
        }
    }
}