import os
import sys
import traceback
import requests
import shutil
import logging


#Logging setup
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "info.log",
    level=os.environ.get("LOGLEVEL", "INFO"),
    format = LOG_FORMAT,
    filemode = 'w')
log = logging.getLogger(__name__)


class Repositories:
	"""
		Class with moethods to fetch jenkins repositories from GITHUB and then extrack the jenks file in to a dataset. 
	"""
	def __init__(self):
		self.num_repos = 0
		self.num_pages = 6
		self.clone_urls = []

	
	@staticmethod
	def collect_jenkins():
		try:
			folders = os.listdir()
			folders.pop(folders.index('.DS_Store'))
			# For every folder, make every name of file/directory uniform, lower(), strip().
			for item in folders:	
				os.chdir(item)
				for i in os.listdir():
					os.rename(i,i.lower().strip())
				# Move the jenkins file tp the said directry and rename each jenkinsfile of the form,
				# jenkinsfile_reponame.
				os.rename('jenkinsfile','jenkinsfile_'+item)
				jenkins_file = 'jenkinsfile_'+item
				log.info('Extracting jenkins file %s' %jenkins_file)
				os.system('cp '+ jenkins_file + ' /Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/jenkins_dataset/')
				os.chdir('..')
		except Exception:
			print(traceback.format_exc())

	def get_jenkins_repositories(self):
		try:
			os.chdir("/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/")
			# Iterate over numebr of pages we want to fetch from github
			for i in range(1,self.num_pages+1):
				log.info("Fetching page number %s" %i)
				jenkins_data =  requests.get('https://api.github.com/search/code?q=filename:jenkinsfile path:/&page=%s' %(i), auth = ('dkaushik94', 'soundspace312'))
				
				# Get user and repo_name and construct clone_url. after, Clone the repository to the local machine.
				for i, item in enumerate(jenkins_data.json()['items']):
					user, repo_name = item['repository']['owner']['login'], item['repository']['name']
					#Clone repo.
					clone_url = "https://www.github.com/%s/%s.git" %(user, repo_name)
					os.system("git clone " + clone_url)
			#Extract jenkins file from each repo using this co-routine.
			self.collect_jenkins()
		except Exception:
			print(traceback.format_exc())



if __name__ == '__main__':
	try:
		r = Repositories()
		r.get_jenkins_repositories()
	except Exception:
		print(traceback.format_exc())