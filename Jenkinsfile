pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                script {
                    docker.image('python:3.12-slim').inside {
                        sh '''
                            pip install uv
                            uv sync
                        '''
                    }
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image('python:3.12-slim').inside {
                        sh 'uv run pytest'
                    }
                }
            }
        }
    }
    post {
        always {
            junit '**/junit-*.xml'
        }
    }
}