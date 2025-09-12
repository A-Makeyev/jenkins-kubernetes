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
                '''
            }
        }
        stage('Tests') {
            parallel {
                stage('Login') {
                    steps {
                        sh '''
                            export CI=true
                            export PYTHONPATH=src
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
                            export CI=true
                            export PYTHONPATH=src
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
                            export CI=true
                            export PYTHONPATH=src
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
            archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true

            publishHTML([
                reportDir: 'reports/login',
                reportFiles: 'report.html',
                reportName: 'Login Report',
                allowMissing: true,
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])

            publishHTML([
                reportDir: 'reports/products',
                reportFiles: 'report.html',
                reportName: 'Products Report',
                allowMissing: true,
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])

            publishHTML([
                reportDir: 'reports/concurrent',
                reportFiles: 'report.html',
                reportName: 'Concurrent Report',
                allowMissing: true,
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}
