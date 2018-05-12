/* this is working DSL in windows with pipline maven integration plugin -- if didnt work try removing <settings> tag in nexuscongi
pipeline {
    agent any
    stages {
        stage ('Compile Stage') {
            steps {
                withMaven(maven : 'apache-maven-3.3.9') {
                    bat 'mvn -s nexusconfigurations/nexus.xml clean compile'
                }
            }
        }
        stage ('Testing Stage') {
            steps {
                withMaven(maven : 'apache-maven-3.3.9') {
                    bat 'mvn -s nexusconfigurations/nexus.xml test'
                }
            }
        }
        stage ('Deployment Stage') {
            steps {
                withMaven(maven : 'apache-maven-3.3.9') {
                    bat 'mvn -s nexusconfigurations/nexus.xml deploy'
                }
            }
        }
    }
}
*/

/*testing in openshift jenkins - not able to download artifacts from maven central..failed in last step
pipeline {
    agent {
              label 'maven'
            }
    stages {
        stage ('Compile Stage') {
            steps {
                 
                    sh "mvn -s nexusconfigurations/nexus.xml clean compile"
               
            }
        }
        stage ('Testing Stage') {
            steps {
                 
                    sh "mvn -s nexusconfigurations/nexus.xml test"
                
            }
        }
        stage ('Deployment Stage') {
            steps {
                 
                    sh "mvn -s nexusconfigurations/nexus.xml deploy"
                
            }
        }
    }
}
*/



/*
stage ('buildInDevelopment'){
steps{
openshiftBuild(namespace: 'jenkinsfdeploy', bldCfg: 'php', showBuildLogs: 'true')}}

stage ('deployInDevelopment'){
steps{
openshiftDeploy(namespace: 'jenkinsfdeploy', depCfg: 'php')
openshiftScale(namespace: 'jenkinsfdeploy', depCfg: 'php',replicaCount: '2')}}*/

/*
//testing oc cli
stage('Create Image Builder') {
                when {
                  expression {
                    openshift.withCluster('https://192.168.99.100:8443, QF03ylfGRGhSR24vxmCU7OXhUVx3k9RAZTnbT4gjncw') {
                      openshift.withProject('abc') {
                        return !openshift.selector("bc", "tasks").exists();
                      }
                    }
                  }
                }
                steps {
                  script {
                    openshift.withCluster('https://192.168.99.100:8443, QF03ylfGRGhSR24vxmCU7OXhUVx3k9RAZTnbT4gjncw') {
                      openshift.withProject('abc')  {
                        openshift.newBuild("--name=tasks", "--image-stream=jboss-eap70-openshift:1.5", "--binary=true")
                      }
                    }
                  }
                }
              }
              stage('Build Image') {
                steps {
                  sh "rm -rf oc-build && mkdir -p oc-build/deployments"
                  sh "cp target/openshift-tasks.war oc-build/deployments/ROOT.war"
                  
                  script {
                    openshift.withCluster('https://192.168.99.100:8443, QF03ylfGRGhSR24vxmCU7OXhUVx3k9RAZTnbT4gjncw') {
                      openshift.withProject('abc')  {
                        openshift.selector("bc", "tasks").startBuild("--from-dir=oc-build", "--wait=true")
                      }
                    }
                  }
                }
              }


    }
}*/


// build in jenkns & deploy in openshift using oc cmds is successfull
// this is working DSL in windows with pipline maven integration plugin -- if didnt work try removing <settings> tag in nexuscongi --
// deploy to openshift
pipeline {
 agent any

 stages {
  stage('Compile Stage') {

   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     bat 'mvn -s nexusconfigurations/nexus.xml clean compile'
    }
   }
  }

  stage('Testing Stage') {

   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     bat 'mvn -s nexusconfigurations/nexus.xml test'
    }
   }
  }
  stage('Sonar Code Analysis') {
   steps {
	   withMaven(maven: 'apache-maven-3.3.9') {
    bat 'mvn -s nexusconfigurations/nexus.xml test sonar:sonar -Dsonar.host.url=http://localhost:9000   -Dsonar.login=aab02659e091858dfd99ddace56d44c604390a52'
   }}
   }

  stage('Deployment Stage') {
   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     bat 'mvn -s nexusconfigurations/nexus.xml deploy'
    }
   }
  }

  stage('Archive jar to Jenkins target') {

   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     archive 'target/*.jar'
    }
   }
  }



  stage('Approve to Deploy on Openshift') {
   steps {
    timeout(time: 2, unit: 'DAYS') {
     input message: 'Do you want to Approve?'
    }
   }
  }
  stage('login') {
   steps {
    sh 'oc login https://192.168.99.100:8443 --token=G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA --insecure-skip-tls-verify'
   }
  }
  stage('new project') {
   steps {
    sh 'oc project jdk71'
   }
  }
  stage('new build') {
   steps {
    sh 'oc new-build --name=abc redhat-openjdk18-openshift --binary=true'
   }
  }
  stage('build') {
   steps {
    sh "rm -rf oc-build && mkdir -p oc-build/deployments"
    sh "cp target/student-services-0.0.1-SNAPSHOT.jar oc-build/deployments/ROOT.jar"

    sh 'oc start-build abc --from-dir=oc-build --wait=true  --follow'

    


   }
  }
  stage('deploy expose') {
   steps {
    sh 'oc new-app abc'
    sh 'oc expose svc/abc'
   }
  }
  stage('scaling') {
   steps {
    sh ' oc scale --replicas=10 dc abc'
   }
  }

 }
} 

