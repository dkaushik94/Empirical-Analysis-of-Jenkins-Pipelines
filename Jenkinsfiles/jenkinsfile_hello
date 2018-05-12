pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            echo 'test'
          }
        }
        stage('Build1') {
          steps {
            echo 'Build1'
          }
        }
        stage('Build2') {
          steps {
            echo 'Build2'
          }
        }
      }
    }
    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            echo 'testing'
          }
        }
        stage('another test') {
          steps {
            sh 'echo "another tets"'
          }
        }
      }
    }
    stage('Done') {
      steps {
        echo 'build done'
      }
    }
    stage('test') {
      steps {
        sh 'echo "test"'
      }
    }
  }
}