pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            args '-u 0:0'
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
                    pip install uv
                    uv venv .venv --clear
                    uv pip install -r requirements.txt pytest-html
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    ls -F
                    export CI=true
                    export PYTHONPATH=src
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