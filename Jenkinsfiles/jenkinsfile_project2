properties([[$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/syamOrg/project1.git'],pipelineTriggers([upstream('Project1, ')]) ])
pipeline {
    agent any
        stages {
            stage('Build') {
                when {
                    expression {
                        "foo" == "bar"
                    }
                }
                steps {
                    echo 'Building'
                }
            }
        stage('Test') {
            when {
                environment name: 'JOB_NAME', value: 'foo'
            }
            steps {
                echo 'Testing'
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                echo 'Deploying'
            }
        }
    
     stage('Deployed') {
            when {
                branch 'master'
            }
            steps {
                echo 'Deployed'
            }
        }
    }
}
