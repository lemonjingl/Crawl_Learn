# https://ec.minmetals.com.cn/open/home/purchase-info

response = requests.get(url, headers=headers,cookies=cookies)
print(response.text)

with open('demo.js','r',encoding='utf-8')as f:
    js_file=f.read()

param=execjs.compile(js_file).call('main123',response.text,2)
print(param)
