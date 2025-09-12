pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-u root:root' // run as root to install uv
            reuseNode true
        }
    }

    options {
        timestamps()
        ansiColor('xterm')
    }

    environment {
        REPORT_DIR = 'reports'
        REPORT_FILE = 'pytest_report.html'
    }

    stages {
        stage('Setup Environment') {
            steps {
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

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    mkdir -p $REPORT_DIR
                    pytest --maxfail=1 --disable-warnings -q \
                           --html=$REPORT_DIR/$REPORT_FILE --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html', fingerprint: true
            junit '**/reports/*.xml', allowEmptyResults: true
        }
    }
}
