node {
    checkout scm
    sh 'mvn clean install'
    junit 'target/surefire-reports/**/*.xml'
}