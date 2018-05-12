node {
    currentStatus = "SUCCESS"
    try {
        stage ("Check docker") {
            sh 'docker ps -a'
            echo "check docker ok"
        }
        stage ("Checkout SCM") {

            checkout scm
            echo "checkout scm ok"
        }
        stage ("sbt-test") {
            sh "java -Dsbt.log.noformat=true -jar /jenkins/tools/org.jvnet.hudson.plugins.SbtPluginBuilder_SbtInstallation/sbt/bin/sbt-launch.jar test"
            echo "sbt-test ok"
        }
        stage ("sbt-assembly") {
            sh "java -Dsbt.log.noformat=true -jar /jenkins/tools/org.jvnet.hudson.plugins.SbtPluginBuilder_SbtInstallation/sbt/bin/sbt-launch.jar assembly"
            echo "sbt-assembly ok."
        }
        stage ("Archive Artifact") {
            archiveArtifacts '**/*.jar, Dockerfile'
            sh "cp ${WORKSPACE}/target/scala-2.11/hello-scala-assembly-1.1.jar ${WORKSPACE}/"

            echo "Archive Artifact ok."
        }
        stage ("Docker Image")  {
            withDockerRegistry([credentialsId: '9ccdbfb5-e443-4e49-aa0e-bfad0415f91f', url: 'https://index.docker.io/v1/']) {
                stage "build"
                    def app = docker.build('busayr/hello-scala:${BUILD_NUMBER}', '.')

                stage "publish"
                    app.push()
            }
        }

    } catch ( err ) {
        currentStatus = "FAILED"
        echo currentStatus
    }
}

