pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build sukses'
      }
    }
    stage('Push') {
      steps {
        echo 'push sukses'
      }
    }
    stage('Test') {
      steps {
        echo 'test'
      }
    }
    stage('Deploy') {
      steps {
        parallel(
          "Deploy Production": {
            echo 'Deploy sukses'
            
          },
          "Deploy Staging": {
            echo 'Deploy staging sukses'
            
          }
        )
      }
    }
  }
}