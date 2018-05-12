pipeline {
  agent any
  stages {
    stage('PDNS_sonar') {
      steps {
        echo '------------------- Sonar ------------------------ '
      }
    }
    stage('PDNS_build') {
      steps {
        echo '------------------- PDNS Starting Build ------------------------ '
        echo '----------- PDNS Build Successfully Completed! ----------------- '
      }
    }
    stage('PDNS_Stage_deply') {
      steps {
        echo '------------------- PDNS Starting Deployment on Staging Server ------------------------ '
        echo '---------------- Staging Server Deploymnet Successfully Completed! -------------------- '
      }
    }
    stage('PDNS_RegressionTest') {
      steps {
        echo '----------------------- Regression Test ----------------------------- '
        echo '----------- Regression Test Successfully Completed! ----------------- '
      }
    }
    stage('PDNS_Production') {
      steps {
        echo '--------------- Production Server Deployment -------------------------- '
        echo '---------- Deployment On Production Server Successfully Completed! ------------ '
        echo "The value of parameter: ${params.host}"
      }
    }
  }
}
