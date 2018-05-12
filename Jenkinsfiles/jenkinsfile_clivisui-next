node {
    stage ("checkout") {
        checkout scm 
    }
    stage ("build"){    
        sh "npm install"
        sh "ng build --aot --env=prod --prod --output-path dist"
    }
    stage ("publish"){
        sh "pwd"
        sh "scp -q -i ~/.ssh/id_rsa nas/* 192.168.1.20:/volume1/web/nas/"
    }
}
