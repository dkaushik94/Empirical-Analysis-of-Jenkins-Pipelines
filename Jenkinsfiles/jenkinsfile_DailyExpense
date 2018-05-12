pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building'
            }
        }
      stage('Test') {
            steps {
                echo 'Running Unit Test'
            }
        }
      stage('Upload Artifacts') {
            steps {
                echo 'Upload Artifacts to Nexus'
            }
        }
      stage('Deploy') {
            steps {
                echo 'Stop App with port 5000'
                echo 'Deploy App with port 5000'
            }
        }
    }
}