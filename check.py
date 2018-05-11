'''
Written by Debojit Kaushik  (Timestamp)
'''
import os
import sys
import traceback
import requests

COUNT = 0


def checker(page_no):
	try:
		global COUNT
		flag = False
		r = requests.get('https://api.github.com/search/code?q=filename:jenkinsfile path:/&page=%s' %(page_no), auth = ('dkaushik94', 'soundspace312'))
		for i, item in enumerate(r.json()['items']):
			user, repo_name = item['repository']['owner']['login'], item['repository']['name']
			url = "https://api.github.com/repos/%s/%s/contents/" %(user, repo_name)
			q = requests.get(url, auth = ('dkaushik94', 'soundspace312'))
			for it in q.json():
				if it['name'].lower().strip() == 'jenkinsfile':
					print(it['name'])
					COUNT += 1
					flag = True
				else:
					pass
		return flag
	except Exception:
		print(traceback.format_exc())

if __name__ == '__main__':
	try:
		for i in range(7):
			flag = checker(i)
			print('\033[1;32mpage\033[1;m:', i)
			if not flag:
				break
		print('Count:',COUNT)
	except Exception:
		print(traceback.format_exc())