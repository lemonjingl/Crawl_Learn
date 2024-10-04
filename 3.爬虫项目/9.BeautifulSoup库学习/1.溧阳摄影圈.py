# http://www.jsly001.com/read-htm-tid-3766678.html

from bs4 import BeautifulSoup
import requests

url='http://www.jsly001.com/thread-htm-fid-45-page-1.html'
res=requests.get(url=url,)

soup=BeautifulSoup(res.text,'lxml')
data=soup.tbody
print(data)
