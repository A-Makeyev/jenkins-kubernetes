pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            args '-u 1000:1000'
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