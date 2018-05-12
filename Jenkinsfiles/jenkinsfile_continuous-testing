stage ('Build'){
	node('testEnv'){
		//sh "echo Checking out and build solution..."
		git 'https://github.com/tjrodrigues/continuous-testing.git'
		//withMaven(maven: 'maven3') {
			//sh '''cd ${WORKSPACE}/spring-petclinic-angularjs-master
				//./mvnw clean install -DskipTests'''
		//}
	}
}

stage('Unit Test & Satic Analysis') {
	parallel (
		"Unit Test" : { 
			node ('testEnv') {                          
				sh "echo Executing Unit tests..." 
				withMaven(maven: 'maven3') {
				  sh '''cd ${WORKSPACE}/spring-petclinic-angularjs-master
					./mvnw test
					'''
					//junit 'spring-petclinic-angularjs-master/spring-petclinic-server/target/surefire-report/*.xml'
				}
			} 
		},
		"SonarQube" : { 
			node ('testEnv') {   
				sh "echo Executing SonarQube Analysis..." 
				git 'https://github.com/tjrodrigues/continuous-testing.git'
				withSonarQubeEnv('SonarQube'){
					withMaven(maven: 'maven3'){
						sh '''cd ${WORKSPACE}/spring-petclinic-angularjs-master
						./mvnw install -DskipTests $SONAR_MAVEN_GOAL -Dsonar.host.url=$SONAR_HOST_URL'''
					}
				} 
			} 
		}
	)
}

stage ('Packaging'){
	node('testEnv'){
		sh "echo Create distribution package and save it to Nexus"
		sh '''cd ${WORKSPACE}
		sudo tar -czvf spring-petclinic-angularjs-master.tar.gz spring-petclinic-angularjs-master/'''
		nexusArtifactUploader artifacts: [[artifactId: 'petclinic', classifier: '', file: "${WORKSPACE}/spring-petclinic-angularjs-master.tar.gz", type: 'tar.gz']], credentialsId: 'Nexus', groupId: 'org.criticalsoftware.sspa', nexusUrl: '192.168.3.11:8081', nexusVersion: 'nexus3', protocol: 'http', repository: 'maven-releases', version: "2.0.${BUILD_NUMBER}"

	}
}

stage ('Deploy'){
	node('testEnv'){
		sh "echo Stopping previous deployments ..."
		sh "pgrep -f wrapper | sudo xargs kill -9"
		sh "pgrep -f mvnw | sudo xargs kill -9"
		sh "echo Deploying services ..."
		sh "${WORKSPACE}/spring-petclinic-angularjs-master/deploy/deploy.sh 192.168.3.11:8081 2.0.${BUILD_NUMBER} ${WORKSPACE}"
		waitUntil {
			// Wait until app is up and running
		    try {
					sh 'timeout 30 wget --retry-connrefused --tries=10 --waitretry=10 http://192.168.3.11:8080' // -o /dev/null
					return true 
				} catch (exception) {
				    return false
				}
		}
	}
}

stage('Functional Tests') {
	parallel (
		"Robot Framework Web" : { 
			node ('rfBox') {            
				git 'https://github.com/tjrodrigues/continuous-testing.git'
				bat '''cd %WORKSPACE%\\spring-petclinic-angularjs-master\\tests\\rf 
				pybot -v HOMEPAGE:http://192.168.3.11:8080 tests\\web-tests.robot'''

				step([$class: 'RobotPublisher',
				  disableArchiveOutput: false,
				  logFileName: 'log.html',
				  otherFiles: '',
				  outputFileName: 'output.xml',
				  outputPath: 'spring-petclinic-angularjs-master\\tests\\rf',
				  passThreshold: 100,
				  reportFileName: 'report.html',
				  unstableThreshold: 0]);
				  publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '%WORKSPACE%\\\\spring-petclinic-angularjs-master\\\\tests\\\\rf', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: ''])
				
			} 
		},
		"SoapUI API" : { 
		node ('testEnv') { 
				//build job: 'API-AutTests', propagate: false 
				sh '${WORKSPACE}/spring-petclinic-angularjs-master/tests/api/run-soapui-tests.sh /home/ubuntu/SoapUI-5.4.0 http://192.168.3.11:8080 ${WORKSPACE}/spring-petclinic-angularjs-master/tests/api/Spring-PetClinic-soapui-project.xml ${WORKSPACE}/spring-petclinic-angularjs-master/tests/api/_test_reports/'
				junit 'spring-petclinic-angularjs-master/tests/api/_test_reports/*.xml'
			} 
		},
		"Robot Framework Mobile" : { 
			node ('testEnv') {  
				return true			
			} 
		}
	)
}


stage ('Performance Testing'){
	node('testEnv'){
		sh "echo Running jMeter tests ..."
		bzt 'spring-petclinic-angularjs-master/tests/performance/performance-test-suite.jmx'
	}
}

stage ('Security Testing'){
	node('testEnv'){
		sh "echo Running AppScan tests ..."
		//bzt 'spring-petclinic-angularjs-master/tests/performance/performance-test-suite.jmx'
	}
}

stage ('Deployment (Production)'){
	input 'Do you approve deployment?'
	node('testEnv'){
		 return true
		//deploy things
	}
}



