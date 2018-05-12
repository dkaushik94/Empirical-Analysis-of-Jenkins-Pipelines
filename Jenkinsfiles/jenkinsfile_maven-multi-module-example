pipeline {
    agent any
    tools { 
        maven 'Maven 3.5.0' 
        jdk 'jdk8' 
    }
    stages {
        stage ('Initialize') {
            steps {
                sh '''
                    export JAVA_HOME=`/usr/libexec/java_home`
                    echo "PATH = ${PATH}"
                    echo "M2_HOME = ${M2_HOME}"
                ''' 
            }
        }
        stage ('SCM') {
            steps {
                git credentialsId: 'github', poll: false, url: 'https://github.com/bradflood/maven-multi-module-example'
            }
        }
        stage ('Build') {
            steps {
                sh 'mvn -Dmaven.test.failure.ignore=true install' 
            }
            post {
                success {
                    junit 'target/surefire-reports/**/*.xml' 
                }
            }
        }
    }
}