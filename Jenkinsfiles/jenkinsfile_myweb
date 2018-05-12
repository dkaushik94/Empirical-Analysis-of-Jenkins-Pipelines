node {
    stage('Checkout') {
        checkout scm
    }
    
	println "Check Out Completed......."
	
	stage ('test'){
		bat(/ gradle.bat test/)
    }
        
    stage ('build'){
		bat(/ gradle.bat build/)
    }
}


 