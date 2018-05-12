#!/usr/bin/env groovy

node {
    git url: 'https://github.com/oyvinder/slack.git'
    def mvnHome = tool 'M3'
    sh "${mvnHome}/bin/mvn test"
    
    step([$class: 'CucumberReportPublisher', jsonReportDirectory: 'target/cucumber', fileIncludePattern: 'cucumber.json'])
}
