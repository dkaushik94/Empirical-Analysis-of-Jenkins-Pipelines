timestamps {
    node('ubuntu-s3') {
        cleanWs()
        stage ('grafana') {
            withCredentials([usernamePassword(credentialsId: '1a69cdbb-be20-4bde-b30a-87ef9b2db969',
                              passwordVariable: 'PWRD',
                              usernameVariable: 'USER')
                ]) {
                // dump database, and make sure there is no time info in file
                sh "sudo docker exec -i mysql mysqldump --user ${USER} --password=${PWRD} grafana | grep -v '^-- Dump completed on' > grafana.sql"
                stash includes: 'grafana.sql', name: 'grafana'
            }
        }
        stage ('kafka_data') {
            withCredentials([usernamePassword(credentialsId: '1a69cdbb-be20-4bde-b30a-87ef9b2db969',
                              passwordVariable: 'PWRD',
                              usernameVariable: 'USER')
                ]) {
                // dump database, and make sure there is no time info in file
                sh "sudo docker exec -i mysql mysqldump --user ${USER} --password=${PWRD} kafka_data | grep -v '^-- Dump completed on' > kafka_data.sql"
                stash includes: 'kafka_data.sql', name: 'kafka_data'
            }
        }
        stage ('nconf') {
            withCredentials([usernamePassword(credentialsId: '1a69cdbb-be20-4bde-b30a-87ef9b2db969',
                              passwordVariable: 'PWRD',
                              usernameVariable: 'USER')
                ]) {
                // dump database, and make sure there is no time info in file
                sh "sudo docker exec -i mysql mysqldump --user ${USER} --password=${PWRD} nconf | grep -v '^-- Dump completed on' > nconf.sql"
                stash includes: 'nconf.sql', name: 'nconf'
            }
        }
        stage ('phpmyadmin') {
            withCredentials([usernamePassword(credentialsId: '1a69cdbb-be20-4bde-b30a-87ef9b2db969',
                              passwordVariable: 'PWRD',
                              usernameVariable: 'USER')
                ]) {
                // dump database, and make sure there is no time info in file
                sh "sudo docker exec -i mysql mysqldump --user ${USER} --password=${PWRD} phpmyadmin | grep -v '^-- Dump completed on' > phpmyadmin.sql"
                stash includes: 'phpmyadmin.sql', name: 'phpmyadmin'
            }
        }
        stage ('zen') {
            withCredentials([usernamePassword(credentialsId: '1a69cdbb-be20-4bde-b30a-87ef9b2db969',
                              passwordVariable: 'PWRD',
                              usernameVariable: 'USER')
                ]) {
                // dump database, and make sure there is no time info in file
                sh "sudo docker exec -i mysql mysqldump --user ${USER} --password=${PWRD} zen | grep -v '^-- Dump completed on' > zen.sql"
                stash includes: 'zen.sql', name: 'zen'
            }
        }
        stage ('Update GIThub') {
            withCredentials([usernamePassword(credentialsId: '935a7b57-da74-45f7-9119-5a0529afb8ae',
                              passwordVariable: 'GIT_PASSWORD',
                              usernameVariable: 'GIT_USERNAME')
                ]) {
                // make sure 'cwd' is empty so we can run 'git clone' into workspace
                sh 'rm -rf *'
                sh 'git clone -v -b master https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/ballab1/DBMS-backup.git .'

                // get our DB bakup files
                unstash 'grafana'
                unstash 'kafka_data'
                unstash 'nconf'
                unstash 'phpmyadmin'
                unstash 'zen'
                archive includes:'*.sql'

                // check the 'git status' to see if there are any changes  (return SUCCESS on 0-changes)
                def porcelainStatus = sh (returnStdout: true, script: 'git status --porcelain')?.split("\\r?\\n")
                int numberOfChanges = porcelainStatus?.findAll{ it =~ /[^\\s]+/ }.size()
                if (numberOfChanges > 0) {
                    // update our git repo with changes
                    sh 'git status'
                    sh 'git add -A'
                    sh 'git commit -m "mysql DB updates"'
                    sh 'git push -v'
                    
                    echo 'Setting build to "UNSTABLE" to indicate changes were detected.'
                    manager.buildUnstable()
                }
            }
        }
    }
}
