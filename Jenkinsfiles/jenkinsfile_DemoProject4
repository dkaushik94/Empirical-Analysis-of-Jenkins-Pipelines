pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        git(url: 'https://github.com/PrabhakaranAnnadurai/DemoProject1', branch: 'master')
        archiveArtifacts 'test.txt'
      }
    }
    stage('Publish'){
      steps {
        s3Upload (file:'test.txt',bucket:'prabha-jenkins-artifacts',path:/test/)
      }
    }
  }
}
