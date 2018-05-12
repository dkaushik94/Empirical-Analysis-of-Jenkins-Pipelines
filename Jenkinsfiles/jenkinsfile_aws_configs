node('linux'){
  
  //step([$class: 'GitHubSetCommitStatusBuilder'])
  
  //Set the rotation of logs and builds
  properties([buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '5', daysToKeepStr: '', numToKeepStr: '5')), pipelineTriggers([[$class: 'PeriodicFolderTrigger', interval: '15m']])])
  
  
  stage('CheckOut Source') {
    checkout scm
  }

  stage('Build') {
    echo "Sample Build Step"
    sh 'zip mybuild.zip  -r . -x *.git*'
  }
  
  stage('Unit Tests') {
    echo "Sample Unit Tests"
  }
  
  stage('Integration Tests') {
    echo "Sample Integration Tests"
  }
  
  stage('publish to s3'){
   step([$class: 'S3BucketPublisher', dontWaitForConcurrentBuildCompletion: false, entries: [[bucket: 'jenkinstest4', excludedFile: '', flatten: false, gzipFiles: false, keepForever: false, managedArtifacts: true, noUploadOnFailure: true, selectedRegion: 'us-west-2', showDirectlyInBrowser: false, sourceFile: 'mybuild.zip', storageClass: 'STANDARD', uploadFromSlave: true, useServerSideEncryption: false]], profileName: 'jenkinstest5', userMetadata: []])
  }
  
  //Return if not master
  if (env.BRANCH_NAME != "master"){
    echo "Is a feature branch, so no need for deployment"
    return
  }
}

//Wait one hour for answer
//Outside of node object to use only a lightweight executor - not a full one
timeout(time: 1, unit: 'HOURS') {
  input 'Deploy to Development?'
}

node('linux'){
  stage ("Development Deployment"){
    
  }
  
  //TODO: Future deploy to QA
  //TODO: Future Run full QA Regression
  //TODO: Future Deploy to Production
}  
  
  
               