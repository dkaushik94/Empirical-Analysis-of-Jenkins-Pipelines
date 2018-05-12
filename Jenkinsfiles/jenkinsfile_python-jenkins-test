pipeline {
  agent any
  stages {
    stage('Install') {
      steps {
        sh '$python --version'
        sh '$python -m pip install -U -r dev-requirements.txt'
      }
    }
    stage('Test') {
      steps {
        catchError() {
          sh '$python -m pytest --junitxml results.xml test'
        }
        
        junit 'results.xml'
      }
    }
  }
  environment {
    python = "$PYTHON_ENVS/test/bin/python"
  }
}