pipeline {
    agent { docker 'hashicorp/terraform:full' }

    stages {
        stage('Example AWS thing') {
            steps {
                sh 'terraform --version'
                sh 'cd simple-instance;terraform plan'
            }
        }
    }
}