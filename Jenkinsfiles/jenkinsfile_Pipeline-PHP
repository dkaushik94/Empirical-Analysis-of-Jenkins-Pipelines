node {
    stage("Build") {
        echo "building appx"
        openshiftBuild buildConfig: "appx", showBuildLogs: "true", namespace: "appx-dev"
    }
    stage("Test") {
        openshiftTag srcStream: 'appx', srcTag: 'latest', destinationStream: 'appx', destinationTag: 'TESTready', namespace: "appx-dev"
        openshiftVerifyDeployment deploymentConfig: 'appx', namespace: "appx-test"
    }
    stage("Approval") {
        input "Go alive with application?"
    }
    stage("Go Live") {
        openshiftTag srcStream: 'appx', srcTag: 'latest', destinationStream: 'appx', destinationTag: 'PRODready', namespace: "appx-dev"
        openshiftVerifyDeployment deploymentConfig: 'appx', namespace: "appx-prod"
    }
}
