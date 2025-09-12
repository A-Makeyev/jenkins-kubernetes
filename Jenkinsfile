pipeline {
    // We run the main pipeline on any available agent
    agent any
    stages {
        stage('Run Tests in Docker') {
            steps {
                // Use a script block for more advanced logic
                script {
                    // Checkout the code first, so it's available for the container
                    checkout scm

                    // Define the Docker image we want to use
                    def myImage = docker.image('selenium/standalone-chrome:latest')
                    
                    // Get the user ID from the host agent and trim whitespace
                    def userID = sh(returnStdout: true, script: 'id -u').trim()
                    def groupID = sh(returnStdout: true, script: 'id -g').trim()

                    // Run the container using the scripted 'inside' syntax
                    // This allows us to build the arguments dynamically
                    myImage.inside("-u ${userID}:${groupID}") {
                        
                        // --- All commands inside this block run inside the container ---

                        echo "--- Installing Dependencies inside container ---"
                        sh '''
                        python3 -m venv .venv
                        source .venv/bin/activate
                        pip install -r requirements.txt pytest-html
                        '''

                        echo "--- Running Tests inside container ---"
                        sh '''
                        source .venv/bin/activate
                        export PYTHONPATH=src
                        pytest --html=report.html
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            // Archive the report generated inside the container
            archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true
        }
    }
}