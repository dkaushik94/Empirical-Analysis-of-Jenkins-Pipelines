node { 
  //notify start
  //slackSend (color: '#AAAAAA', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
  
  currentBuild.result = "SUCCESS"
  
  try {
    stage('Prepare') {
        checkout scm
        sh 'npm install'
    }
    stage('Build') {
        //sh 'npm run lint'
        sh './node_modules/.bin/ng build'
    }
    stage('Test') {
        //sh './node_modules/.bin/ng test'
        //sh 'npm run serverTest' 
	sh 'xvfb-run -a --server-args="-screen 0 $SCREEN_RES}" npm run e2e'
    }
    stage('Deploy') {
        /* .. snip .. */
    }
    //notify success
    //slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
  } catch (e) {
    currentBuild.result = "FAILED"
    //notify error
    //slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    
    throw e
  }
}
