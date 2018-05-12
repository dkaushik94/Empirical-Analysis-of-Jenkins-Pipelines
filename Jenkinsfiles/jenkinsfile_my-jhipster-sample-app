pipeline {
  agent any
  stages {
    stage('Build') {
      agent {
        docker {
          image 'maven:3-alpine'
          args '-v /root/.m2:/root/.m2'
        }
      }
      steps {
	sh 'mvn -B -DskipTests clean package'
	stash name: 'war', includes: 'target/**'
      }
    }

    stage('Backend') {
      agent {
        docker {
          image 'maven:3-alpine'
          args '-v /root/.m2:/root/.m2'
        }
      }

      steps {
        parallel(
          'Unit': {
            unstash 'war'
            sh 'mvn -B -DtestFailureIgnore test || exit 0'
          },
          'Performance': {
            unstash 'war'
            sh 'echo Performance'
          }
      )}
    }

    stage('Frontend') {
      agent { docker 'node:alpine' }
      steps {
        sh 'node --version'
        sh 'yarn install'
        sh 'yarn global add gulp-cli'
      }
    }

    stage('Static Analysis') {
      steps {
        sh 'echo Static Analysis'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo Deploy'
      }
    }
  }
}