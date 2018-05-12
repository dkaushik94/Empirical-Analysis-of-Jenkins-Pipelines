pipeline{
    agent any
	
	stages {
	   stage ('Compile stage'){
	     steps {
		 
	      withMaven(maven : 'Maven350') {
		  bat 'mvn clean compile'
				}
			}
		  }
		stage ('Testing Stage') {
		  steps {
		withMaven(maven : 'Maven350') {
		  bat 'mvn test'		 }
		}
		}
	}
	}
