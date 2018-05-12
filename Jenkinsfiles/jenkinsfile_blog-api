node {
    try {
        stage("Build") {
            git 'git@github.com:qaninjahq/blog-api.git'
            ruby('bundler install')
        }
        stage("Development") {
            env.RACK_ENV = 'development'
            ruby("rspec -fd --format RspecJunitFormatter --out logs/unit_tests.xml")
            junit 'logs/unit_tests.xml'
        }
            stage("Testing") {
            sh "./deploy.sh testing"
            env.RACK_ENV = 'testing'
            ruby("rspec -fd --format RspecJunitFormatter --out logs/func_tests.xml")
            junit 'logs/func_tests.xml'
        }
        stage("Production") {
            sh "./deploy.sh prod"
        }
    }
    catch (err) {
        currentBuild = 'Deu ruim no build :('
        junit 'logs/*.xml'
        throw err
    }

}

def ruby(String commands) {
    sh "bash -c 'source ~/.bashrc && rbenv global 2.4.3 && ${commands}'"
}