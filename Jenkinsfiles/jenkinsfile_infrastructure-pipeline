properties([pipelineTriggers([githubPush()])])
node('linux') {
    git url: 'https://github.com/tyetter01/infrastructure-pipeline/blob/master/Jenkinsfile.git', branch: 'master'
    stage('Test') {
        sh "env"
    }
}
