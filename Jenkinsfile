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
                    python -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt pytest-html
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest --html=report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            echo 'Tests complete'
        }
    }
}