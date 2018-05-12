pipeline {
    agent none
    options {
        timeout(time: 5, unit: 'DAYS')
        disableConcurrentBuilds()
    }
    stages {
        stage('Build') {
            agent any
            steps {
                script {
                    bat "mvn clean package"
                }
            }
        }
        stage('Deploy') {
            agent any
            when { branch 'master' }
            steps {
                script {
                    bat "echo 'Not implemented yet'"
                }
            }
        }

    }
    post {
        changed {
            echo "Changed from failure to success"
        }
        unstable {
            echo "Build is unstable"
        }
        failure {
            echo "Whops, build failed"
        }
        aborted {
            echo "User aborted build"
        }
        success {
            echo "Waddayaknow. Succeeded!"
        }
        always {
            echo "Always show this message"
        }
    }
}