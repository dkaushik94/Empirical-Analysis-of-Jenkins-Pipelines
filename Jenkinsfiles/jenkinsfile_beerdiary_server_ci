node {
    stage('Checkout') {
        checkout scm
    }

    stage('Image') {
        sh 'docker-compose build'
        sh 'docker-compose push'
    }

    stage('Deployment') {
        sh 'docker stack deploy --compose-file ./docker-compose.yml $BUILD_NAME'
        sh 'docker-compose -p "$BUILD_NAME" run django python manage.py migrate'
        sh 'docker-compose -p "$BUILD_NAME" run django python manage.py collectstatic --noinput'
    }
}