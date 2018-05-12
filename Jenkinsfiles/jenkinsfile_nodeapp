#!/usr/bin/env groovy
pipeline{
    agent{
        docker {
            ////Run the Docker image and create Docker Container to perform the Pipeline activities
            image 'localhost:5000/sheeteshkumarrath/nodeimage:latest'
            args '-u root'
                }
          }    
    stages{
    stage('Build') {      
        steps {
                echo 'Building...'
            //Install NPM
                sh 'npm install'
            //Install Express to run our Node JS APP i.e. 'app.js'
                sh 'npm i --save express'
            //Intall Dev-dependencies ('Supertest, Should & Mocha) to test the app
                sh 'npm i --save-dev supertest should mocha'
            //Make the test file executable under 'Script' folder
                sh 'chmod +x ./script/test'                 
              }
                    }
stage('Run App') {
    //Test can only be perfomed on the running application
   steps {
           echo 'Running the app...' 
       // Run the app
           sh 'node app.js &'
           echo 'App is Running'
          }
                  }        
    stage('Test') { 
        steps { 
            echo 'Testing the app...'
        //Run the executable Test file
            sh './script/test'
            //Can run directly with the following command
            //sh './node_modules/.bin/_mocha ./test/test.js'            
               }
                   }
        //App Terminate is not required as all processes will stop when Docker Container stops running      
    }}
