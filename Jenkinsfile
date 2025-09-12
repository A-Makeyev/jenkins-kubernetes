pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            // The 'seluser' is the standard user in this image
            // We need to use it to install dependencies and run tests
            args '-u 1000:1000'
        }
    }
    stages {
        stage('Install') {
            steps {
                sh '''
                # The virtual environment is created in the user's home directory
                # or in the workspace. Let's create it in the workspace.
                uv venv .venv --clear
                uv pip install --python .venv -r requirements.txt pytest-html
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                export PYTHONPATH=src
                # Running with uv
                uv run --python .venv pytest --html=report.html
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}