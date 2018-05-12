/***********************************************************************
 * These will vary from branch to branch
 ***********************************************************************/
branch='master'
symbolicTag = "unstable"
tagPrefix=''


/***********************************************************************
 * Constants
 ***********************************************************************/
repo='git@github.com:deweysasser/docker-project-template.git'
String gitcreds= 'git@github.com'
image="docker-project-template"
registry="registry:5000"
registryurl="https://${registry}"	

/***********************************************************************
 * Derived variables
 ***********************************************************************/

number=env.BUILD_NUMBER
tag = "${tagPrefix}${branch}-${number}"

/***********************************************************************
 * Build code
 ***********************************************************************/

node('docker') {

    //////////////////////////////////////////////////////////////////////
    stage 'Checkout'
    //////////////////////////////////////////////////////////////////////

    git credentialsId: gitcreds, branch: branch, url: repo

    //////////////////////////////////////////////////////////////////////
    stage 'Preparing'
    //////////////////////////////////////////////////////////////////////

    sh 'make clean'

    //////////////////////////////////////////////////////////////////////
    stage 'Docker build'
    //////////////////////////////////////////////////////////////////////

    sh "make build IMAGE=${image} TAG=${tag}"

    //////////////////////////////////////////////////////////////////////
    stage 'Test'
    //////////////////////////////////////////////////////////////////////

    sh "make test IMAGE=${image} TAG=${tag}"

    //////////////////////////////////////////////////////////////////////
    stage 'Push'
    //////////////////////////////////////////////////////////////////////

    if(branch.equals('release')) {
	// tag the build in GIT, so we can get back to it later
	sh "git tag build/${tag}"
	sshagent([gitcreds]) {
	    sh 'git push --tags'
	}
    }

    dockerImage= docker.image("${image}:${tag}")
    docker.withRegistry(registryurl) {
	dockerImage.push(tag)
    }
}

if(symbolicTag) {
    //////////////////////////////////////////////////////////////////////
    stage "Tagging ${symbolicTag}"
    //////////////////////////////////////////////////////////////////////

    if(branch.equals("release")) {
	input "Mark as ${symbolicTag}?"
    }

    node("docker") {
	sh "docker pull ${registry}/${image}:${tag}"
	sh "docker tag ${registry}/${image}:${tag} ${image}:${tag}"
	dockerImage = docker.image("${image}:${tag}")
	docker.withRegistry(registryurl) {
	dockerImage.push(symbolicTag)
	}
    }
}
	