# 内容：爬取王者荣耀高清壁纸
# 范围：所有英雄页面下壁纸
# 目录链接：https://pvp.qq.com/web201605/herolist.shtml
# 格式：存储为jpg图片
import pprint

import requests
from fake_useragent import UserAgent
import re
import os
from lxml import etree
if not os.path.exists('./王者荣耀壁纸'):
    os.mkdir('./王者荣耀壁纸')

ua=UserAgent()


def req(url):
    headers={'User-Agent':f'{ua.chrome}'}
    res=requests.get(url,headers=headers)
    return res

def parse0(url):
    res=req(url)
    res = eval(res.text)
    for i in res:
        title = i['cname']
        href = f'https://pvp.qq.com/web201605/herodetail/{i["id_name"]}.shtml'
        #调用解析图片函数
        parse(href,title)

"""解析图片链接"""
def parse(url,title):
    res=req(url)
    href='https:'+re.findall('<div class="wrapper">(.*?)<div class="con1-pic">',res.text,re.S)[0].split("'")[1]
    html=etree.HTML(res.text)
    #调用保存函数
    save(href,title)

def save(href,title):
    with open(f'./王者荣耀壁纸/{title}.jpg','wb')as f:
        f.write(requests.get(href).content)
        print(f'{title}保存成功')

if __name__ == '__main__':
    url = 'https://pvp.qq.com/web201605/js/herolist.json'
    parse0(url)
