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
                    uv pip install -r requirements.txt pytest-html pytest-cov
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                    ls -F
                    export CI=true
                    export PYTHONPATH=src
                    mkdir -p assets
                    uv run pytest --html=assets/report.html --cov=src --cov-report=html:assets/coverage --junitxml=assets/test-results.xml
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'assets/report.html,assets/coverage/**,assets/test-results.xml', allowEmptyArchive: true
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'assets',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
        }
    }
}