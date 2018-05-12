pipeline {
    agent { any 'maven:3.3.3' }
    stages {
        stage('build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('deploy') {
            steps {
                sh 'mvn spring-boot:run&'
            }
        }
    }
}
