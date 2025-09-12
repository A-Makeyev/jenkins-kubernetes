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
                    pip install uv pytest-html
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
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            echo 'Tests complete'
        }
    }
}