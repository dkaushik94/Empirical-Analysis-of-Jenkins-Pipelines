pipeline {
  agent any
  stages {
    stage('REPO-DOWNLOAD') {
      steps {
        git(url: 'https://github.com/versionit/mvnrepo.git', branch: 'master')
      }
    }
    stage('Compile') {
      steps {
        sh 'mvn clean compile package'
      }
    }
    stage('Deploy-Nexus') {
      steps {
        sh 'mvn deploy'
      }
    }
    stage('Deploy-Tomcat') {
      steps {
        sh 'sudo su - javaee7 -c /home/javaee7/deploy.sh'
      }
    }
  }
}