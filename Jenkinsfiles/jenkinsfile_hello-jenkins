pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh './script/test'
            }
        }
        stage('Deploy') {
            steps {
                sh './script/deploy'
            }
        }
    }
}
