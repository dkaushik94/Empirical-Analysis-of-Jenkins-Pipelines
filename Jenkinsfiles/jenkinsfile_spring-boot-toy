#!/usr/bin/env groovy
currentBuild.displayName = "${env.BUILD_NUMBER}:mario/gs-spring-boot-docker"

parameters {
    buildDiscarder(logRotator(numToKeepStr:'15'))
}

// properties(
//   [
//     // Make this a parameterized build.
//       [$class: 'jenkins.model.BuildDiscarderProperty',
//       strategy: [$class: 'LogRotator', numToKeepStr: '15', artifactNumToKeepStr: '15']
//     ],
//     disableConcurrentBuilds(),
//   ]
// )

def deployEnv = ''

node('docker_java8') {
  docker.withRegistry('https://903480711441.dkr.ecr.us-west-2.amazonaws.com', 'ecr:us-west-2:ci') {

    switch(env.JOB_BASE_NAME) {
      case ~/^dev.*$/:
        deployEnv = 'dev'
      break;
      default: 
        error 'nothing to build. make sure job name starts with env name. env is dev,qa,prod'
    }
    
    stage('Checkout') {
      
      checkout scm
      pom = readMavenPom file: 'pom.xml'

    }

    stage('Build') {
      sh "mvn clean package"
  
    }
    
    stage('Push') {

      sh "docker tag 903480711441.dkr.ecr.us-west-2.amazonaws.com/mario/gs-spring-boot-docker:${pom.version} 903480711441.dkr.ecr.us-west-2.amazonaws.com/mario/gs-spring-boot-docker:${pom.version}-${env.BUILD_NUMBER}"
      sh "docker push 903480711441.dkr.ecr.us-west-2.amazonaws.com/mario/gs-spring-boot-docker:${pom.version}-${env.BUILD_NUMBER}"
      sh "docker tag 903480711441.dkr.ecr.us-west-2.amazonaws.com/mario/gs-spring-boot-docker:${pom.version}-${env.BUILD_NUMBER} 903480711441.dkr.ecr.us-west-2.amazonaws.com/mario/gs-spring-boot-docker:latest"
      sh "docker push 903480711441.dkr.ecr.us-west-2.amazonaws.com/mario/gs-spring-boot-docker:latest"
    
    }

    build = "${env.BUILD_NUMBER}"
    version = "${pom.version}"
    build job: "${deployEnv}-mario-deploy", parameters: [[$class: 'StringParameterValue', name: 'buildNumber', value: build], [$class: 'StringParameterValue', name: 'version', value: version]], propagate: false 
  }
}
