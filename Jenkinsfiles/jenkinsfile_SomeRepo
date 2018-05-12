pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh '''
                    echo "Starting ..."
                    mvn --version
                    node --version
                    npm --version
                '''
            }
        }
    }
}
