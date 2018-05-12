pipeline {
    agent {
        node 'xenial'
    }
    stages {
        stage('Build') {
            steps {
                // This relies on the ~/.pypirc config file that setups the repository
                sh 'python setup.py sdist upload -r local'
            }
        }
    }
}