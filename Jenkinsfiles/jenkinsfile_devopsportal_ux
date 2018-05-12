node('dockerhost34') {
	stage('Update Code') {

		checkout([$class: 'GitSCM', branches: [[name: '*/devopsportal_ux']], doGenerateSubmoduleConfigurations: false, extensions: [], gitTool: 'Default', submoduleCfg: [], userRemoteConfigs: [[credentialsId: '850f825e-b762-4d50-ae7d-8f1ea478d1d6', url: 'http://10.103.21.145:7990/bitbucket/scm/dop/devopsportal.git']]])

		}
	
	// docker.image('sonar-scanner-2.8').inside{
	// stage('Code Analysis') {

	// 	sh "sonar-scanner" 

	// 	}
	// }

	stage('Build'){
		docker.build "devopsux_img:${env.BUILD_NUMBER}"
	}
	
	stage('Deploy'){
		sh "/home/support/delete_container.sh devopsux_con"
		sh "/home/support/create_container.sh devopsux_con devopsux_img ${env.BUILD_NUMBER}"
	}

}