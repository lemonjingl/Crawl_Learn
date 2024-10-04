# 内容：爬取飞卢小说网免费小说
# 范围：1~61章
# 链接：https://b.faloo.com/html_1217_1217177/
# 格式：存储为一个txt文件
'''
首先先爬一个章节的内容，然后爬取目录通过目录爬取章节的链接和章节的名字
'''

import requests
from bs4 import BeautifulSoup
import os
import time
if not os.path.exists('./飞卢小说'):
    os.mkdir('./飞卢小说')

"""请求函数"""
def req(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    res=requests.get(url,headers=headers).text
    return res

"""解析目录页的函数"""
def parse(url):
    res=req(url)
    soup=BeautifulSoup(res,'lxml')
    data=soup.select('.c_con_li_detail_p > a')
    data_y=[]
    for i in data:
        url_detail='http:'+i.get('href')
        title=i['title']
        data_y.append((url_detail,title))
    return data_y

"""解析详情页"""
def parse_detail(url):
    for i in parse(url):
        url_detail,title=i
        res=req(url_detail)
        soup=BeautifulSoup(res,'lxml')
        essay=soup.find('div',class_="noveContent").text
        title=title.split(":")[1]
        save(essay,title)

def save(essay,title):
    path=f'飞卢小说/全民：开局邀请光头强挑战只狼.txt'
    with open(path,'a',encoding='utf-8')as f:
        f.write(title+'\n\n')
        f.write(essay+'\n\n')
        f.write('--'*60+'\n\n')
        print(f'{title}保存成功')

if __name__ == '__main__':
    url='https://b.faloo.com/html_1217_1217177/'
    print(parse_detail(url))


