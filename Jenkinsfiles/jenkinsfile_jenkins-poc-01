pipeline {
    agent none

    stages {
        stage ('First') {
            agent any
            steps {
                echo "First dummy stage"
            }
        }
        stage ('Input') {
            agent none
            steps {
                script {
                    myStage = input message: 'What stage do you want to run now?', parameters: [choice(choices: 'Stage1\nStage2\nStage3', description: '', name: 'Stage')]
                }
                echo myStage
            }
        }
stage('Tests') {
      parallel {
        stage('Stage1') {
            when {
                expression { myStage == 'Stage1' }
            }
            steps {
                echo "Running Stage1"
            }
        }

        stage('Stage2') {
            when {
                expression { myStage == 'Stage2' }
            }
            steps {
                echo "Running Stage2"
            }
        }

        stage('Stage3') {
            when {
                expression { myStage == 'Stage3' }
            }
            steps {
                echo "Running Stage3"
            }
        }
      }
    }
        

    }
}
