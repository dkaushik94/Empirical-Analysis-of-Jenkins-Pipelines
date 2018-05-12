pipeline {
  agent any

  stages {
    stage('Clean Compile') {
      steps {
        sh 'mvn clean compile -DskipTests'
      }
    }

        stage('Units Tests') {
          steps {
            sh 'mvn clean test'
          }
          post {
            success {
              junit 'target/surefire-reports/*.xml'
            }

          }
        }


    stage('Integration Tests') {
      steps {
        echo 'Jeux Campagne tests d\'intégration'
      }
    }
    stage('Functionnals Tests Phases') {
      parallel {
        stage('NR Tests') {
          steps {
            echo 'Jeux Campagne tests de Non regression'
          }
        }
        stage('Integration Tests') {
          steps {
            echo 'Jeux Campagne tests d\'intégration'
          }
        }
      }
    }

  }
  tools {
    maven 'Maven_3.3.9'
  }
  post {
    always {
        sh 'mvn clean'
    }
  }
  options {
    timeout(time: 30, unit: 'MINUTES')
  }
}