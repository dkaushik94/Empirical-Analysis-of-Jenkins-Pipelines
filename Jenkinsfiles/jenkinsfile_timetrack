node('nodejs') {
    dir('build') {
        stage('checkout') {
            checkout scm
        }

        stage('npm install') {
            sh "npm install --ignore-scripts"
        }

        stage('build') {
            sh "make"
        }
    }
    cleanWs()
}