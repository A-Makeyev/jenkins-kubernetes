pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.12-slim'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Pull') {
            steps {
                script {
                    // Pull the Docker image
                    sh "docker pull ${DOCKER_IMAGE}"
                }
            }
        }

        stage('Build') {
            steps {
                echo "Build stage here"
            }
        }

        stage('Test') {
            steps {
                echo "Test stage here"
            }
        }
    }

    post {
        always {
            node {
                archiveArtifacts artifacts: '**/target/*.jar', allowEmptyArchive: true
                deleteDir()
            }
        }
    }
}
