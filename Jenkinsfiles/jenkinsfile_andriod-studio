node {
  def app
    stage('Clone repository') {
      checkout scm
    }
    stage('Deploy image') {
	    sh "chmod +x deploy.sh"
	    sh "./deploy.sh"
    }
}
