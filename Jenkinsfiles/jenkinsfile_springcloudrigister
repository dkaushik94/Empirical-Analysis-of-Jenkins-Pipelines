pipeline {
  agent any
  stages {
    stage('checkout') {
      parallel {
        stage('compile') {
          steps {
            git(url: 'https://github.com/linyiming85/springcloudrigister.git', branch: 'master')
            sh 'mvn clean package'
            sh '''cd target
java -jar eureka-0.0.1-SNAPSHOT.jar'''
          }
        }
        stage('') {
          steps {
            git(url: 'https://github.com/linyiming85/configcenter.git', branch: 'master')
            sh 'mvn clean package'
            sh '''cd target
java -jar configserver-0.0.1-SNAPSHOT.jar'''
          }
        }
      }
    }
  }
}