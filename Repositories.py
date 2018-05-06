import requests


class Repositories(object):

    num_pages = 2

    def get_jenkins_repositories(self):
        for i in range(0,self.num_pages+1):
            jenkins_data = requests.get('https://api.github.com/search/code?q=filename:Jenkinsfile&page='+str(i),auth=('sandeepjoshi1910','P@ssw0rd'))

            jenkins_files = jenkins_data.json()['items']

            for item in jenkins_files:
                repo = item['repository']['name']
                print(repo)
                data = requests.get('https://api.github.com/search/repositories?q='+repo,auth=('sandeepjoshi1910','P@ssw0rd'))
                try:
                    clone_url = data.json()['items'][0]['clone_url']    
                    print(clone_url)
                except:
                    print('Error')
            
r = Repositories()
r.get_jenkins_repositories()