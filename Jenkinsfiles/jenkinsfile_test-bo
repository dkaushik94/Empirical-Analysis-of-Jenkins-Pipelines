pipeline {
  agent any
  stages {
    stage('stage one') {
      steps {
        echo 'step one '
        sh '''cd /home/tibco/tibco/tra/5.10/bin
./AppManage -start -app Log -domain localDomain -user admin -pw admin
'''
      }
    }
    stage('stage two') {
      steps {
        parallel(
          "stage two": {
            echo 'step two'
            sh 'ls'
            
          },
          "stage three": {
            echo 'step three'
            sh 'pwd'
            
          }
        )
      }
    }
  }
}
