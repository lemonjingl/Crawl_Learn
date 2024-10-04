import base64
import re
from hashlib import md5

import requests
import io
from fontTools.ttLib import TTFont
from lxml import etree
from fake_useragent import UserAgent

ua=UserAgent()

def request():
    url='https://ruitengjinshu.cn.china.cn/'
    headers={'User-Agent':f'{ua.chrome}'}
    res=requests.get(url,headers=headers)
    res.encoding='gbk'
    text=res.text

    decrypt(text)
def decrypt(text):
    html=etree.HTML(text)

    font_url=html.xpath('/html/head/style[1]/text()')[0].split('base64,')[1].split("') format")[0]
    # print(font_url)
    font_file_url=base64.b64decode(font_url)

    font=TTFont(io.BytesIO(font_file_url))
    font.save('./ttf/cn6.ttf')
    font.saveXML('./xml/cn6.xml')

    '''
    通过font模块加载字体文件，分别解析两个文件，对比数字1的矢量图部分内容，发现编码不一致，但内容完全相同
    '''
    # 字典一：
    cmap=font.getBestCmap()
    print(cmap)

    # 字典二：
    glyph_dict={}
    data_list=['1','3','9','2','5','0','8','4','6']
    # 将内容一致的部分通过md5加密
    with open('./xml/cn6.xml','r',encoding='utf-8')as f:
        ret=f.read()
    for i,j in zip(cmap,data_list):
        data = re.findall(f'.*?<CharString name="{cmap[i]}">(.*?)</CharString>', ret,re.S)[0]
        char_data=md5(data.encode('utf-8')).hexdigest()
        glyph_dict[char_data]=j
    print(glyph_dict)


    # 字典三：
    real_dict={}
    for i in cmap:
        data1 = re.findall(f'.*?<CharString name="{cmap[i]}">(.*?)</CharString>', ret, re.S)[0]
        char_data1=md5(data1.encode('utf-8')).hexdigest()
        for k in glyph_dict:
            if k==char_data1:
                real_dict['&#x'+cmap[i][3:]]=glyph_dict[k]
    print(real_dict)
    # 调用函数
    parse(text,real_dict)

def parse(text,real_dict):
    phone=re.findall('<span class="phone secret">(.*?)</span>',text)[0].replace(' ','')

    # 解密最后得到的手机号
    phone_data=''.join([real_dict[i] for i in phone.split(';')[:-1]])
    print(phone_data)

    # &#x10072;&#x10073;&#x10074; &#x10075;&#x10075;&#x10076;&#x10072; &#x10077;&#x10073;&#x10078;&#x10073;

request()