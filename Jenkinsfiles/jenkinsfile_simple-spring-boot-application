node {
	stage('Init') {
		env.module = 'simple-spring-boot-application'
		env.repoUrl = 'github.com/iancollington/'
		env.dockerImagePrefix = 'iancollington/'

		properties([
			buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10')),
			[$class: 'GithubProjectProperty', displayName: '', projectUrlStr: 'https://${repoUrl}/${module}'],
			pipelineTriggers([githubPush()])
		])

		env.PATH = "${tool 'Maven'}/bin:${env.PATH}"

		git (url: "https://${repoUrl}/${module}")

		pom = readMavenPom file: 'pom.xml'
		env.version = pom.version
	}

	stage('Version') {
		sh "echo \'\ninfo.build.version=\'$version >> src/main/resources/application.properties || true"
	}

	stage('Compile') {
		sh 'mvn -B -V -U -e clean compile -DskipTests'
	}

	stage('Test') {
		try {
			sh "mvn -B -V -U -e verify"
		} finally {
			junit allowEmptyResults: true, testResults: '**/target/surefire-reports/*.xml'
			junit allowEmptyResults: true, testResults: '**/target/failsafe-reports/*.xml'
		}
	}

	stage('Package') {
		sh 'mvn -B -V -U -e clean package -DskipTests'

		sh "git config user.name 'Jenkins'"
		sh "git config user.email 'jenkins@iancollington.com'"
		sh "git tag -f $version"

		withCredentials([[$class: 'UsernamePasswordMultiBinding',
			credentialsId: 'GitHub',
			usernameVariable: 'GIT_USERNAME',
			passwordVariable: 'GIT_PASSWORD']]) {

			sh 'git push -f https://${GIT_USERNAME}:${GIT_PASSWORD}@${repoUrl}/${module} --tags'
		}

		docker.withRegistry('https://registry.hub.docker.com/u/','DockerHub') {
			def image = docker.build "$dockerImagePrefix$module"
			image.push "$version"
			image.push "latest"
		}
	}

	stage('Deploy') {
		sh '/usr/local/bin/kubectl set image -f src/main/k8s/k8s-deployment.yaml $module=$dockerImagePrefix$module:$version --local -o yaml | sed "s/BUILD_DATE_PLACEHOLDER/$(date)/g" - | /usr/local/bin/kubectl apply --force -f -'
		sh "/usr/local/bin/kubectl apply -f src/main/k8s/k8s-service.yaml"
		sh "/usr/local/bin/kubectl apply -f src/main/k8s/k8s-ingress.yaml"
	}
}
