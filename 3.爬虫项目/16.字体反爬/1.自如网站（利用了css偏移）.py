# coding = utf-8
import re

import requests
from lxml import etree

url = 'https://www.ziroom.com/z/p1/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

res = requests.get(url, headers=headers)

# 数据解析
html=etree.HTML(res.text)
data=html.xpath('//span[@class="num"]/@style')[0]
# print(data)

img_src=re.findall('background-image: url\(//(.*?)\);background-position:.*?',data)[0]
# print(img_src)

# 通过OCR软件识别相关信息，然后进行提取
# 下载图片文件，通过OCR 识别出数字

import ddddocr
ocr=ddddocr.DdddOcr()

res=requests.get('https://'+img_src,headers=headers)

with open('./img.png','wb')as f:
    f.write(res.content)

res1=ocr.classification(res.content)
print(res1)
