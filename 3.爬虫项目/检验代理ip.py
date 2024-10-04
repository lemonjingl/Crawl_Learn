import requests
from fake_useragent import UserAgent
ua=UserAgent()

#方法一
url='https://www.baidu.com'

headers={'User-Agent':ua.chrome}

proxies={
    'http':'http://59.120.115.116:8080',
    'https':'https://59.120.115.116:8080'
}

res=requests.get(url=url,headers=headers,proxies=proxies)
print(res.text)

