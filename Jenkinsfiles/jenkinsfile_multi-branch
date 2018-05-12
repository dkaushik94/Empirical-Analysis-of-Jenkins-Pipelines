properties([[$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://github.com/nikhiltinchu/multi-branch.git/'], pipelineTriggers([githubPush()])])


pipeline {
    agent any 
             parameters {
                            string(defaultValue: "default", description: 'Select Branch here ', name: 'Branch')
                           // choices are newline separated
                            choice(choices: 'Integration\nUnit', description: 'Used for posgress sh and codedeploy deployment group', name: 'Environment')
                            booleanParam(name: 'REBUILD DATABASE', defaultValue: true, description: 'Should we rebuild the database')
                            booleanParam(name: 'DEPLOY', defaultValue: true, description: 'should we deploy the application')
             }
    stages {
        stage('Build') { 
            steps { 
                echo 'Hello'
            }
        }
      
    }
}
