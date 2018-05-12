#!groovy
node {
   def mvnHome
   checkout scm

   stage('Preparation') {
      mvnHome = tool 'M3'

   }
   stage('Build') {
         job_name = env.JOB_NAME.toLowerCase()
         job_name = job_name.replaceAll(" ","-")
         job_name_slug = job_name.replaceAll("/","_")

         sh "'${mvnHome}/bin/mvn' clean install  -f mybatis/pom.xml"
         sh "ansible-playbook  mybatis/deploy/dev.yml --extra-vars 'job_name=${job_name} slug=${job_name_slug}'"


   }

   stage('Results') {
      archive '**/target/*.jar'
   }

}