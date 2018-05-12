#!groovy
/*
The web project is built on the build server, then the dist directory is uploaded to the container
This is different than the API project, which is first uploaded to the image and compiled directly in the image.
*/

node {
  stage('Build') {
    dir("${WORKSPACE}@script") {
      bat 'npm install'
      bat 'node node_modules\\gulp\\bin\\gulp.js clean'
      bat 'node node_modules\\gulp\\bin\\gulp.js build'
    }
  }
    stage('Containerize') {
      dir("${WORKSPACE}@script") {
            bat 'docker build -t toddlamothe/beerdb-web -f Dockerfile.dist .'
        }
    }
    stage('Deploy to Docker Hub') {
      bat 'docker push toddlamothe/beerdb-web'
    }
}
