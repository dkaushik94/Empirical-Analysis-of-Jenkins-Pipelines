import os
import sys
import traceback
import requests
import shutil
from progress.bar import ChargingBar

class Repositories:

    def __init__(self):
        self.num_repos = 0
        self.num_pages = 1
        self.clone_urls = []

    @staticmethod
    def create_substructure(dir_name = None, dir = True, filename = None, data = None):
        try:
            if dir:
                try:
                    os.system('mkdir '+ dir_name)
                    return (os.getcwd() + dir_name, 1)
                except Exception:
                    return 0
            elif not dir:
                try:
                    os.chdir(dir_name)
                    f = open(filename, 'w+')
                    f.write(data)
                    f.close()
                    os.chdir('..')
                except Exception:
                    return 0
        except Exception:
            print(traceback.format_exc())
    
    @staticmethod
    def clone_repos(repo_url):
        try:
            os.chdir("/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/")
            os.system("git clone " + repo_url)
            name = repo_url.split('/')[-1].replace('.git','')
            os.chdir(name)

            assert 'Jenkinsfile'.lower().strip() in [a.lower().strip() for a in os.listdir()]
            [os.rename(a, a.strip().lower()) for a in os.listdir()]
            os.rename('jenkinsfile', 'Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/jenkinsfiles_'+name)
            shutil.move('jenkinsfile', 'Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/jenkinsfiles_'+name)
            for item in os.listdir():
                if item != 'jenkinsfile':
                    print(item)
                    os.system('sudo rm -r'+item)
            os.chdir('../')
            # os.system('sudo rm -r' + name)
        except Exception:
            print(traceback.format_exc())

    def get_jenkins_repositories(self):
        try:

            # bar = ChargingBar('Fetching repositories:', max_length = self.num_pages)
            for i in range(0,self.num_pages+1):
                jenkins_data = requests.get('https://api.github.com/search/code?q=filename:Jenkinsfile&page='+str(i),auth=('sandeepjoshi1910','P@ssw0rd'))
                try:
                    jenkins_files = jenkins_data.json()['items']    
                except:
                    continue

                for item in jenkins_files:
                    repo = item['repository']['name']
                    data = requests.get('https://api.github.com/search/repositories?q='+repo, auth=('sandeepjoshi1910','P@ssw0rd'))
                    try:
                        clone_url = data.json()['items'][0]['clone_url']    
                        self.clone_urls.append(clone_url)
                        self.num_repos = self.num_repos + 1
                    except Exception:
                        print(traceback.format_exc())
                # bar.next()
            # bar.finish()

            print("\033[1;32mCloning repositories..\033[1;m")
            for item in self.clone_urls:
                self.clone_repos(item)

                
        except Exception:
            print(traceback.format_exc())



if __name__ == '__main__':
    try:
        r = Repositories()
        r.get_jenkins_repositories()
        print(r.clone_urls)
    except Exception:
        print(traceback.format_exc())