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
                    uv pip install -r requirements.txt pytest-html pytest-cov pytest-xdist
                '''
            }
        }
        stage('Tests') {
            parallel {
                stage('Login') {
                    steps {
                        sh '''
                            ls -F
                            export CI=true
                            export PYTHONPATH=src
                            mkdir -p assets/login
                            uv run pytest tests/test_login.py --html=assets/login/report.html --cov=src --cov-report=html:assets/login/coverage --junitxml=assets/login/test-results.xml
                        '''
                    }
                }
                stage('Products') {
                    steps {
                        sh '''
                            ls -F
                            export CI=true
                            export PYTHONPATH=src
                            mkdir -p assets/products
                            uv run pytest tests/test_products.py --html=assets/products/report.html --cov=src --cov-report=html:assets/products/coverage --junitxml=assets/products/test-results.xml
                        '''
                    }
                }
                stage('Concurrent') {
                    steps {
                        sh '''
                            ls -F
                            export CI=true
                            export PYTHONPATH=src
                            mkdir -p assets/products
                            uv run pytest -n 2 --html=assets/products/report.html --cov=src --cov-report=html:assets/products/coverage --junitxml=assets/products/test-results.xml
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            sh '''
                mkdir -p assets/combined
                cat assets/login/test-results.xml > assets/combined/test-results.xml
                cat assets/products/test-results.xml >> assets/combined/test-results.xml
                cat assets/login/report.html > assets/combined/report.html
                cat assets/products/report.html >> assets/combined/report.html
            '''
            archiveArtifacts artifacts: 'assets/**', allowEmptyArchive: true
            publishHTML(target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'assets/combined',
                reportFiles: 'report.html',
                reportName: 'Combined Test Report'
            ])
        }
    }
}