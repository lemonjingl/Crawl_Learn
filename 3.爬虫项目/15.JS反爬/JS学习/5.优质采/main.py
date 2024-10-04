# coding = utf-8
import re

import crawles
import requests.utils
import execjs

url = 'https://www.youzhicai.com/nd/ef01deba-b1cd-4acc-a4c3-2dd94dded3d9-2.html'

headers = {
    'authority': 'www.youzhicai.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://www.youzhicai.com/nd/ef01deba-b1cd-4acc-a4c3-2dd94dded3d9-2.html',
    'sec-ch-ua': '\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = crawles.get(url, headers=headers)


with open('./1234.html','w',encoding='utf-8')as f:
    f.write(response.text)

response1=re.sub('\s','',response.text)
var_a=re.findall("vara='(.*?)';",response1)[0]
var_b=re.findall("varb='(.*?)';",response1)[0]
# print(var_a)
# print(var_b)

with open('demo.js','r',encoding='utf-8')as f:
    js_file=f.read()
spvrscode=execjs.compile(js_file).call('main123',var_a,var_b)


cookies=requests.utils.dict_from_cookiejar(response.cookies)#将response.cookies变成字典
cookies['spvrscode']=spvrscode


# 第二次请求
response2 = requests.get(url, headers=headers,cookies=cookies).text
print(response2)



