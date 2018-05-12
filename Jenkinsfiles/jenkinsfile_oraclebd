pipeline {
    stages {
        stage('Build Oracle Docker Images') {
            steps {
                sh """#!/bin/bash
                set -exuo pipefail
                mkdir vijayDB/
                cd vijayDB/
                git clone 'https://github.com/oracle/docker-images.git'
                """
            }
        }
    }
}   
