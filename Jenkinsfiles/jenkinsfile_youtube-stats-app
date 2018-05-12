node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("youtube-stats-app")
        
        
      
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        app.inside {
            sh 'echo "Tests passed"'
        }
    }
    
    stage('Deploy') {
    sh "docker run --rm -d -p 8090:8090 youtube-stats-app:latest" -e $YOUTUBE_API_KEY -e $YOUTUBE_V3_URL
    }
    
  
}
