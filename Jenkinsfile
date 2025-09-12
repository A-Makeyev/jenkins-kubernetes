pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            // Keep this for security! It's good practice.
            args '-u 1000:1000'
        }
    }
    stages {
        stage('Install Dependencies') { // Renamed for clarity
            steps {
                sh '''
                # Create a virtual environment in the local workspace directory
                python3 -m venv .venv

                # Activate the virtual environment and install requirements into it
                source .venv/bin/activate
                pip install -r requirements.txt pytest-html
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                # Activate the virtual environment to use the installed packages
                source .venv/bin/activate
                
                export PYTHONPATH=src
                pytest --html=report.html
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