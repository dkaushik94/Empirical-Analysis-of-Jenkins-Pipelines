node {
    stage('SCM') {
        git 'https://github.com/lsySummer/RiskManage.git'
    }
    stage('QA') {
        sh '~/sonar/sonar-scanner-2.8/bin/sonar-scanner'
    }
    stage('build') {
        def mvnHome = tool 'M3'
        sh "${mvnHome}/bin/mvn -B clean package"
    }
    stage('deploy') {
        sh "docker stop risk|| true"
        sh "docker rm risk || true"
        sh "docker run --name risk -p 11112:8080 -d dordoka/tomcat"
        sh "docker cp target/RiskManage.war risk:/opt/tomcat/webapps"
    }
    stage('results') {
        archiveArtifacts artifacts: '**/target/*.war', fingerprint: true
    }
}
