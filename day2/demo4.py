import urllib.request,http.cookiejar

cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
# response = opener.open('https://www.instagram.com/takanashi_hanariv3v/')
response = opener.open('https://www.baidu.com')
#遍历cookies
for item in cookie:
	print(item.name+"="+item.value)
