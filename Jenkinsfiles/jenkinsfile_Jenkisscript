//https://github.com/jenkinsci/http-request-plugin

node{
    stage('deploy') {
        def response
        try{    
         response = httpRequest 'http://localhost:8080/jenkins/api/json?pretty=true'
         
         
         println("Status: "+response.status)
         println("Content: "+response.content)
         //mysh('curl www.google.com')
        }catch(error){
            //throw error
         println("C...")
        }
    
     
     
        def response2 = httpRequest 'http://192.168.0.13:9000/hello-world?name=test'
        println("Status: "+response2.status)
        println("Content: "+response2.content)
     
        mysh('curl http://192.168.0.13:9000/hello-world?name=test')
    }
}
def mysh(cmd) {
    sh('#!/bin/sh -e\n' + cmd)
}