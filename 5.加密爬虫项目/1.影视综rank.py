# 目标网站：https://www.chinaindex.net/ranklist/4
# 要求：1、使用requests
#           2、抓取：电影榜电影排名，名称，活跃受众，受众变化，趋势
# 提交方式：代码+运行效果截图
#

import requests
import execjs
import prettytable as tp

with open('1.js', 'r', encoding='utf-8')as f:
    js_file = f.read()
d={
    "url": "mobile/movie/objectFansRank",
    "method": "GET"
}
sign=execjs.compile(js_file).call('getSign',d)

def req_get(url):
    headers = {
        'Referer': 'https://www.chinaindex.net/ranklist/4',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = {
        'channel': 'movielist',
        'sign': f'{sign}',
    }

    response = requests.get(url, headers=headers, params=params)
    return response

def get_data(response):
    data=response.json()['data']
    n=response.json()['lastFetchTime']
    with open('1.js', 'r', encoding='utf-8')as f:
        js_file=f.read()
    data1=execjs.compile(js_file).call('dataFilte',data,n)
    return data1

def get_detail_data(data1):
    tb = tp.PrettyTable()
    tb.field_names = ['排名', '名称', '活跃受众', '受众变化', '趋势']
    for i in data1["listOfRank"]:
        rank = i['rank']
        movie_name = i['object_name']
        Active_audiences = i['user_day_num']
        Audience_changes = i['user_change_num']
        tend = i['rank_change']
        tb.add_row([rank, movie_name, Active_audiences, Audience_changes, tend])
    print(tb)

if __name__ == '__main__':
    url = 'https://www.chinaindex.net/iIndexMobileServer/mobile/movie/objectFansRank'
    response=req_get(url)
    data1=get_data(response)
    get_detail_data(data1)