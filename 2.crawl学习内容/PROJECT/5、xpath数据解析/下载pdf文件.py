import requests
from lxml import etree

url='https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fdown4.abcjiaoyu.com%2Fabcziyuan%2F2a447fc70c3641d9ba4cf113a1b35398%2F%25e6%2590%25ad%25e9%2585%258d%25e4%25b8%25ad%25e7%259a%2584%25e5%25ad%25a6%25e9%2597%25ae.ppt&wdOrigin=BROWSELINK'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}

response=requests.get(url,headers=headers)
with open('a.ppt','wb')as f:
    f.write(response.text)
