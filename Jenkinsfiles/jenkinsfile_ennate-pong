node {
  def ECR_ADDRESS = "536232358765.dkr.ecr.us-east-1.amazonaws.com"
  def ECR_REPO = "ennate-pong"
  def DOCKER_IMAGE_VERSION = ""

  def DOCKER_SERVICE_ID = "ennate-pong"

  stage("clean workspace") {
    deleteDir()
  }

  stage("git checkout") {
    checkout scm

    def GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim().take(11)
    DOCKER_IMAGE_VERSION = "${BUILD_NUMBER}-${GIT_COMMIT}"
  }

  stage("npm build") {
    nodejs(nodeJSInstallationName: "nodev6.10.0") {
      sh "npm install"
      sh "node_modules/.bin/ng build --prod --env=prod"
    }
  }

  stage("docker build") {
    sh "mv ./dist ./config/docker/dist"
    dir("./config/docker/") {
      sh "docker build -t ${ECR_ADDRESS}/${ECR_REPO}:${DOCKER_IMAGE_VERSION} ."
    }
  }

  stage("docker push") {
    sh "aws ecr get-login --no-include-email --region us-east-1 | bash"

    try {
      sh "aws ecr create-repository --repository-name ${ECR_REPO}"
    }
    catch(e) {
      echo "${ECR_ADDRESS}/${ECR_REPO} already exists"
    }

    sh "docker push ${ECR_ADDRESS}/${ECR_REPO}:${DOCKER_IMAGE_VERSION}"
  }

  stage("docker service") {
    try {
      // Create the service if it doesn't exist otherwise just update the image
      sh """
        ssh jenkins@swarm.egen.io bash -c "'
            aws ecr get-login --no-include-email --region us-east-1 | bash
            if [[ \\\$(docker service ls --filter name=${DOCKER_SERVICE_ID} --quiet | wc -l) -eq 0 ]]; then
              docker service create \
                --with-registry-auth \
                --replicas 1 \
                --name ${DOCKER_SERVICE_ID} \
                --network kernel-network \
                ${ECR_ADDRESS}/${ECR_REPO}:${DOCKER_IMAGE_VERSION}
            else
              docker service update \
                --with-registry-auth \
                --image ${ECR_ADDRESS}/${ECR_REPO}:${DOCKER_IMAGE_VERSION} \
                ${DOCKER_SERVICE_ID}
            fi
        '"
      """
    }
    catch(e) {
      sh "docker service update --rollback ${DOCKER_SERVICE_ID}"
      error "Service update failed. Rolling back ${DOCKER_SERVICE_ID}"
    }
    finally {
      sh """
        ssh jenkins@swarm.egen.io bash -c "'
            docker container prune -f
            docker image prune -af
        '"
      """
    }
  }

  stage("cleanup") {
    deleteDir()
    sh "docker container prune -f"
    sh "docker rmi ${ECR_ADDRESS}/${ECR_REPO}:${DOCKER_IMAGE_VERSION}"
  }
}