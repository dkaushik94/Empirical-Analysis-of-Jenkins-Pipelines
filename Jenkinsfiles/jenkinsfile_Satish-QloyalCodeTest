pipeline {
  agent any
  stages {
    stage('Preparation') {
      steps {
        git 'https://github.com/Satishpnc/SeleniumCucumberWithJava.git'
      }
    }
    stage('Build') {
      steps {
        sh "'${M3}/bin/mvn' -Dmaven.test.failure.ignore clean package"
      }
    }
    stage('Email') {
      steps {
        emailext(body: 'Dummy Message', subject: 'Running Jenkins Test', to: 'satishpnc.cse@gmail.com')
      }
    }
  }
}