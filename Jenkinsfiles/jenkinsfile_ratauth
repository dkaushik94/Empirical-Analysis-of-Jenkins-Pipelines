pipeline {
	agent any
	
	stages {
	
//		stage('Checkout') {
//			steps {
//				checkout scm
//			}
//		}
	
		stage('Compile') {
			steps {
				 sh './gradlew clean classes --info'
			}
		}
	
		stage('Test') {
			steps {
				 sh './gradlew cleanTest test --info'
				 junit '**/test-results/test/*.xml'
				 jacoco(classPattern: '**/classes/java/main')
			}
		}	

		stage('Integration test') {
			steps {
				script {
					docker.image('mongo').withRun('-p 27017:27017') { mongo ->
						echo 'Integration tests running ...'
						sh './gradlew cleanIntegrationTest integrationTest --info'
				 		junit '**/test-results/integrationTest/*.xml'
					}
				}
			}	
		}
		
		stage('Build') {
			steps {
				 sh './gradlew build --info'
			}
		}
				
	}
}
