#!/bin/env groovy
//#!/usr/bin/env groovy

import java.lang.*
import java.net.*

def skipStages = false //Skips certain stages - Testing purposes.
def sendSlackUpdates = true //Sending Slack Updates toggle
def buildVersion = ""
def slackMessage = ""
currentBuild.result = 'SUCCESS'


    node() {
        def mvnHome = tool 'maven'
        def workspace = pwd()

        stage('Checkout') {
            checkout scm
        }

        stage('Install + Build') {
            try {
                echo "Building"
                sh "${mvnHome}/bin/mvn  clean install -f ./pom.xml"
            } catch (error) {
                echo "${error}"
                error()
            }
        }
       /* stage('Package') {
            try {
                archiveArtifacts artifacts: '**//*springMVC4-0.1.0-vanilla-SNAPSHOT.war',
                        fingerprint: true
            } catch (error) {
                echo "${error}"
                error()
            }
        }*/
        stage('Unit Testing') {
            try {
                timeout(5) {
                    withSonarQubeEnv('Sonar') {
                        sh "${mvnHome}/bin/mvn org.jacoco:jacoco-maven-plugin:0.7.8:prepare-agent verify -Dno-deploy -f ./SpringMVC4_Git/pom.xml"
                        sh "${mvnHome}/bin/mvn sonar:sonar -Pno-deploy -f ./pom.xml"
                    }
                }
            } catch (error) {
                echo "${error}"
                error()
            }
        }
      /*  def qualityMetrics = ""
        //Quality Metric Stages
        stage('Automated Code Analysis') {
            def reportPage = sh ( script: "curl 'http://sonarqube.amelco.co.uk/api/measures/component?additionalFields=metrics%2Cperiods&componentKey=ats-hkjc%3Aats-hkjc-master&metricKeys=alert_status%2Cquality_gate_details%2Cbugs%2Cnew_bugs%2Creliability_rating%2Cvulnerabilities%2Cnew_vulnerabilities%2Csecurity_rating%2Ccode_smells%2Cnew_code_smells%2Csqale_rating%2Csqale_index%2Cnew_technical_debt%2Ccoverage%2Cnew_coverage%2Cnew_lines_to_cover%2Ctests%2Cduplicated_lines_density%2Cnew_duplicated_lines_density%2Cduplicated_blocks%2Cncloc%2Cncloc_language_distribution%2Cnew_lines' > qualityInfo.json",
                    returnStdout: true )
            qualityMetrics = sh (script: "jq -r '.component.measures[] | select(.metric==\"quality_gate_details\").value | fromjson.conditions[] | select(.metric) | \"->\" + .metric + \": \" + .actual + \" / \" + .error + \" = \" + .level' qualityInfo.json", returnStdout: true )
            echo "Quality Gate Metrics: \n" + qualityMetrics
            if (qualityMetrics.contains("ERROR")) {
                slackMessage = "Build '${buildVersion}' Code Analysis FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' <${env.BUILD_URL}|*LINK*>" + "\n" + qualityMetrics
                qualityMetrics = "Quality Gate FAILED: \n" + qualityMetrics
                currentBuild.result = 'FAILURE'
                currentBuild.description = qualityMetrics
                error()
            } else {
                slackMessage = slackMessage + "\n" + qualityMetrics
                qualityMetrics = "Quality Gate PASSED: \n" + qualityMetrics
                currentBuild.description = qualityMetrics
            }
        }
        if (!skipStages) {
            stage('Regression Testing')
                    {
                        dir('../Jenkins_Integration_Testing')
                                {
                                    try {

                                        checkout([$class                : 'SubversionSCM',
                                                  additionalCredentials : [],
                                                  excludedCommitMessages: '',
                                                  excludedRegions       : '',
                                                  excludedRevprop       : '',
                                                  excludedUsers         : '',
                                                  filterChangelog       : false,
                                                  ignoreDirPropChanges  : false,
                                                  includedRegions       : '',
                                                  locations             : [[credentialsId        : '629d031d-661a-4223-b486-4d6c3c2d4d7a',
                                                                            depthOption          : 'infinity',
                                                                            ignoreExternalsOption: true,
                                                                            local                : 'cable_branch',
                                                                            remote               : 'https://svn.amelco.co.uk/repos/ats-repo/proj/ats-automated-functional-tests/readyAPI/hkjc/']],
                                                  workspaceUpdater      : [$class: 'UpdateUpdater']])
                                        sh "${mvnHome}/bin/mvn install -e -DtestSuiteName= -DtestCaseName= -DtestEnvironment=hkjc_hkjc-test1 -fcable_branch/pom.xml"
                                    } catch (error) {
                                        echo "${error}"
                                        slackMessage = "Build '${buildVersion}' Failed at Regression Testing stage: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' <${env.BUILD_URL}|*LINK*>"
                                        currentBuild.result = 'FAILURE'
                                        error()
                                    } finally {
                                        System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "default-src 'self'; style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline';")
                                        publishHTML([allowMissing: true, alwaysLinkToLastBuild: false, keepAll: true, reportDir: 'cable_branch/target/soapui', reportFiles: 'index.html', reportName: 'RegressionTestingResults'])
                                    }
                                }
                    }
        }
    }


*/
/*
try{
    node (){
        stage('Checkout'){
            try{
                checkout scm
                git url :'https://github.com/aschalewat/GUIChat1.git/'
            }catch (error){
                echo "${error}"
            }
        }
        stage('build'){
            echo 'Building the code'
        }
        stage('QA'){
            echo 'Test is complete'
        }
        stage('PRODUCTION'){
            echo 'Product is ready'
        }
    }
}finally {
    echo "Done!"
}
*/
/*
node {
    def branch = env.BRANCH_NAME
    echo "the new branch ${branch}"
    stage('DEV'){
        echo 'Hello World1'
    }
    stage('QA'){
        echo 'Test is complete'
    }
    stage('PRODUCTION'){
        echo 'Product is ready'
    }*/
}