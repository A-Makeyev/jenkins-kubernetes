pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'
            // Use the host's Jenkins user ID inside the container
            args '-u $(id -u):$(id -g)'
        }
    }
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                # This will now work because the user inside the container
                # has the same UID as the owner of the workspace directory.
                python3 -m venv .venv

                # Activate the virtual environment and install requirements
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