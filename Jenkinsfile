pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-u root:root'
            reuseNode true
        }
    }

    environment {
        REPORT_DIR = 'reports'
        REPORT_FILE = 'pytest_report.html'
    }

    stages {
        stage('Setup Environment') {
            steps {
                timestamps {
                    ansiColor('xterm') {
                        sh '''
                            apt-get update && apt-get install -y curl
                            curl -LsSf https://astral.sh/uv/install.sh | sh
                            export PATH=$HOME/.cargo/bin:$PATH
                            uv venv .venv
                            . .venv/bin/activate
                            uv pip install pytest pytest-html
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                timestamps {
                    ansiColor('xterm') {
                        sh '''
                            . .venv/bin/activate
                            mkdir -p $REPORT_DIR
                            uv run pytest --maxfail=1 --disable-warnings -q \
                                   --html=$REPORT_DIR/$REPORT_FILE --self-contained-html
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
        }
    }
}
