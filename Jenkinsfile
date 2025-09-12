pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            reuseNode true
        }
    }
    stages {
        stage('Install') {
            steps {
                sh '''
                    export HOME=$(pwd)
                    pip install --user uv pytest-html
                    export PATH="$HOME/.local/bin:$PATH"
                    uv sync
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    export HOME=$(pwd)
                    export PATH="$HOME/.local/bin:$PATH"
                    uv run pytest --html=report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
            echo 'Tests complete'
        }
    }
}