pipeline {
  agent {
    node {
      label 'Sid_Machine'
    }
    
  }
  stages {
    stage('Master_A') {
      steps {
        parallel(
          "Master_A": {
            node(label: 'Master') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\a.vbs"', returnStatus: true, returnStdout: true)
            }
            
            bat(script: 'Wscript "C:\\Devaraj\\Test\\b.vbs"', returnStatus: true, returnStdout: true)
            echo '"In Stage Master A - Last step"'
            
          },
          "Slave_A": {
            node(label: 'Sid_Machine') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\a.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          }
        )
      }
    }
    stage('Master_B') {
      steps {
        parallel(
          "Master_B": {
            node(label: 'Master') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\b.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          },
          "Slave_B": {
            node(label: 'Sid_Machine') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\b.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          },
          "Slave_C": {
            node(label: 'Sid_Machine') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\c.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          }
        )
      }
    }
    stage('Slave_D') {
      steps {
        parallel(
          "Slave_D": {
            node(label: 'Sid_Machine') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\d.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          },
          "Slave_E": {
            node(label: 'Sid_Machine') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\e.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          }
        )
      }
    }
    stage('Master_D') {
      steps {
        parallel(
          "Master_D": {
            node(label: 'Master') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\d.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          },
          "Master_E": {
            node(label: 'Master') {
              bat(script: 'Wscript "C:\\Devaraj\\Test\\e.vbs"', returnStatus: true, returnStdout: true)
            }
            
            
          }
        )
      }
    }
  }
}