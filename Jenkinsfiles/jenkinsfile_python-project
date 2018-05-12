pipeline{
  environment{
    var_x = "puppet"
  }
  agent none


  stages{
    stage ('python-project'){
      agent any
      steps{
        sh 'python newfile.py'
          echo "ID"
          sh 'id'
          echo "PWD"
          sh 'pwd'
      }
      post{
        always{
          archiveArtifacts artifacts: "logs/*.txt", fingerprint: true
        }
      }
    }

    stage ('sayHello'){
      agent any
      steps{
        sayHello 'Brent'
      }
    }
    stage ('env'){
      agent any
      steps{
        sh 'echo "var_x is $var_x"'
      }
    }



    stage('promote to green'){
      agent{
        label 'apache'
      }
      when{
        branch 'development'
      }
      steps{

        sh """
        if [ ! -d "/var/www/html/green" ];then sudo mkdir /var/www/html/green;fi
        sudo cp logs/myOutFile.txt /var/www/html/green
        """
      }
    }
    stage('run-parallel-branches'){
      agent any
      steps{
        parallel(
          a:{
            echo "This is branch a"
            sh 'hostname'
          },
          b:{
            echo "This is branch b"
            sh 'hostname'
          }
        )
      }
    }
    stage('run-parallel-on-different-nodes'){
      parallel{
        stage ('run on master'){
          agent{
            label 'apache'
          }
          steps{
            sh 'echo `hostname`'
          }
        }
        stage('run on slave'){
          agent{
            label 'Linux'
          }
          steps{
            sh 'echo `hostname`'
          }
        }
      }
    }
    stage('merge development to master'){
      agent any
      when{
        branch 'development'
      }

      steps{
        echo "Stashing any local changes"
        sh 'git stash'
        echo "checkout development"
        sh 'git checkout development'
        echo "pull latest changes"
        sh 'git pull'
        echo "checkout master"
        sh 'git checkout master'
        echo "pull latest from master"
        sh 'git pull'
        echo "merging development into master"
        sh 'git merge development'
        echo "Pushing to remote"
        sh 'git push origin master'
      }
    }
  }
}
