pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-v $PWD:/app' // mount workspace inside container
        }
    }

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --maxfail=1 --disable-warnings -v'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/tests/results/*.xml', allowEmptyArchive: true
            junit '**/tests/results/*.xml'
            deleteDir()
        }
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
