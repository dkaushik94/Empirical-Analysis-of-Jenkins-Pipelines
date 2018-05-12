pipeline {
	agent any
	tools {
		maven 'apache-maven-3.5.2'
	}
	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
		stage('Build') {
			steps {	
				echo 'Building...'
				sh "mvn clean install"
			}
 		}
		stage('Test') {
			steps {
				echo 'Testing...'
			}
		}
		stage('Deploy') {
			steps {
				echo 'Deploying....'
			}
		}	
	}
}

