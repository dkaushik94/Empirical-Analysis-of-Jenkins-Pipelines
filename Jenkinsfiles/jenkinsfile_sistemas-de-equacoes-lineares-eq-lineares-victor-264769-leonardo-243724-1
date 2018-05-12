pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'matlab -r "teste_eqs_linear"'
            }
        }
    }
}