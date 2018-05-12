#!groovy

node {

    stage("Source") {
        checkout scm
    }

    stage("Initialize virtualenv") {
        sh "rm -rf venv"
        sh "python3 -m venv venv"
        sh "venv/bin/pip install -U wheel pip cffi"
        sh "venv/bin/pip install -r requirements.txt"
    }

    stage("Build GOV.UK assets") {
        sh "venv/bin/python manage.py install_all_govuk_assets --clean"
    }

    if (!BRANCH_NAME.startsWith('PR-')) {

        stage("Deploy") {
            def branch = "${BRANCH_NAME.replace('_', '-')}"
            def appName = cfAppName("ags-prototypes", branch)
            def url = "https://${appName}.cloudapps.digital"

            stash(
                name: "app",
                includes: ".cfignore,Procfile,application/**,deploy-to-paas,lib/**,*.yml,*.txt"
            )

            node('master') {

                unstash "app"

                deployToPaaS(appName)
            }

        }

    }
}


def cfAppName(appName, branch) {

    if (branch != 'master') {
        appName = "${appName}-${branch}"
    }

    return appName
}


def deployToPaaS(app_name) {

    withEnv(["CF_APPNAME=${app_name}"]) {
        withCredentials([
            usernamePassword(
                credentialsId: 'paas-deploy',
                usernameVariable: 'CF_USER',
                passwordVariable: 'CF_PASSWORD'),
            file(
                credentialsId: 'environment.sh',
                variable: 'ENV_FILE')]) {

            ansiColor("xterm") {
                sh "./deploy-to-paas"
            }
        }
    }
}
