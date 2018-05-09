post  {
            x = 25
            stage ('text') {
                y = 35
            }

        z = 45
        c = 22
        always {
                mailTo: build_results_watch_list@jenkins.com
                gradle clean
                xcode build
            }

        success ('deploy') {
                ./gradlew build test assemble
                jacoco gather-coverage-result
            }
        
        stage ('test') {
            gradle test
        }
}

parallel {
                stage('Unit Test') {
                    steps {
                        mvn 'test'
                    }
                }
                stage('Integration Test') {
                    steps {
                        mvn 'verify -DskipUnitTests -Parq-wildfly-swarm '
                    }
                }
            }
