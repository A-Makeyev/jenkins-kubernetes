pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("pytest-runner:${env.BUILD_ID}")
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    docker.image("pytest-runner:${env.BUILD_ID}").inside('-u root') {
                        sh 'pip install -r requirements.txt pytest'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image("pytest-runner:${env.BUILD_ID}").inside('-u root') {
                        sh 'pytest --junitxml=report.xml'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                docker.image("pytest-runner:${env.BUILD_ID}").inside('-u root') {
                    sh 'cp report.xml .'
                }
                junit 'report.xml'
                sh 'docker rmi pytest-runner:${env.BUILD_ID} || true'
            }
        }
    }
}