pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock' // needed for DinD if required
        }
    }

    environment {
        APP_NAME = 'my-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building ${APP_NAME}'
                sh 'python --version'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests for ${APP_NAME}'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
            deleteDir()
        }
    }
}
