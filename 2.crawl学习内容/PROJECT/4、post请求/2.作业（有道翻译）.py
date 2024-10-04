import requests

url='https://dict.youdao.com/webtranslate'
headers={'Accept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6.中国五矿集团采购信息',
'Connection': 'keep-alive',
'Content-Length': '252',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'OUTFOX_SEARCH_USER_ID=-829659723@10.108.162.134; OUTFOX_SEARCH_USER_ID_NCOO=530209000.163514',
'Host': 'dict.youdao.com',
'Origin': 'https://fanyi.youdao.com',
'Referer': 'https://fanyi.youdao.com/',
'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'}

data={'i': '坚持',
'from': 'auto',
'dictResult': 'true',
'keyid': 'webfanyi',
'sign': '7009ffe9ceb625de28726b789c2ddc6d',
'client': 'fanyideskweb',
'product': 'webfanyi',
'appVersion': '1.0.0',
'vendor': 'web',
'pointParam': 'client,mysticTime,product',
'mysticTime': '1673365410212',
'keyfrom': 'fanyi.web'}

response=requests.post(url,data=data,headers=headers)
print(response.text)