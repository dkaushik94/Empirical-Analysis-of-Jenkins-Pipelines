node('master') {
  checkout scm
  stage('Get Ansible Roles') {
    sh('#!/bin/sh -e\n' + 'ansible-galaxy install -r ansible/requirements.yml -p ansible/roles/ -f')
  }
  stage('Get inventory') {
    dir('ansible/inventory') {
      git url: 'git@github.com:USF-IT/cims-ansible-inventory.git', branch: 'master'
    }
    dir('ansible/common') {
      git url: 'git@github.com:USF-IT/idm-ansible-common.git', branch: 'master'
    }
  }
  stage('Build jenkins') {
    sshagent (credentials: ['jenkins']) {
      sh('#!/bin/sh -e\n' + "ansible-playbook -i ansible/inventory/${env.DEPLOY_ENV.toLowerCase()}/hosts --user=jenkins --vault-password-file=${env.USF_ANSIBLE_VAULT_KEY} ansible/playbook.yml --extra-vars 'target_hosts=jenkins deploy_env=${env.DEPLOY_ENV}' -b -t deploy")
    }
  }

}
