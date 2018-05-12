import org.jenkinsci.plugins.workflow.steps.FlowInterruptedException
def notifySlack(String Status = 'STARTED',String customMessage=" ")
{
    // build status of null means successful
    Status =  Status ?: 'SUCCESSFUL'
    // Default values
    def colorName = 'RED'

    def colorCode = '#FF0000'

    def subject = "${Status}: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'"

    def summary = "${subject} (${env.BUILD_URL})"

    def details = """<p>STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>

    <p>Check console output at <a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a></p>"""

     

    // Override default values based on build status

    if (Status == 'STARTED') {

        color = 'YELLOW'

        colorCode = '#FFFF00'

    }

    else if (Status == 'SUCCESSFUL'){

        color = 'GREEN'

        colorCode = '#00FF00'

    }

    else {

        color = 'RED'

        colorCode = '#FF0000'

    }

    slackSend (color: colorCode, message: summary)

    slackSend (color: colorCode, message: customMessage)
            
}
def rollback(int server){

    def res = ""

    try{

        timeout(time: 12000, unit: 'SECONDS') {

            input message: 'Click Proceed to Rollback Automatically', submitter: ''

        }       

        for(int RollBackFromServer=server;RollBackFromServer>=0;RollBackFromServer--){

            stage("REVERT ")

            timeout(time: 12000, unit: 'SECONDS') {

                input message: 'Click Proceed to RollOver', submitter: ''

            }
            
            timeout(time: 12000, unit: 'SECONDS') {

                input message: 'Click Proceed to AddNode', submitter: ''

            }

        }

    }

    catch(Exception ex) {

        echo res

        echo 'RollBack Unsuccessful'

        throw ex

    }               
}
    node {
            env.WorkSpace = 'C:\\Users\\Administrator\\Desktop'
            dir("${env.WorkSpace}") {

                stage 'CHECKOUT'

                try{           

                     //checkout([$class: 'GitSCM', branches: [[name: 'origin/' + ""]], doGenerateSubmoduleConfigurations: false,  extensions: [[$class: 'PruneStaleBranch']], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/rjkumar1536/Demo.git']]])
                      checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '56506a35-9c43-4e38-acf6-96cc65436690', url: 'https://github.com/rjkumar1536/Demo.git']]])
                }

                catch(Exception ex){

                    throw ex

                }     
                
                stage 'BUILD'

                try {

                    notifySlack('STARTED')

                    echo "hello"

                } 

                catch (Exception ex){


                    echo "There is some error in build"

                    currentBuild.result = "FAILED"

                    throw ex

                }
               stage 'DeployStatic'
                
                for(currentStaticServer=0;currentStaticServer < 5;currentStaticServer++){

                    try {

                        timeout(time: 12000, unit: 'SECONDS') {

                            input message: 'Click Proceed to Deploy static content', submitter: ''                                        

                        }

                        

                    }

                    catch(Exception ex) {

                       

                        throw ex

                    }

                finally {

                    echo "finally"

                    notifySlack(currentBuild.result)

                }

            }
              for(currentServer=0;currentServer<5;currentServer++){

            try{

                stage("RemoveNode")

                timeout(time: 12000, unit: 'SECONDS') {

                    input message: 'Click Proceed to RemoveNode', submitter: ''

                }

                node{

                    echo "node removed"                                    

                }

            }   

            catch(FlowInterruptedException ex){

                echo 'Its aborted..now I cant do anything.....Removing node cant be done'

                rollback(currentServer)

            }

            catch (Exception ex){

                echo "Some error in remove node" //need to check whether to rollback or not 

                rollback(currentServer)

                throw ex                    

            }        

            try{

                stage("DeployCode")

                timeout(time: 12000, unit: 'SECONDS'){

                    input message: 'Click Proceed to DeployCode', submitter: ''

                }

            }

            catch(FlowInterruptedException ex){

                echo "Aborted by user or time out"

                rollback(currentServer)

                throw ex

            }

            catch (Exception ex){

                echo "exception occured"

                rollback(currentServer)

                throw ex

            }

            stage("API Testing")

             try{

                node{

                    echo "Api Testing"

                 }

            }

            catch (Exception ex){

                echo "exception occured"

                rollback(currentServer)

                throw ex

             }

            try{

                stage("Warmup")

                echo "warming up"

            }

            catch (Exception ex){

                echo "exception occured"

                rollback(currentServer)

                throw ex

            }    

            try{

                stage("AddNode")

                timeout(time: 12000, unit: 'SECONDS'){

                    input message: 'Click Proceed to AddNode', submitter: ''

                }

                node{

                    echo "Node Added To LB"

                }

            }

            catch(FlowInterruptedException ex){

                echo "Aborted by user or time out"

                rollback(currentServer)

                throw ex

            }

            catch (Exception ex){

                echo "exception occured"

                rollback(currentServer)

                throw ex

            }                        

        }
                
     }
}

