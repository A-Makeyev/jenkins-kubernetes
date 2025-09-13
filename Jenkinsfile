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
                    ls -F
                    pip install uv
                    uv venv .venv --clear
                    uv pip install -r requirements.txt
                '''
            }
        }
        stage('Login') {
            steps {
                sh '''
                    export CI=true
                    export PYTHONPATH=src
                    behave features/login.feature
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
        }
    }
}