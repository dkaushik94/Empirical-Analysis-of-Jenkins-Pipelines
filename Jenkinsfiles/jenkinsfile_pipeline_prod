pipeline {
    agent any

    stages {
        stage('gate') {
            steps {
                input message:'ready to go?',submitter:'prod_admin,admin'
            }
        }        
        stage('task1_prod') {
            steps {
                echo "PROD banner"
            }
        }
        stage('task2_prod') {         
            steps {
                //bat  "set path=%path%C:\\Program Files (x86)\\Java\\jdk1.8.0_151\\bin;"
				bat 'mkdir C:\\tempDirectoryPROD'
            
            }
        }
        stage('task3_prod') {
            environment {
                PATH = "%path%;C:\\Windows\\SysWOW64;C:\\Program Files (x86)\\Java\\jdk1.8.0_151\\bin"
            }
            steps {
                bat 'javac helloWorld.java'
                bat 'java helloWorld'
            }
        }
    }

     post {
        success{
            echo 'mail sent'
        }
        failure {
            echo 'rollback process'
        }
        
    }
}