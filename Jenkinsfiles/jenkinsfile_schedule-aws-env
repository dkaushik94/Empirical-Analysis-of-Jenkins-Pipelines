node {
    stage ('checkout'){
         checkout([$class: 'GitSCM',
             branches: [[name: '*/master']],
             doGenerateSubmoduleConfigurations: false,
             extensions: [
                 [$class: 'CleanBeforeCheckout'],
                 [$class: 'CloneOption', noTags: true, reference: '', shallow: true]
             ],
             submoduleCfg: [],
             userRemoteConfigs: [[url: 'https://github.com/taykey/schedule-aws-env.git']]
         ])

    }
    stage('Prepare') {
        echo 'Preparing environment..'
        if (isUnix()) {
            sh """
                virtualenv -p python3.6 venv
                . venv/bin/activate
                pip install pybuilder
                pyb install_dependencies
            """
        }
    }
    stage('Build') {
        echo 'Building..'
        sh """
                . venv/bin/activate
                pyb publish
            """
    }
    stage('Test') {
        echo 'Testing..'
         sh """
                . venv/bin/activate
                pyb run_unit_tests
            """
    }
    stage('Deploy') {
        echo 'Deploying....'
         sh """
                . venv/bin/activate
                pyb upload
            """
    }

}
