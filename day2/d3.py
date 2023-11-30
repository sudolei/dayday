import requests

r = requests.get('http://www.weibo.com/')
with open('xxx.ico','wb')as f:
	f.write(r.content)
