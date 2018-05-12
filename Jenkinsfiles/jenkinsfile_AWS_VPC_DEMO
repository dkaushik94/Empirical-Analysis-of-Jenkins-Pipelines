pipeline {
  agent any
  stages {
    stage('Execute Terraform') {
      steps {
        echo 'creating vpc'
        sh '''(cd /var/lib/jenkins/terraformPractice/; sudo git pull)
cp -f /var/lib/jenkins/variables/variables.tf variables.tf
cp -f /var/lib/jenkins/terraformPractice/aws-vpc.tf aws-vpc.tf
terraform init
terraform plan
terraform apply'''
      }
    }
    stage('Sleep 5.5 min') {
      steps {
        echo 'Sleeping'
        sleep(time: 330, unit: 'SECONDS')
        echo 'Waking up'
      }
    }
    stage('InSpec Tests') {
      steps {
        echo 'Testing with InSpec'
        sh '''cp -f /var/lib/jenkins/inspecTests/test.rb test.rb
sudo inspec exec test.rb -t ssh://ec2-user@`terraform output privateVMip` -i /home/ec2-user/.ssh/id_rsa'''
        sh 'sudo inspec exec test.rb -t ssh://ec2-user@`terraform output protectedVMip` -i /home/ec2-user/.ssh/id_rsa'
        sh 'sudo inspec exec test.rb -t ssh://ec2-user@`terraform output publicVMip` -i /home/ec2-user/.ssh/id_rsa'
      }
    }
    stage('Destroy') {
      steps {
        echo 'Destroying'
        sh 'terraform destroy -force || true'
      }
    }
  }
}
