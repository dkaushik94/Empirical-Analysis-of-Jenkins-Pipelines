node {
   echo 'Hello Docker'
   
    stage 'Build'
        cleanWs()
        sh 'sudo rm -rf node-js-sample'
        sh 'git clone https://github.com/durgadeviramadoss/node-js-sample.git'
        sh 'cd node-js-sample && pwd'
        sh 'acc=$(cat node-js-sample/account)'
        sh 'echo $acc'
    env.Account = `cat node-js-sample/account`
    stage 'Docker image build'
        sh 'cd node-js-sample &&  sudo docker build -t nodejs-image-new .'
        
    stage 'Docker image tag'
   sh 'echo $(aws ecr get-login --region us-east-1 --registry-ids ${env.Account}) > file.txt'
        sh 'sudo $( sed "s/-e none//g" file.txt)'
        sh 'sudo  docker tag nodejs-image-new ${env.Account}.dkr.ecr.us-east-1.amazonaws.com/demo-jenkins-pipeline:nodejs-image-new-v1'
    
    stage 'Docker image push'
        sh 'sudo docker push ${env.Account}.dkr.ecr.us-east-1.amazonaws.com/demo-jenkins-pipeline:nodejs-image-new-v1'

    stage 'Kubernetes Deploy'
        sh 'echo Hello'
        sh 'kubectl replace -f node-js-sample/deploy.yml --record'
        sh 'kubectl get pods'
}
