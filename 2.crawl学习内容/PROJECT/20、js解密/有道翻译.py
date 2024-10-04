import requests
'''
MD5信息摘要算法：一种被广泛使用的密码散列函数，可以产生出一个128位（16字节）的散列值，用于确保信息传输完整一致。不可逆
'''

url='https://dict.youdao.com/webtranslate'

headers={
'ccept': 'application/json, text/plain, */*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Length': '252',
'Content-Type': 'application/x-www-form-urlencoded',
'Cookie': 'OUTFOX_SEARCH_USER_ID=1034277662@10.110.96.157; OUTFOX_SEARCH_USER_ID_NCOO=1925758068.3947096',
'Host': 'dict.youdao.com',
'Origin': 'https://fanyi.youdao.com',
'Referer': 'https://fanyi.youdao.com/',
'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': 'Windows',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-site',
'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

data={'i': '香蕉',
'from': 'auto',
'dictResult': 'true',
'keyid': 'webfanyi',
'sign': '66d982a0739ad11e2e7347e2b053988c',
'client': 'fanyideskweb',
'product': 'webfanyi',
'appVersion': '1.0.0',
'vendor': 'web',
'pointParam': 'client,mysticTime,product',
'mysticTime': '1675137540420',
'keyfrom': 'fanyi.web'
}
response=requests.post(url=url,data=data,headers=headers)
print(response.text)

#数据特征提取的算法
# import hashlib
#
# m=hashlib.md5()
# m.update('aaa0'.encode('utf-8'))
# print(m.hexdigest())