# 内容：爬取虎牙视频
# 范围：第一页
# 目录链接：https://v.huya.com
# 格式：存储为mp4文件

import pprint

import requests
import json
import time
import os
from lxml import etree
from tqdm import tqdm

if not os.path.exists('./虎牙视频'):
    os.mkdir('./虎牙视频')

def req(url,params):
    headers = {
        'referer': 'https://www.huya.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    res = requests.get(url, params=params,headers=headers)
    res = json.loads(res.text)
    return res

# 解析列表链接
def parse0(url):
    headers = {
        'referer': 'https://www.huya.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    res = requests.get(url, headers=headers)
    html=etree.HTML(res.text)
    url_list=html.xpath('//*[@id="root"]/div/article/section/ul[2]/li/a/@href')
    return url_list

# 解析视频链接
def parse(res):
    url_detail=res['data']['moment']['videoInfo']['definitions'][0]['url']
    title=res['data']['moment']['title'].replace('\n','')
    return title,url_detail

def save(title,url_detail):
    path=f'./虎牙视频/{title}.mp4'
    with open(path,'wb')as f:
        f.write(requests.get(url_detail).content)
        print(f'{title}保存成功')

def main():
    url = 'https://www.huya.com/video/g/survival?set_id=33&order=hot&page=1'
    link_list=parse0(url)
    for i in tqdm(link_list):
        id=i.split('/')[-1].split('.')[0]
        link='https://liveapi.huya.com/moment/getMomentContent'
        params = {
            'videoId': f'{id}',
            '_': f'{int(time.time() * 1000)}',
        }
        res=req(link,params)
        title,url_detail=parse(res)
        save(title,url_detail)

if __name__ == '__main__':
    main()
