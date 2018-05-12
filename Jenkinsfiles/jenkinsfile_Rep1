#!/usr/bin/env groovy
properties([
    [$class: 'GithubProjectProperty',
    displayName: '',
    projectUrlStr: 'https://github.com/BabuNagaRam/Rep1.git/'],
    pipelineTriggers([githubPush()])])



node
{  
stage 'integrate'
echo 'integrated'
stage 'Test'
echo 'Tested'
stage 'Deploy'
echo 'Deployed'
}


