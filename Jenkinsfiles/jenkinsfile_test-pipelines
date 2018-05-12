#!/usr/bin/env groovy
pipeline {
    agent any
    
    stages {
        stage('Clean and Clone'){
            steps 
            {
                script{
                    cleanWs()
                    sh 'git clone https://github.com/nalbarracin/test-pipelines/ .'
                }
        	}
        }
        stage('Build') {
            steps {
                echo 'Build..'
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..' 
                sh 'mvn test'
            }
        }        
    }
    post{
        always{
            echo "Workspace Clean"
            cleanWs()
        }
    }
}