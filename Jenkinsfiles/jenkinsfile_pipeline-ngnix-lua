stage('build & push') {
    node {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            git url: "https://github.com/abz99/pipeline-ngnix-lua"
            sh "git rev-parse HEAD > .git/commit-id"
            def commit_id = readFile('.git/commit-id').trim()
            println commit_id
            def app = docker.build "corvuscoraxx/nginx"
            app.push "${env.BUILD_NUMBER}"
            app.push "latest" 
        }
    }
}
stage('deploy') {
    podTemplate(label: 'ngnix-lua', containers: [
        containerTemplate(name: 'helm', image: 'lachlanevenson/k8s-helm:latest', command: 'cat', ttyEnabled: true),
      ]){
            node('ngnix-lua'){
    	        container('helm') {
                	git url: "https://github.com/abz99/pipeline-ngnix-lua"
                	def chart_dir = "charts/nginx-lua"
                	sh "helm init && helm delete --purge nginx-lua || True; helm install --name nginx-lua ${chart_dir}"
    	        }
            }
    }
}
