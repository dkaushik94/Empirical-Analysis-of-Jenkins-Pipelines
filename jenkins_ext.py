import re


file = open('./jenkinsfile.groovy','r')
data = file.read()
# print(data)

res = re.findall(r'agent\s',data)
print(res)