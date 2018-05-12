#!groovy
pipeline {
    
    agent {
        label 'sms-pom-2'
    }
    
    stages {
        stage('Build') {
            steps {
                echo 'Build Stage 1: Deploying docker'
                sh 'docker build -t centos/python-flask .'
                echo 'Build Stage 2: Running docker'
                sh 'docker run -d --rm --name python-flask -p 80:80 centos/python-flask'
         
            }
        }
        stage('Test') {
            steps {
                echo 'This is Test stage...'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'This is Deploy stage...'
                
            }
        }
    }
    
}
