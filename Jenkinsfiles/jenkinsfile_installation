pipeline {
  agent any
  stages {
    stage('installation') {
      steps {
        sh 'python2.7 /var/tmp/Nightswatch/deploy/upgrade_machines_sa.py -p $target_cluster --ininame \'/var/lib/jenkins/nightswatch/5.1/config.ini\''
      }
    }
    stage('fragment_cache') {      
        steps {
        build '../Fragment_cache/master'
      }
    } 
    stage('Thumbnail') {      
        steps {
        build '../Thumbnails/master'
      }
    } 
  
  }
 environment {
   target_cluster = '10.65.173.162'
  }
}

