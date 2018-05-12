pipeline {
  agent any
  stages {
    stage('checkout') {
      steps {
        git(url: 'https://code.aliyun.com/tansun/itom-fe.git', branch: 'dev', changelog: true, credentialsId: 'd2803c4b-f3cc-4137-8df0-d597cab09606')
      }
    }
  }
}