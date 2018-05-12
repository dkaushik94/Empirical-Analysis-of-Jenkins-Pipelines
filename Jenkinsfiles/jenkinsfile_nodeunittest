pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Build') {
      environment {
        npm_config_cache = 'npm-cache'
      }
      steps {
        sh '''echo \'running npm install\'
npm install'''
      }
    }
    stage('test') {
      steps {
        sh 'npm test'
      }
    }
    stage('package') {
      steps {
        sh 'zip -r function.zip index.js sms.js node_modules smsRepository.js'
        sh 'aws s3 cp ./function.zip s3://mg-lambda-deployment/ --region us-west-2'
      }
    }
    stage('cloudFormation-Deploy') {
      steps {
        sh '''aws cloudformation delete-stack --stack-name blueocean-lambda --region us-west-2
'''
        sh 'aws cloudformation create-stack --stack-name blueocean-lambda --template-body file://lambda-cf.yml --region us-west-2'
      }
    }
    stage('deploy') {
      steps {
        sh 'aws lambda create-function --function-name blueocean-lambda --zip-file fileb://./function.zip --timeout 30 --role arn:aws:iam::459375513878:role/lambda_bot_execution --handler index.handler  --runtime nodejs6.10 --region us-west-2 || aws lambda update-function-code --function-name blueocean-lambda --zip-file fileb://./function.zip --region us-west-2'
      }
    }
  }
}