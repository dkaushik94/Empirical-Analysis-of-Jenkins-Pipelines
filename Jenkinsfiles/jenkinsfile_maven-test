@Library('spk-jenkins-lib')

def d = dockerRunner('james.mcdonald@spk.no')

d.mvn 'clean package'
d.build {
    sh 'ls -l /*.jar'
}
