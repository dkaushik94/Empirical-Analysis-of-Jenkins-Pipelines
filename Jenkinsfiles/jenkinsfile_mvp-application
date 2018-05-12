#!groovy

node {

 stage('checkout') {
   checkout scm
 }

 stage('check tools') {
   sh "pwd"
   sh "./gradlew --version"
 }

 stage('clean') {
   sh "./gradlew clean"
 }

 stage('test') {
   sh "./gradlew :web-sandbox:test"
 }

 stage('packaging') {
   sh "./gradlew :web-sandbox:war"
 }

 stage('deploying') {
    sh "./gradlew :web-sandbox:deployTest"
 }
}