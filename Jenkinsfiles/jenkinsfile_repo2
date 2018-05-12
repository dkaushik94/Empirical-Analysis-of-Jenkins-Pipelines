Pipeline {
   agent any

   stages {
      
      stage ('Compile Stage') {
          steps {
	     withMaven(Maven : 'maven-3.5.2') {
                  sh 'mvn clean compile'
	     }

        }
   
     }
     stage ('Testing Stage') {
        steps {
           withMaven(Maven : 'maven-3.5.2'){
	      sh 'mvn test'
	   }

	}
     }
     stage ('Deployment Stage') {
         steps {
           withMaven (Maven : 'maven-3.5.2'){
               sh 'mvn deploy'
	   }

	   
	  }
	 
	 }

     }


}


