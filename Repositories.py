import os
import sys
import traceback
import requests
import shutil
from progress.bar import ChargingBar

class Repositories:

	def __init__(self):
		self.num_repos = 0
		self.num_pages = 6
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
	def collect_jenkins():
		try:
			folders = os.listdir()
			folders.pop(folders.index('.DS_Store'))
			for item in folders:
				
				os.chdir(item)
				# assert 'Jenkinsfile'.lower().strip() in [a.lower().strip() for a in os.listdir()]
				for i in os.listdir():
					os.rename(i,i.lower().strip())
				os.rename('jenkinsfile','jenkinsfile_'+item)
				jenkins_file = 'jenkinsfile_'+item
				os.system('cp '+ jenkins_file + ' /Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/')
				os.chdir('..')
				
		except Exception:
			print(traceback.format_exc())

	def get_jenkins_repositories(self):
		try:
			os.chdir("/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/")
			for i in range(1,self.num_pages+1):
				print('\033[1;32mPage:\033[1;m', i)
				jenkins_data =  requests.get('https://api.github.com/search/code?q=filename:jenkinsfile path:/&page=%s' %(i), auth = ('dkaushik94', 'soundspace312'))
				for i, item in enumerate(jenkins_data.json()['items']):
					user, repo_name = item['repository']['owner']['login'], item['repository']['name']
					clone_url = "https://www.github.com/%s/%s.git"%(user, repo_name)
					os.system("git clone " + clone_url)
			# self.collect_jenkins()
				
		except Exception:
			print(traceback.format_exc())



if __name__ == '__main__':
	try:
		r = Repositories()
		# r.get_jenkins_repositories()
		os.chdir("/Users/debojitkaushik/ATSE/sandeep_joshi__debojit_kaushik_course_project/Repos/")
		r.collect_jenkins()
		
	except Exception:
		print(traceback.format_exc())