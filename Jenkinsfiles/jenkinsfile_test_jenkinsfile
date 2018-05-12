#!groovy

properties([parameters([
    string(name: 'githash', defaultValue: '43408ca'),
    choice(choices: 'sandbox\nprod', name: 'target_env'),
    choice(choices: 'mp\nebayk', name: 'tenant'),
])])

def releaseName = '-'

def log (String msg) {
    echo msg
}

node {
    stage("Find release") {
        echo "Looking for release tenant: ${tenant}, env: ${target_env}, githash: ${githash}"
        def response = httpRequest "http://repo_comaas:V9Knbsi4Nm@repositories.ecg.so/v2/files/${tenant}"
        log("Status: " + response.status)
        def releaseNames = new groovy.json.JsonSlurper().parseText(response.content).keySet()
        log "${releaseNames}"
        for (name in releaseNames) {
            if (name ==~ /.*\/comaas-${tenant}_${target_env}-\d+-\d+-${githash}\.tar.gz/) {
                echo "Release found: ${name} ***"
                releaseName = name
                break
            }
        }
        if (releaseName == '-') {
            error("Could not find release ${githash} for tenant ${tenant} and target env ${target_env} in repositories server.")
        }
    }

    stage("Release") {
        echo "Releasing $releaseName"
    }
}
