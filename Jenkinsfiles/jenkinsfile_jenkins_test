#!groovy

node('docker') {
  def golang = docker.image('golang:latest')
  
  stage('Test and static build') {
    parallel 'Test': {
      node('docker') {
        checkout scm
        golang.pull()  // make sure golang image is up-to-date
        golang.inside {
          sh 'go test -v ./...'
        }
      }
    }, 'Static build': {
      node('docker') {
        checkout scm
        golang.pull()  // make sure golang image is up-to-date
        golang.inside {
          sh 'go build -a -installsuffix cgo -o jenkins-test main.go'
        }
        stash includes: 'jenkins-test', name: 'jenkins-test-static'
      }
    }
  }

  def cont = null
  stage('Docker image build') {
    checkout scm
    unstash 'jenkins-test-static'
    if (env.BRANCH_NAME == 'master') {
      tag = 'latest'
    } else {
      tag = env.BRANCH_NAME
    }
    cont = docker.build "camptocamp/jenkins-test:${tag}"
  }

  stage('Test docker image') {
    sh "docker run camptocamp/jenkins-test:${tag}"
  }

  stage('Push to dockerhub') {
    withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub',
        usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD']]) {
      sh 'docker login -u "$USERNAME" -p "$PASSWORD"'
      cont.push()

      versions = load 'versions.groovy'
      versions.pushContainer(cont)

      sh 'rm -rf ~/.docker*'
    }
  }

  stage('Approve deploy') {
    timeout(time: 7, unit: 'DAYS') {
      input message: 'Do you want to deploy?', submitter: 'ops'
    }
  }

  stage('Deploy') {
    rancher = load 'rancher.groovy'

    rancher.withEnvironment('http://rancher.test/abcd', 'rancher-test') {
      sh 'echo "RANCHER_URL=$RANCHER_URL"'
      sh 'echo "RANCHER_ACCESS_KEY=$RANCHER_ACCESS_KEY"'
      sh 'echo "RANCHER_SECRET_KEY=$RANCHER_SECRET_KEY"'

      rancher.composeUp()
    }
  }
}
