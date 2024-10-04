import pprint

import requests
import execjs
url = 'https://interface.bidcenter.com.cn/search/GetSearchProHandler.ashx'

headers = {
    'referer': 'https://search.bidcenter.com.cn/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

data = {
    'from': '6137',
    'guid': '94a49897-7e5e-44f9-b683-d03398050325',
    'location': '6138',
    'token': '',
    'next_token': '',
    'keywords': '%E5%85%AC%E5%85%B1%E4%BA%A4%E6%98%93%E8%B5%84%E6%BA%90',
    'mod': '0',
    'page': '3',
}

response = requests.post(url, headers=headers, data=data)
str=response.text
with open('./采招网.js','r',encoding='utf-8')as f:
    js_file=f.read()

data1=execjs.compile(js_file).call('data',str)
print(data1)

