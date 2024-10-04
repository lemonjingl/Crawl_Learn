import requests
from fake_useragent import UserAgent
from lxml import etree

# 先获取进入详情页的链接
def requests_f():
    url = 'https://www.maoyan.com/films?showType=3&offset=30'

    cookies = {
        '__mta': '146584075.1691968846968.1692599986511.1692600035750.20',
        'uuid_n_v': 'v1',
        'uuid': '08589B903A3011EE8C94F7F95193CE98EB1CCC364BA04D119AF0FFC222C112C6',
        '_lxsdk_cuid': '189f133bb31c8-026661f2c484e4-26031c51-e1000-189f133bb3196',
        '_lxsdk': '08589B903A3011EE8C94F7F95193CE98EB1CCC364BA04D119AF0FFC222C112C6',
        '_lx_utm': 'utm_source%3Dbing%26utm_medium%3Dorganic',
        '_csrf': '35584aefda9717fe85b992ab355c89c9887afc1c97ca15d580df563299d2e9f5',
        'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2': '1691968847,1692313970,1692598362',
        'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2': '1692600035',
        '_lxsdk_s': '18a16b95d81-698-74e-368%7C%7C36',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://www.maoyan.com/films?showType=3',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '\\',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '\\',
    }


    response = requests.get(url, headers=headers,cookies=cookies)
    parse(response)

def parse(res):
    html=etree.HTML(res.text)
    url_list=html.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[1]/a/@href')
    print(url_list)
    for i in url_list:
        url_detail='https://www.maoyan.com'+i
        print(url_detail)

requests_f()
