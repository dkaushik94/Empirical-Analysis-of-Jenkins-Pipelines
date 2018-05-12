pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        parallel(
          "Build": {
            echo 'Build'
            sleep 10
            
          },
          "Build_2": {
            zip(zipFile: 'build001.zip', archive: true)
            
          }
        )
      }
    }
    stage('Test') {
      steps {
        parallel(
          "Test": {
            echo 'Test'
            
          },
          "Test_2": {
            sleep 40
            
          }
        )
      }
    }
    stage('Deploy') {
      steps {
        sleep 4
      }
    }
  }
}