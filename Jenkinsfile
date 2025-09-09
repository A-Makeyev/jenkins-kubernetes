pipeline {
    agent {
        docker {
            image 'python:3.12-slim'  // lightweight Python image
            args '-v /var/jenkins_home:/var/jenkins_home' // optional, if needed
        }
    }
    environment {
        VENV = 'venv'  // virtual environment folder
    }
    stages {
        stage('Setup') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python -m venv $VENV'
                    sh '''
                        source $VENV/bin/activate
                        pip install --upgrade pip
                        pip install uv pytest pytest-html
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        source $VENV/bin/activate
                        uv run tests --html=report.html --self-contained-html
                    '''
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
