pipeline {
  agent { dockerfile true }

  stages {
    stage('Cleanup') {
      steps {
        sh 'rm -rf squid'
        sh 'rm *.deb'
      }
    }

    stage('Build') {
      steps {
        sh 'git clone --depth 3 -b master git@github.com:gideao/squid.git'
        sh 'cd squid && dpkg-buildpackage -us -uc -b'
      }
    }

    stage('Deploy') {
      environment { 
        GITHUB_TOKEN = credentials('github-token')
      }
      
      steps {
        sh '/release.sh'
      }
    }
  }
}
