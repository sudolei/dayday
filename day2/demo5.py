#导入request模块
import urllib.request
#发出请求并得到响应
response = urllib.request.urlopen("https://www.python.org")
content = response.readlines()
print(content)