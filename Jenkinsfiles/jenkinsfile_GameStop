pipeline {
  agent any
  stages {
    stage('Dev') {
      steps {
        echo 'This is a test '
      }
    }
    stage('CAB') {
      parallel {
        stage('CAB') {
          steps {
            input(message: 'Please Approve Stuff', submitter: 'tmiles@cloudbees.com', submitterParameter: 'OK')
          }
        }
        stage('INPUT') {
          steps {
            input(message: 'Please Appro0ve', id: 'Approve ', ok: 'GO', submitter: 'tmiles@cloudbees.com')
          }
        }
      }
    }
    stage('Push to production') {
      steps {
        echo 'done'
      }
    }
  }
}