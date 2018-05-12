def build = "${env.BRANCH_NAME}".replace('-', '').replace('/', '').replace('_','')

pipeline {
    agent {
        docker {
            image 'htplbc/node-serverless:latest'
            args '-u root:root -v $HOME/workspace/serverless-multi-pipeline:/serverless-multi-pipeline'
        }
    }
    options {
      buildDiscarder(logRotator(numToKeepStr:'5'))
      timeout(time: 20, unit: 'MINUTES')
    }

    stages {
        stage('Environment Version') {
          steps {
            echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
            sh 'node --version'
            sh 'serverless --version'
          }
        }
        stage('serverless deployment'){
          steps{
            withAWS(credentials:'AWS_CTI_DEV_CREDS') {
              sh "serverless deploy -s ${build}"
            }
          }
        }
    }
    post {
        success {
            echo 'Do something when it is successful'
        }
        failure {
            echo 'Do something when it is failed'
        }
    }
}
