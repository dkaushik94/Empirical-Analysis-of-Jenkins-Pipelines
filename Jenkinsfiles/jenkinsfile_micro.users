pipeline {
  agent any
  stages {
    stage('print') {
      steps {
        echo 'hell world!'
      }
    }
    stage('') {
      steps {
        git(url: 'git@github.com:duorourou/micro.users.git', branch: 'master', changelog: true, credentialsId: 'duorourou')
      }
    }
  }
}