pipeline {
  agent {
    node {
      label 'master'
    }
    
  }
  stages {
    stage('Stage1') {
      steps {
        powershell 'write-host "Test"'
      }
    }
    stage('stage2') {
      steps {
        bat 'dir'
      }
    }
  }
}