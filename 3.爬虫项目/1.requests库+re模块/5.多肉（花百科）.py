# coding = utf-8
from lxml import etree
import requests
import os
if not os.path.exists('./多肉'):
    os.mkdir('./多肉')

url = 'https://www.huabaike.com/jingtian/'

cookies = {
    '__yjs_duid': '1_bafe4d9a16dfadb08a4a5fe4140fb5631681033411834',
    '__bid_n': '1876566465d5db739a4207',
    'FPTOKEN': 'pTIfI4PwIXjT4tE8b3rf7AnJfjEIilssbMd5+v+0TDAPRnCmeq14VfVHVJcWNyh2LXh5Fx0BFoPZKY/hLk02HjGqxSeIq6Xb6OQh8uRxl5jdiseZwAj2NuQIdLm60TrubidxIaKqiOa7AhBh9yXkCCoacDPHao7XQL9CkeFnSnKKd+Bm7ld2Z90qJEjtBgqqtcRwxC0Rz9QtVNtCOI0mdANWnnO/fosjxlc7sf7QXvbCOlXUlzsk3Mm8sw8GsgXj8lSMbXVWXFz67ae3yF3YtvzlpOYNXU/tf5KBqQ2ePmn7SUfissxEm2W/W/eURtkTJBzRRh/Tg0MnDsitunAMdrrJ2TCcgeyUWfIHXqIdI8nCRy06xS4YnA9MFIgWwhaHzD9ZcWWoFCVPSfFNOE1kXg==|rskdVx9OTLJLuakxrlt+1g4DUZ2+O/NVS+bBwiqDnR0=|10|1f6ff93fc2b194c5e0d32ca735fb765b',
    'Hm_lvt_74d598b5f90fcb987e1ff71fafbea9b6': '1690333160',
    'PHPSESSID': 'rrtranf9fchekmf27kcdee0ct4',
    'Hm_lpvt_74d598b5f90fcb987e1ff71fafbea9b6': '1690333500',
}

headers = {
    'user-agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

response = requests.get(url=url, headers=headers, cookies=cookies)
response.encoding='utf-8'


# 数据解析
html=etree.HTML(response.text)

title=html.xpath('//div[@class="zhiwuImg"]/ul/li/a/img/@alt')
url_list=html.xpath('//div[@class="zhiwuImg"]/ul/li/a/img/@src')
data=zip(title,url_list)

# 数据保存
for title,url1 in data:
    res=requests.get(url=url1,headers=headers)
    path=f'多肉/{title}.jpg'
    with open(path,'wb')as f:
        f.write(res.content)
        print(f'{title}保存完成')


