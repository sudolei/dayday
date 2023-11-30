from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError

username = 'admin'
password = 'admin1'
# tomcat服务器管理页
url = 'http://localhost:8080/manager/html'
p = HTTPPasswordMgrWithDefaultRealm();
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)
try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print("error : {} ", e);
