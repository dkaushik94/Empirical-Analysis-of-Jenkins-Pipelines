pipeline {
  agent any
  stages {
    stage('Testing') {
      parallel {
        stage('Pester') {
          steps {
            powershell(script: 'Invoke-Pester -Path "$env:workspace\\add-numbers.test.ps1\'', returnStatus: true)
          }
        }
        stage('PSScriptAnalyzer') {
          steps {
            powershell(script: 'Invoke-ScriptAnalyzer -Path "$env:workspace\\add-numbers.ps1"', returnStatus: true)
          }
        }
      }
    }
    stage('Publish') {
      steps {
        powershell 'New-ScriptFileInfo -Path "$env:workspace\\\\add-numbers.test.ps1" -Description "Adds two inputs" -Version "1.1" -Author "Kyle Ruddy" -Tag "DTW"'
        powershell 'Publish-Script -Path ./Add-Numbers.ps1 -repository InternalRepo -NuGetApiKey "2e8ddec2-3117-3af9-a2e3-820fe83ad469"'
      }
    }
  }
}