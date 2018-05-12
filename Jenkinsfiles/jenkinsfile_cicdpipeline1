node {
    stage 'build'
        echo 'Hello World (build)'
        openshiftBuild(namespace: 'insultapp', buildConfig: 'insults', showBuildLogs: 'true')
    stage 'deploy'
        echo 'Hello World (deploy)'
        openshiftDeploy(namespace: 'insultapp', deploymentConfig: 'insults')
}
