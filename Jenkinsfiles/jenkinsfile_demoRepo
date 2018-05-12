library 'SharedLibs'
pipeline {
  agent any
  stages {
    stage('Maven') {
      steps {
        echo 'Hello World'
      }
    }
    stage('Shared Lib') {
         steps {
             helloWorld("Jenkins")
         }
    }
    
  }
}
