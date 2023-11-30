#导入request模块
import urllib.request
#发出请求并得到响应
response = urllib.request.urlopen("https://www.python.org")
#查看响应的类型
print(type(response))
#打印响应状态码
print(response.status)
#打印请求头
print(response.getheaders())
#打印请求头中Server属性的值（表示服务端使用Web服务器是什么软件，如Tomcat、Nginx等）
print(response.getheader("Server"))

content = response.readline()
print(content)