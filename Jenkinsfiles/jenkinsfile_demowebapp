 node ('linux'){
  stage 'Build and Test'
  env.PATH = "${tool 'Maven 3'}/bin:${env.PATH}"
stage ‘Checkout’  
git url: 'https://github.com/pmisarwala/demowebapp.git'
  sh 'mvn clean package'
 }