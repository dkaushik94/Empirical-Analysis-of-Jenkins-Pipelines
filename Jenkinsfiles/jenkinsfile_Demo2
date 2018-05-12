pipeline {
    agent any
    stages{
        stage ('init') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'eeec42e6-c7fe-4afd-8225-85247a6e32a7', url: 'https://github.com/tjug/Demo2.git']]])
            }
        }
        stage ('build') {
            steps {
                  sh 'mvn clean package'
                  echo 'Look at me I\'m executing a build step'
            }
        }
        stage ('archive') {
            steps {
                    archiveArtifacts 'target/*.jar'
            }
        }
    }
    post {
        always {
            echo 'I say Good Day Sir!'
        }
    }
}