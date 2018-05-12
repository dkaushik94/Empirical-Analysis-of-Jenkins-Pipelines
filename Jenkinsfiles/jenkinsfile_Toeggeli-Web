def profiles = [
            integration: [stage: "Integration", namespace: "rch-toeggeli-int", imageStream: "toeggeli-web", imageTag: "latest", buildConfig: "toeggeli-web", deploymentConfig: "toeggeli-web", "replicaCount": "1"],
        ]

        def integration = profiles['integration']


        stage('Build integration') {
            node {
                openshiftBuild(namespace: integration.namespace, buildConfig: integration.buildConfig, showBuildLogs: 'true', waitTime: '3000000')
            }
        }

        stage('Deploy integration') {
            node {
                openshiftDeploy(namespace: integration.namespace,
                        deploymentConfig: integration.deploymentConfig,
                        waitTime: '300000')
            }
        }


        stage('Verify integration deployment') {
            node {
                openshiftVerifyDeployment(namespace: integration.namespace, depCfg: integration.deploymentConfig, replicaCount: integration.replicaCount, verifyReplicaCount: 'true', waitTime: '300000')
            }
        }
