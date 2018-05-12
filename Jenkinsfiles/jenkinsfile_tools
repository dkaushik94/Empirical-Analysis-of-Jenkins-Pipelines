pipeline {
    agent {
        node {label 'master' }
    }
stages {
stage ('git clone') {
    steps {
        checkout poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/buildscripts']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'CleanBeforeCheckout']], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'e2a65016-6fd8-418f-92c3-eb9400d734f3', url: 'http://snagaraja@bitbucket.cambridgefx.com:7990/scm/c/code.git']]]
}
}
stage ('build') {
    steps {
    bat '''cd Camtrade.Net\\
    build.cmd'''
}
}

stage ('archive artifact') {
    steps {
        archiveArtifacts '*/*.zip'
    }
}
stage ('upload artifact') {
    steps {
        bat '''cd Camtrade.Net\\
            deploy.cmd'''
    }
}
stage ('post build task') {
    steps {
        bat 'git log -n 2'
    }
}
}
}

