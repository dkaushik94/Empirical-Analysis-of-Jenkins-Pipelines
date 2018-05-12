node {
    try {
        checkout scm

        stage('Run tests') {
            sh "echo 'snake oil'"
        }

        stage('Build container') {
            if (env.BRANCH_NAME == "master") {
                sh "docker-compose up --build -d production"
            } else {
                sh "echo 'Skipping as branch was ${env.BRANCH_NAME} instead of master'"
            }
        }

    } catch (err) {
        echo "${err}"
        throw err
    } finally {
        stage('Shutdown') {
            sh "echo 'Shutdown'"
        }
    }
}
