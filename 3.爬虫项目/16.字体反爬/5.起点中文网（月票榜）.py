import re

import requests
from lxml import etree
import io
from fontTools.ttLib import TTFont
from fake_useragent import UserAgent
ua=UserAgent()

def res():
    url='https://www.qidian.com/rank/yuepiao/'
    headers={'User-Agent':f'{ua.chrome}'}
    res=requests.get(url,headers=headers)
    text=res.text
    decrypt(text)

def decrypt(text):
    # 字体链接
    html=etree.HTML(text)
    font_url=html.xpath('//style[1]/text()')[0].split("format('eot'); src: url('")[1].split("') format('woff'),")[0]

    font=TTFont(io.BytesIO(requests.get(font_url).content))

    # font.save('./ttf/qdyb5.ttf')
    font.saveXML('./xml/qdyb5.xml')

    # 字典一：
    font_cmap=font.getBestCmap()
    # print(font_cmap)

    # 字典二：
    glyph=font['cmap'].tables[0].ttFont.getGlyphOrder()[1:]
    data_list=['.','0','1','2','3','4','5','6','7','8','9']
    glyph_dict={}
    for k,v in zip(glyph,data_list):
        glyph_dict[k]=v
    # print(glyph_dict)

    # 字典三：
    real_dict={}
    for i in font_cmap:
        real_dict[f'&#{i}']=glyph_dict[font_cmap[i]]
    # print(real_dict)

    # 函数调用
    parse(text,real_dict)
def parse(text,real_dict):
    title=re.findall('<div class="book-mid-info"><h2><a href=".*?" .*? title=".*?">(.*?)</a>',text)
    monthly_list=re.findall('</style>.*?<span class=".*?">(.*?)</span></span>月票</p>',text)
    print(title)
    # print(monthly_list)

    """解密"""
    monthly_list1=[]
    for i in monthly_list:
        # print(i.split(';'))
        monthly_list1.append(''.join([real_dict[j] for j in i.split(';')[:-1]]))
    print(monthly_list1)

if __name__=='__main__':
    res()