stage('hello') {
    echo 'hello from Pipeline'
}

docker.image('node:5.10.1').inside {
    stage('checkout') {
        checkout scm
    }
}
