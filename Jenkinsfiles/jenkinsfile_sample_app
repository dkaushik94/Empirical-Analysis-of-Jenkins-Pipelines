pipeline {
  agent any
  stages {
    stage('Sample app build') {
      steps {
        sh '''#!/bin/bash -xe
export RAILS_ENV=test
bundle install --deployment --path vendor/bundle
bundle exec rake db:migrate
bundle exec rspec spec --order random --fail-fast'''
      }
    }
  }
}