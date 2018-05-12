// https://github.com/jenkinsci/pipeline-plugin/blob/master/TUTORIAL.md
//
node {
  checkout scm

  env.PATH = "${tool 'Maven3'}/bin:${env.PATH}"

  stage 'Package'
  sh 'mvn clean package -DskipTests'


  stage 'Create Docker Image'
  def image = docker.build("odilontalk/docker-jenkins-pipeline:${env.BUILD_NUMBER}")

  stage 'Run Application'
  try {
    // Run application using Docker image
    // sh "docker run odilontalk/docker-jenkins-pipeline:${env.BUILD_NUMBER}"
  } catch (error) {
    //
  } finally {
    // Stop and remove container here
  }


  stage 'Run Integration Tests'
  try {
    // Run integration tests
    sh "mvn test"
  } catch (error) {
    //
  } finally {
    junit '**/target/surefire-reports/*.xml'
  }

  stage 'Push Docker image'
  docker.withRegistry("http://localhost:5000") {
    image.push()
  }
}