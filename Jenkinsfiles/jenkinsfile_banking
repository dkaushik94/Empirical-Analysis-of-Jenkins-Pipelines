pipeline {
  agent none
  stages {
stage('Docker Build') {
      agent any
      steps {
        sh 'docker build -t ubuntu_nginx:latest .'
      }
    }
stage('Docker Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'Dockerhub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} --password-stdin ${env.dockerHubPassword}"
          sh 'docker push ubuntu_nginx:latest'
        }
      }
    } 
  }
}
