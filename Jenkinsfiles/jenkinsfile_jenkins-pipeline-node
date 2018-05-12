node {
    stage('Initialize') {
        echo 'Initializing...'
        def node = tool name: 'Node-7.4.0', type: 'jenkins.plugins.nodejs.tools.NodeJSInstallation'
        env.PATH = "${node}/bin:${env.PATH}"
    }
    stage('Checkout') {
        echo 'Checking version control...'
        checkout scm
    }
    stage('Build') {
        echo 'Building dependencies...'
        sh 'npm i'
    }
    stage('Test') {
        echo 'Testing...'
        sh 'npm test'
    }
    stage('Publish') {
        echo 'Publishing'
		publishHTML (target: [
			allowMissing: false,
			alwaysLinkToLastBuild: false,
			keepAll: true,
			reportDir: 'coverage/lcov-report',
			reportFiles: 'index.html',
			reportName: "node-pipeline-jenkins"
		])
    }
}
