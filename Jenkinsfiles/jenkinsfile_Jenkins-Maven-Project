pipeline {
  agent none
  options {
    skipDefaultCheckout true
  }
  tools {
    maven 'maven-3.5.2'
  }
  stages {
    stage("Checking source code for SCM"){
        agent {
          label 'master'
        }
        steps {
          checkout([
               $class: 'GitSCM',
               branches: [[name: '*/devops_1_maven']],
               doGenerateSubmoduleConfigurations: false,
               extensions: [[$class: 'LocalBranch', localBranch: "**"]],
               submoduleCfg: [],
               userRemoteConfigs: [[credentialsId: '736051fa-c90e-4823-8b1b-cc861e19f951',
               url: 'git@gitlab.rabat.sqli.com:DEVOPS_TRAINING/DEVOPS_TRAINING.git']]])
        }
      }

    stage('Build') {
      agent {
        label 'master'
      }
      steps {
        sh "mvn clean compile"
      }

    }

    stage('Unit Tests') {
      agent {
        label 'master'
      }
      steps {
        sh 'mvn surefire:test'
        sh "mvn surefire-report:report -DoutputName=report-${env.BUILD_NUMBER}"
      }
    }
    stage("Temp"){
      agent {
        label 'master'
      }
      steps{
        sh "env"
      }
    }

    stage('Packaging') {
      agent {
        label 'master'
      }
      steps {
        sh "mvn clean install"
      }
      post {
        success {
          sh "cp target/*.jar target/rectangle_${env.BUILD_NUMBER}.jar"
          archiveArtifacts artifacts: "target/*.jar", fingerprint: true
        }
      }
    }

     stage('Deploying to Snapshots') {
      agent {
        label 'master'
      }
      steps {
        sh "mvn deploy"
        sh "cp target/*.jar /var/www/html/rectangles/all/"
      }
    }

     stage('Deploying to Releases') {
      agent {
        label 'master'
      }
      steps {
        sh "mvn release:clean release:prepare release:perform"
      }
    }

     stage("Functional Testing") {
      agent {
        label 'Slave1'
      }
      steps {
        sh "wget http://192.168.56.100/rectangles/all/rectangle_${env.BUILD_NUMBER}.jar"
        sh "java -jar rectangle_${env.BUILD_NUMBER}.jar 3 4"
      }
    }

  }
}

