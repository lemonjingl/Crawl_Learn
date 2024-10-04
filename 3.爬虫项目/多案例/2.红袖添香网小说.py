# 目标数据：
# 内容：爬取红袖添香网免费小说
# 范围：1~47章节
# 目录链接：https://www.hongxiu.com/book/23319469809201404#Catalog
# 存储为txt模块

import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
if not os.path.exists('./谢爷说夫人命中缺宠，得惯着！'):
    os.mkdir('./谢爷说夫人命中缺宠，得惯着！')

def req(url):
    headers = {
        'Referer': 'https://www.hongxiu.com/book/23319469809201404',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    response = requests.get(url, headers=headers).text
    return response

"""目录解析"""
def parse0(url):
    response=req(url)
    html=etree.HTML(response)
    href_list=html.xpath('//*[@id="j-catalogWrap"]/div[2]/div/ul/li/a/@href')
    for i in href_list:
        href='https://www.hongxiu.com'+i
        # 调用详情页解析函数
        parse(href)

"""详情页解析函数"""
def parse(url):
    response=req(url)
    soup=BeautifulSoup(response,'lxml')
    title=soup.find('h1',class_="j_chapterName").text
    print(title)
    content=soup.select('.ywskythunderfont > p')
    for i in content:
        content1=i.text
        save(title,content1)

"""保存函数"""
def save(title,content1):
    with open(f'./谢爷说夫人命中缺宠，得惯着！/{title}.txt','a',encoding='utf-8')as f:
        f.write(content1+'\n')

if __name__ == '__main__':
    url = 'https://www.hongxiu.com/book/23319469809201404#Catalog'
    parse0(url)

