node {
stage('SCM') {
git 'https://github.com/padeoe/TestJenkins.git/'
}
stage('QA') {
bat 'sonar-scanner'
}
stage('build') {
def mvnHome = tool 'M3'
bat "${mvnHome}/bin/mvn -B clean package"
}
stage('deploy') {
bat "docker stop my"
bat "docker rm my"
bat "docker run --name my -p 11111:8080 -d tomcat"
bat "docker cp target/test_project-1.0-SNAPSHOT.jar my:/usr/local/tomcat/webapps"

}
stage('results') {
archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
}
}