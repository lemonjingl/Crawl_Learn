# 内容：爬取免费TX动漫
# 范围：1~65章
# 目录链接：https://ac.qq.com/Comic/comicInfo/id/651757
# 格式：存储为jpg图片

import requests
from lxml import etree
import os
import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
ua=UserAgent()

def req0(url):
    headers={'User-Agent':f'{ua.chrome}'}
    res=requests.get(url,headers=headers)
    html=etree.HTML(res.text)
    href_list=html.xpath('//*[@id="chapter"]/div[2]/ol[1]/li/p/span[2]/a/@href')[0:20]
    for i in href_list:
        link='https://ac.qq.com/'+i
        req(link)

"""请求详情页函数"""
def req(url):
    service=Service(executable_path='/chromedriver-win64/chromedriver.exe')
    driver=webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(2)
    parse(driver)


"""解析图片链接函数"""
def parse(driver):
    href_list = driver.find_elements(By.XPATH, '//*[@id="comicContain"]/li/img')
    title=driver.find_element(By.XPATH,'//*[@id="comicTitle"]/span[3]').text
    subheadings=1
    for i in href_list:
        time.sleep(0.5)
        # 需要将页面下滑到该链接，然后才能出的来那个正常的链接
        ActionChains(driver).scroll_to_element(i).perform()
        href = i.get_attribute('src')
        save(href,title,subheadings)
        subheadings+=1
    print(f'{title}保存成功')

"""保存函数"""
def save(url,title,subheadings):
    # 每一章节创建一个文件夹
    path = os.path.join('.\\Tx动漫', title)
    if not os.path.exists(path):
        os.makedirs(path)
    # 每一张图片一个命名
    path1=os.path.join(path,str(subheadings))
    with open(path1+'.jpg','wb')as f:
        f.write(requests.get(url).content)


if __name__ == '__main__':
    url='https://ac.qq.com/Comic/comicInfo/id/651757'
    req0(url)
