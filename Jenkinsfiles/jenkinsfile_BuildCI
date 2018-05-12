pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        svn(url: 'http://srvfr01-0020/repos/IntegrationContinue', changelog: true, poll: true)
      }
    }
  }
}