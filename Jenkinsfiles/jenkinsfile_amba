pipeline {
  agent any
  stages {
    stage('Check for amba') {
      steps {
        sh 'echo \'Hello Amba\''
        timeout(time: 10) {
          retry(count: 3)
        }
        
      }
    }
  }
}