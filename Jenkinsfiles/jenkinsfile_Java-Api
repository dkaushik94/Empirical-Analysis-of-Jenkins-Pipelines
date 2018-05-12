node {

    stage('Slack started') {
    slackSend channel: "#northcoders-java", message: "TvsApp started building"
   }

   stage('Preparation') {
      git 'https://github.com/jonsey247/Java-Api.git'
   }
   stage('Clean') {
      sh "mvn -Dmaven.test.failure.ignore clean"
   }
   stage('Package') {
      sh "mvn -Dmaven.test.failure.ignore package"
   }

   stage('Docker Build') {
       sh "docker build -t mytvapp ."
   }

   stage('Stop app') {
       sh "docker stop mytvapp || true"
       sh "docker rm mytvapp || true"
   }

   stage('Docker Deploy') {
       sh "docker run -d --name mytvapp -p 8081:8080 mytvapp"
   }
}