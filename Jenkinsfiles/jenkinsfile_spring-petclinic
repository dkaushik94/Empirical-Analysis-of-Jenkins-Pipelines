pipeline {
    agent {
		label 'rhel'
	}
    
    stages{
        
        stage('Git Clone or Pull'){
            
            steps {
                git 'https://github.com/asquarezone/spring-petclinic.git'
            }
        }
        
        stage('Maven Build'){
            steps{
                sh 'mvn clean install'
            }
        }
        
        stage('Publish'){
            steps{
                archiveArtifacts 'target/springboot-petclinic-1.4.1.jar'
                junit 'target/surefire-reports/*.xml'
                
            }
        }
    }
	post {
        success {
          emailext(
            subject: "${env.JOB_NAME} [${env.BUILD_NUMBER}] Development Promoted to Master",
            body: """<p>'${env.JOB_NAME} [${env.BUILD_NUMBER}]' Development Promoted to Master":</p>
            <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
            to: "shaik.khaja.ibrahim@gmail.com"
          )
        }
   
        failure {
        emailext(
            subject: "${env.JOB_NAME} [${env.BUILD_NUMBER}] Failed!",
            body: """<p>'${env.JOB_NAME} [${env.BUILD_NUMBER}]' Failed!":</p>
            <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
            to: "shaik.khaja.ibrahim@gmail.com"
        )
        }
  }
}