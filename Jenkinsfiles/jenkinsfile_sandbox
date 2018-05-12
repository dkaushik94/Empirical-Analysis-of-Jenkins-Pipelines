pipeline {
    agent {
        label 'win-vs2017bt'
    }
    stages {
        stage('Test') {
            steps {
                echo "hello"
            }
        }
    }
    post {
        always {
            pkiDeleteDir()
        }
    }
}
