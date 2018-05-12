pipeline
{
    agent { docker 'maven:3-alpine' }

    stages
    {
        stage('Compile Stage')
        {
            steps
            {
                withMaven(maven : 'Maven3.5.2') { sh 'mvn clean package -DskipTests' }
            }
        }

        stage('Testing Stage')
        {
            steps
            {
                withMaven(maven : 'Maven3.5.2') { sh 'mvn test' }
            }
        }
    }

}

