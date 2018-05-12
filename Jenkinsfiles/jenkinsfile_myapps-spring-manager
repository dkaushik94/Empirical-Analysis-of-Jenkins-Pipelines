pipeline {
  agent any
  stages {
    stage('Build verification test') {
      steps {
        build(job: '../bvt/datica-hips-bvt/', propagate: true, quietPeriod: 5, wait: true)
      }
    }
    stage('User acceptance test') {
      steps {
        parallel(
          "User acceptance test": {
            build(job: '../website/datica-rwb-website-hips-tests', propagate: true, wait: true, quietPeriod: 5)
            
          },
          "Visual & link checkers": {
            build(job: '../visual/datica-hips-visual', propagate: true, wait: true, quietPeriod: 5)
            
          }
        )
      }
    }
  }
}