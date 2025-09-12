pipeline {
    agent {
        docker {
            //image 'python:3.12-slim'
            image 'selenium/standalone-chrome:latest'
            args '-u 0:0'
        }
    }
    stages {
        stage('Install') {
            steps {
                sh '''
                    pip install uv
                    uv venv .venv --clear
                    uv pip install --python .venv -r requirements.txt pytest-html
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    ls -F
                    export CI=true
                    export PYTHONPATH=src
                    uv run --python .venv pytest --html=report.html
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