node 
{
     stage('Configure')
{ 
	version = '1.0.' + env.BUILD_NUMBER
	currentBuild.displayName = version
}

	stage ('Initialize') 
        {
            
    bat '''
        
        echo "M2_HOME = %M2_HOME%"
        '''
            
        }
		
		

    stage ('Build') 
		    {
            
             bat 'cd NumberGenerator & mvn -B -V -U -e clean package'
            }
             
	   stage ('Test case') 
             {
              junit 'NumberGenerator/target/surefire-reports/*.xml, allowEmptyResults: true'
                        
		     
	   stage ('Archive')
			  {
			  
				archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
			  }
		stage ('Deploy')
			 {
			 sh '''
			 
			 cp NumberGenerator/target/NumberGenerator-1.0-SNAPSHOT.jar D:/Paperboat/jar
			 
			 '''
			 
			 }
     }
	 
	 }
                 
               

           

        
    

