pipeline { 
	agent any
	stages { 
		stage("Compile Stage") { 
			steps { 
				withMaven(maven : 'mvn') { 
					sh 'mvn clean compile' 
				}
			}
		}
		stage("Testing Stage") { 
			steps { 
				withMaven(maven : 'mvn') { 
					sh 'mvn test' 
				}
			}
		}
		stage("Deployment Stage") { 
			steps { 
				withMaven(maven : 'mvn') { 
					sh 'mvn install'
				}
			}
		}
	
	}

}
