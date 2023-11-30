
import requests
# POST方法如果是
data = {'msg':'germey','id':'25'}
headers = {
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': '*/*'
}
r = requests.post('http://127.0.0.1:1990/day/h/getData',json=data,headers=headers)
print(r.text)
print(r)
