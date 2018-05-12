pipeline {
  
  agent any
 
  triggers {
         pollSCM('* * 24 02 *') 
  }

  stages{
   stage ('Run') {
        steps {
            sh 'echo "TODAY IS `date`"'
            sh 'echo `date` > /tmp/jenkins_was_here'
        }
    }
   }
  
   post {
            failure {
                sh 'echo "THE PIPELINE HAS BEEN FAILED"'
            }
   }
 
    
}
