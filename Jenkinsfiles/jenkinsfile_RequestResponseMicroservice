pipeline {
    agent any
	

    stages {

        stage ('Workspace refresh') {
            steps {
                git 'https://github.com/SwatyGupta/RequestResponseMicroservice'
            }
        }

        stage ('Compile') {
          steps {
            sh 'mvn clean compile'
          }
        }

        stage ('Test') {
          steps{
            sh 'mvn test'
          }
        }

        stage ('Package') {
          steps{
            sh 'mvn package -Dmaven.test.skip=true'
          }
        }

    }
}