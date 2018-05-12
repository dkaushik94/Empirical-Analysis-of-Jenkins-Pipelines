node {
  def nodeHome = "/home/Applications/IBM/node6.11.5/node/bin/node"

  echo "Starting UI build..."
  echo "currently logged in as:"
  sh "whoami"
  echo "DeployId env var is ${env.DEPLOY_ID}"
}

pipeline {
  agent {
    docker {
      image 'node:6-alpine'
      args '-p 3000:3000'
    }
  }

  environment {
    DEPLOY_ID = "${env.DeployId}"
    DEPLOY_PASSWORD = "${env.DeployPassword}"
    PATH = "${nodeHome}/bin:${env.PATH}"
  }

  stages {
    stage('Init') {
      steps {
        echo "Initializing..."
        echo "${BUILD_ID}"
        echo "${branchName}"
        echo "node version:"
        sh "node -v"
        sh "npm uninstall bower -g"
        sh "npm install bower -g"
      }
    }
    stage('buildAndDeploy') {
      steps {
        echo "Building and deploying"
        sh "pwd && ls -al"
        sh "sh ./Bluemix-Whisk-UI/myscript.sh"
        sh "rm -Rf ./*"
        sh "pwd && ls -al"
      }
    }
  }
}
