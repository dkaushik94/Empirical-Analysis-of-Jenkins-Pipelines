pipeline {
  agent any
  
  stages {
    stage('Build') {
      environment {
        // 'This value is exported to all commands in this stage'
        IMAGE_TAG = "${env.BRANCH_NAME}"
        HOST_BUILD = ":2375"
        IMAGE_NAME = ":5000//:${env.BRANCH_NAME}"
      }
      
      steps {
        echo 'Building...'

        sh 'echo "HI"'
        sh "echo ${env.BUILD_TAG}"
        sh "echo ${env.BRANCH_NAME}"

        sh "/usr/local/bin/docker -H $HOST_BUILD build -t ${IMAGE_NAME} ."
        sh '/usr/local/bin/docker -H $HOST_BUILD push $IMAGE_NAME'
        sh '/usr/local/bin/docker -H $HOST_BUILD rmi $IMAGE_NAME'
      }
    }
  }
}
