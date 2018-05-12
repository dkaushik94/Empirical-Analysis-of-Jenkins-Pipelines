pipeline {
agent any
stages {


stage('Build') {
steps {
sh 'ant -f build.xml -v'
echo 'Building..'
}
}

 stage('Unit Tests') {
        steps {
            sh 'ant -f test.xml -v'
            junit 'reports/result.xml'
                }
                        }

}
post {
	always {
        
          archiveArtifacts artifacts: 'dist/*.jar', fingerprint: true
        }
      }
    }

