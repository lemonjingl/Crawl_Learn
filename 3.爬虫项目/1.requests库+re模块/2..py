import requests

url = 'http://www.ik123.com/q/tuku/keai/75251.html'

cookies = {
    't': '599ed3a26a340571ed7806a365dc290c',
    'r': '2693',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'http://p.ik123.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}


response = requests.get(url, headers=headers, cookies=cookies)
response.encoding='gb2312'
print(response.text)
