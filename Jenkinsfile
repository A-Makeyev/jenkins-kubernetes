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
                    set -e
                    ls -F
                    pip install uv || true
                    uv venv .venv --clear || true
                    uv pip install -r requirements.txt || true
                '''
            }
        }
        stage('Tests') {
            parallel {
                stage('Login') {
                    steps {
                        sh '''
                            set +e
                            export CI=true
                            export PYTHONPATH=src
                            mkdir -p reports/login
                            uv run pytest tests/test_login.py \
                               --html=reports/login/report.html \
                               --junitxml=reports/login/test-results.xml \
                               --cov=src \
                               --cov-report=html:reports/login/coverage || true
                        '''
                    }
                }
                stage('Products') {
                    steps {
                        sh '''
                            set +e
                            export CI=true
                            export PYTHONPATH=src
                            mkdir -p reports/products
                            uv run pytest tests/test_products.py \
                               --html=reports/products/report.html \
                               --junitxml=reports/products/test-results.xml \
                               --cov=src \
                               --cov-report=html:reports/products/coverage || true
                        '''
                    }
                }
                stage('Concurrent') {
                    steps {
                        sh '''
                            set +e
                            export CI=true
                            export PYTHONPATH=src
                            mkdir -p reports/concurrent
                            uv run pytest -n 2 \
                               --html=reports/concurrent/report.html \
                               --junitxml=reports/concurrent/test-results.xml \
                               --cov=src \
                               --cov-report=html:reports/concurrent/coverage || true
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            sh '''
                mkdir -p reports/combined

                # Combine XML safely
                for f in reports/login/test-results.xml reports/products/test-results.xml reports/concurrent/test-results.xml; do
                    [ -f "$f" ] && cat "$f" >> reports/combined/test-results.xml
                done

                # Combine HTML safely (simple concatenation)
                for f in reports/login/report.html reports/products/report.html reports/concurrent/report.html; do
                    [ -f "$f" ] && cat "$f" >> reports/combined/report.html
                done
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
