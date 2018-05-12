pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'echo hello'
      }
    }
  }
  environment {
    prod = '1'
    dev = '0'
  }
}