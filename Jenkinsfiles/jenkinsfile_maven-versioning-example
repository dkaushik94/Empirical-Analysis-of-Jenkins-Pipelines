node {
  jdk = tool name: 'jdk-8'
  env.JAVA_HOME = "${jdk}"
  env.PATH = "${tool 'maven-3.3.9'}/bin:${env.PATH}"
  
  stage 'Checkout'
  checkout scm
  
  stage 'Build & Test'
  sh 'mvn clean package -Drevision=$BUILD_ID'
}
