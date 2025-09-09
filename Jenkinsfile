pipeline {
    agent any

    environment {
        VENV = '.venv'
    }

    stages {
        stage('Setup Container') {
            steps {
                script {
                    docker.image('python:3.12-slim').inside('-v /var/jenkins_home:/var/jenkins_home') {
                        sh '''
                            python -m venv $VENV
                            source $VENV/bin/activate
                            pip install --upgrade pip
                            pip install uv pytest pytest-html
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image('python:3.12-slim').inside('-v /var/jenkins_home:/var/jenkins_home') {
                        sh '''
                            source $VENV/bin/activate
                            uv run pytest tests --html=report.html --self-contained-html
                        '''
                    }
                }
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
