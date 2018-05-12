#!/usr/bin/env groovy

import hudson.model.*
import hudson.EnvVars
//import groovy.json.JsonSlurperClassic
//import groovy.json.JsonBuilder
//import groovy.json.JsonOutput
//import java.net.URL
//def my_env = System.getenv()
//def my_build_number = Job.getVariable("BUILD_NUMBER")
def myVar = build.getEnvironment(listener).get('BUILD_NUMBER')


@Library('jenkins_lib') _

def start_message = "Started ${env.JOB_NAME} <${env.BUILD_URL}|#${env.BUILD_NUMBER}>" + "\n" +
            "<${env.RUN_DISPLAY_URL}|Pipeline details>" + "\n" +
            "<${env.JOB_DISPLAY_URL}|Pipeline activity>"          

pipeline {
    agent any
    environment {
        MY_VAR = 'DEFINE_MY_ENV_VARIABLE_HERE'
        SLACK_SWITCH = 'OFF' // ON or OFF
    }
    stages {
/*        if(env.SLACK_SWITCH=="ON") {
            stage('To send or not to send to slack') {
                steps{
                    sendToSlack('Zero stage')
                }
            }
        }
*/
        stage('Checkout') {
            steps {
                script {
                    //?
                }
                //echo 'Job.getVariable("BUILD_NUMBER")'
                //print my_build_number
                echo 'print myVar:'
                print myVar
                sendToSlack()
                sendToSlack('Checkout stage', '#devops', '#ABCDEF')
                checkout(
                    [
                        $class: 'GitSCM', 
                        branches: [[name: '*/master']], 
                        doGenerateSubmoduleConfigurations: false, 
                        extensions: [], 
                        submoduleCfg: [], 
                        userRemoteConfigs: [
                            [credentialsId: 'f51f83e4-f521-40fb-8aa6-6fce2ddf22d8', 
                            url: 'git@github.com:vensder/pipeline_test.git']
                        ]
                    ]
                )
                echo "Env vars is: ${env.NODE_NAME}, ${env.BRANCH_NAME}, ${env.GIT_URL}"
                sh 'printenv'
                sh 'printenv | wc -l'
            }
        }
        stage('Build') {
            steps {
                slackSend (
                    channel: '#devops', 
                    color: '#439FE0', 
                    message: start_message, 
                    teamDomain: slackParams.teamDomain, 
                    tokenCredentialId: slackParams.tokenCredentialId
                )
                ansiColor('xterm') {
                    sh '''#!/usr/bin/env bash
ls -la /var/jenkins_home/logs/audit/
cat /var/jenkins_home/logs/audit/audit-*.log
'''
                }
            }
        }
    }
    post {
        always {
            sh 'printenv'
            sh 'printenv | wc -l'
        }
        success {
            sendToSlack ('Pipeline finished successfully','#devops', 'good')
        }
        failure {
            slackSend (
                channel: '#devops', 
                color: 'danger', 
                message: "Pipline failed", 
                teamDomain: slackParams.teamDomain, 
                tokenCredentialId: slackParams.tokenCredentialId
            )
        }
    }
}





