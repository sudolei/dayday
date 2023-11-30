import requests
import re

r = requests.get('https://cuiqingcai.com/')
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
