/*Jenkinsfile (Declarative Pipeline)*/
pipeline { 
  agent any
       
  stages {
    stage ('Maven Build') {
    steps { 
       echo "Maven Build Starts and Ends"  
    echo "###########################"
       }
    }
    stage ('Maven Compile') {
    steps { 
       echo "Maven Compile Starts and Ends"
          echo "###########################"    
       }
    }
    stage ('Maven TEst') {
    steps { 
       echo "Maven Test Starts and Ends"
          echo "###########################"
       }
    }
    stage ('Show BuildID') {
    steps { 
       echo "Build is ${env.BUILD_ID}"
          echo "###########################"
       }
    }
   stage ('Set Env Vars...') {
       environment {      
       surname = 'sahoo'
       }
    steps { 
       echo "Show Env Var ...."
    sh 'printenv'
          echo "###########################"
       }
    }   
    }
}