/*
// testing cd jenkins code
// this is working DSL in windows with pipline maven integration plugin -- if didnt work try removing <settings> tag in nexuscongi --
// deploy to openshift
pipeline {
 agent any

 stages {
  stage('Compile Stage') {

   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     bat 'mvn -s nexusconfigurations/nexus.xml clean compile'
    }
   }
  }

  stage('Testing Stage') {

   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     bat 'mvn -s nexusconfigurations/nexus.xml test'
    }
   }
  }


  stage('Deployment Stage') {
   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     bat 'mvn -s nexusconfigurations/nexus.xml deploy'
    }
   }
  }

  stage('Archive jar to Jenkins target') {

   steps {
    withMaven(maven: 'apache-maven-3.3.9') {
     archive 'target/*.jar'
    }
   }
  }



  stage('Approve to Deploy on Openshift') {
   steps {
    timeout(time: 2, unit: 'DAYS') {
     input message: 'Do you want to Approve?'
    }
   }
  }

  
  
  
  
                stage('Create Image Builder') {
                when {
                  expression {
                    openshift.withCluster('https://192.168.99.100:8443','G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA') {
                      openshift.withProject('cdcd') {
                        return !openshift.selector("bc", "tasks").exists();
                      }
                    }
                  }
                }
                steps {
                  script {
                    openshift.withCluster('https://192.168.99.100:8443','G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA') {
                      openshift.withProject('cdcd') {
                        openshift.newBuild("--name=tasks", "--image-stream=redhat-openjdk18-openshift", "--binary=true")
                      }
                    }
                  }
                }
              }
              stage('Build Image') {
                steps {
                  sh "rm -rf oc-build && mkdir -p oc-build/deployments"
                  sh "cp target/student-services-0.0.1-SNAPSHOT.jar oc-build/deployments/ROOT.jar"
				  
                  
                  script {
                    openshift.withCluster('https://192.168.99.100:8443','G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA') {
                      openshift.withProject('cdcd') {
                        openshift.selector("bc", "tasks").startBuild("--from-dir=oc-build", "--wait=true")
                      }
                    }
                  }
                }
              }
              stage('Create DEV') {
                when {
                  expression {
                    openshift.withCluster('https://192.168.99.100:8443','G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA') {
                      openshift.withProject('cdcd') {
                        return !openshift.selector('dc', 'tasks').exists()
                      }
                    }
                  }
                }
                steps {
                  script {
                    openshift.withCluster('https://192.168.99.100:8443','G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA') {
                      openshift.withProject('cdcd') {
                        def app = openshift.newApp("tasks:latest")
                        app.narrow("svc").expose();
                        def dc = openshift.selector("dc", "tasks")
                        while (dc.object().spec.replicas != dc.object().status.availableReplicas) {
                            sleep 10
                        }
                        openshift.set("triggers", "dc/tasks", "--remove-all")
                      }
                    }
                  }
                }
              }
              stage('Deploy DEV') {
                steps {
                  script {
                    openshift.withCluster('https://192.168.99.100:8443','G2AsDzhLjmwyBsRCYmRu0EekAGGetQlFJewtR2XmyVA') {
                      openshift.withProject('cdcd') {
                        openshift.selector("dc", "tasks").rollout().latest();
                      }
                    }
                  }
                }
              } 

 }
}*/