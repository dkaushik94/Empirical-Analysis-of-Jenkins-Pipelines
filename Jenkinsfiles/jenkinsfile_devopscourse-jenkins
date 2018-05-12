node() {
    stage('Build') {
        checkout scm
        sh './gradlew build'
    }
    stage('Test') {
        sh './gradlew test'
    }
}