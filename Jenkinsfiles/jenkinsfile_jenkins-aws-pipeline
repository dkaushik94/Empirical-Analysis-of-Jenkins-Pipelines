#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh './script/test'
            }
        }
        stage('Deploy') {
           steps {
               echo 'Deploying....'
               sh './script/deploy'
             }
        }
    }
}
