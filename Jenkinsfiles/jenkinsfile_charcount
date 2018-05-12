#!/usr/bin/env groovy

pipeline {
    agent any

    tools {
        nodejs "node-8.10.0"
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh 'npm install'
            }
        }
        stage('Test') {
            steps {
                sh 'npm test'
            }
        }
        stage('Bundle') {
            steps {
                sh 'rm *.tgz'
                sh 'npm pack'
                sh 'mv *.tgz bundle.tgz'
            }
        }
        stage('PackAmi') {
            steps {
                sh 'rm packer_*'
                sh 'wget https://releases.hashicorp.com/packer/1.2.1/packer_1.2.1_linux_amd64.zip'
                sh 'gunzip -S .zip packer_1.2.1_linux_amd64.zip'
                sh 'chmod +x packer_1.2.1_linux_amd64'
                sh './packer_1.2.1_linux_amd64 build packerAMI.json'
            }
        }
    }
}