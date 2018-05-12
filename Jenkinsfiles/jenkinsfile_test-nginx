node {
    def app
    def image_name = "kramarov555/test-nginx"
   
   stage('Build') {
       checkout scm
        app = docker.build(image_name)
       sh('docker images')
    }

   stage('Dockerize') {

         docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("latest")
        }
    }

  stage('Deploy') {
        checkout scm
        sh "bash deploy.sh ${image_name}"
    }



    
   
}
