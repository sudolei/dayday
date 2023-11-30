from urllib import request,error
try:
  #该url是不存在的，所以会产生异常
    response = request.urlopen('https://cuiqingcai.com/indea.html')
# except error.URLError as e:
#   #由于访问的网页不存在，所以会打印Not Found
# 	print(e.reason)
except error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)