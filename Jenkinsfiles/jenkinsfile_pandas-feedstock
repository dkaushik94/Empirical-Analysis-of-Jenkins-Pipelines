pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '.circleci/run_docker_build.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
