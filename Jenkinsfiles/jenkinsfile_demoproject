pipeline {
    agent any

    // Global environment vars
    environment {
        COMMIT_ID = 'XXX'
    }

    // Pipeline stages
    stages {
        stage('Build') {
            steps {
                echo '''All prerequisite reside here..
                say,
                - do *-lint/style check
                - compile the app
                - version tagging etc.
                '''
            }
        }
        stage('Test') {
            steps {
                sh './tests/unit_tests.sh'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                ansiblePlaybook(playbook: 'deploy/deploy.yml', colorized: true)
            }
        }
    }

    // TODO: post Jenkins job
    post {
        always {
            echo 'clean up workspace'
            deleteDir()
        }
        success {
            echo 'I succeeeded!'
            slackSend channel: '#wcdeploy',
                      color: 'good',
                      message: "The pipeline ${currentBuild.fullDisplayName} completed successfully."
        }
        failure {
            echo 'I failed :('
            slackSend channel: '#wcdeploy',
                      color: 'bad',
                      message: "The pipeline ${currentBuild.fullDisplayName} failed."
        }
    }

}
