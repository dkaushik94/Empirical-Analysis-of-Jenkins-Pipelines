pipeline {
  agent {
    docker {
      image 'frolvlad/alpine-oraclejdk8:slim'
      args '-p 8000:8000'
    }
    
  }
  stages {
    stage('Move') {
      steps {
        sh 'cd AuthService'
      }
    }
    stage('Build') {
      steps {
        sh 'mvn clean package'
      }
    }
  }
}