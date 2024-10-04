# 内容：批量爬虫A站免费视频
# 目录页链接：https://www.acfun.cn/
# 视频demo页链接：https://www.acfun.cn/v/ac34857244
# 格式：将视频保存为mp4文件

"""
知识点：
    理解m3u8视频结构
    Requests模块使用
    Json数据提取
    re模块使用
    bs4提取数据
    tqdm模块使用
"""

import pprint
import re
import requests
import json
import os
from tqdm import tqdm
from lxml import etree

# 获取目录页的视频链接
def parse0(url):
    res=req(url).text
    html=etree.HTML(res)
    link_list=html.xpath('//*[@id="listwrapper"]/div/div/a[1]/@href')
    link_l=[]
    for i in link_list:
        link='https://www.acfun.cn'+i
        link_l.append(link)
    return link_l


# 请求函数
def req(url):
    headers = {
        'referer': 'https://www.acfun.cn/v/list215/index.htm',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return response


# 获取m3u8列表文件和标题
def get_m3u8(response):
    m3u8_data = re.findall('window.pageInfo = window.videoInfo = (.*?)window.videoResource = \{\}', response.text, re.S)[0].split(';')[0]
    m3u8_json = json.loads(m3u8_data)
    m3u8_url = json.loads(m3u8_json['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['url']
    title=m3u8_json['title']
    return m3u8_url,title

# 提取所有视频片段的播放地址 ts文件
def get_ts(m3u8_url,title):
    response=req(m3u8_url).text
    print(response)
    href_list=re.sub('#.*','',response).split()
    return href_list,title

# 下载并合并视频片段
def save(url_list,title):
    if not os.path.exists('./A站视频'):
        os.mkdir('./A站视频')
    with open(f'./A站视频/{title}.mp4', 'wb')as f:
        for i in tqdm(url_list):
            url='https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/'+i
            f.write(requests.get(url).content)


def main():
    url = 'https://www.acfun.cn/v/list215/index.htm?sortField=rankScore&duration=all&date=default&page=1'
    link_l=parse0(url)
    for i in link_l:
        response=req(i)
        get_m3u8(response)
        m3u8_url,title = get_m3u8(response)
        url_list,title=get_ts(m3u8_url,title)
        save(url_list,title)
        print(f'{title}保存成功')

if __name__ == '__main__':
    main()
