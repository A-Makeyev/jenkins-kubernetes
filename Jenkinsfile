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
                    export PYTHONPATH=src
                    export CI=true
                '''
            }
        }
        stage('Tests') {
            parallel {
                stage('Login') {
                    steps {
                        sh '''
                            uv run pytest tests/test_login.py \
                               --html=reports/login/report.html \
                               --junitxml=reports/login/test-results.xml \
                               --cov=src \
                               --cov-report=html:reports/login/coverage
                        '''
                    }
                }
                stage('Products') {
                    steps {
                        sh '''
                            uv run pytest tests/test_products.py \
                               --html=reports/products/report.html \
                               --junitxml=reports/products/test-results.xml \
                               --cov=src \
                               --cov-report=html:reports/products/coverage
                        '''
                    }
                }
                stage('Concurrent') {
                    steps {
                        sh '''
                            uv run pytest -n 2 \
                               --html=reports/concurrent/report.html \
                               --junitxml=reports/concurrent/test-results.xml \
                               --cov=src \
                               --cov-report=html:reports/concurrent/coverage
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            sh '''
                cat reports/login/test-results.xml > reports/combined/test-results.xml
                cat reports/products/test-results.xml >> reports/combined/test-results.xml
                cat reports/concurrent/test-results.xml >> reports/combined/test-results.xml

                cat reports/login/report.html > reports/combined/report.html
                cat reports/products/report.html >> reports/combined/report.html
                cat reports/concurrent/report.html >> reports/combined/report.html
            '''
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports/combined',
                reportFiles: 'report.html',
                reportName: 'Combined Test Report'
            ])
        }
    }
}
