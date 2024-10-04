import base64

import requests
from lxml import etree
import io
from fontTools.ttLib import TTFont
from fake_useragent import UserAgent
ua=UserAgent()

def request():
    url='https://house.leju.com/cq/#wt_source=pc_csss_mf_lpph'
    headers={'User-Agent':f'{ua.chrome}'}
    res=requests.get(url,headers=headers)
    text=res.text

    # 调用函数
    # decrypt(text)
    parse(text)

def decrypt(text):
    '''解密字典'''
    html=etree.HTML(text)
    # 字体链接
    font_url = html.xpath('//style/text()')
    font_file_url = font_url[0].split('src: url(data:font/truetype;charset=utf-8;base64,')[1].split('}')[0].split(')')[0]
    font_f_url = base64.b64decode(font_file_url)


    font = TTFont(io.BytesIO(font_f_url))
    # font.save('./ttf/lj.ttf')
    font.saveXML('./xml/lj.xml')

    # 字典一
    glyth_dict={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    # print(glyth_dict)

    # 字典二
    font_cmap=font.getBestCmap()
    # print(font_cmap)

    # 字典三
    real_dict={}
    list_data=[]
    for i in list(font_cmap.values())[:10]:
        list_data.append(glyth_dict[i])
    # print(list_data)

    for v,k in zip(list_data,list(glyth_dict.values())):
        real_dict[k]=v
    # print(real_dict)
    return real_dict

def parse(text):
    '''解析数据'''
    html=etree.HTML(text)
    address=html.xpath('//div[@class="z_sug_list"]/ul/li/a/div/span/em/text()')
    type1=html.xpath('//div[@class="z_sug_list"]/ul/li/a/div[2]/p[3]/em/text()')
    opening_time=html.xpath('//div[@class="z_sug_list"]/ul/li/a/div[2]/p[1]/text()')
    price=html.xpath('//div[@class="z_sug_list"]/ul/li/a/div[2]/p[2]/em[2]/text()')


    real_dict=decrypt(text)
    true_price_list=[]
    for i in price:
        true_price=''.join([_ if not _.isdigit()  else real_dict[_] for _ in i])
        true_price_list.append(true_price)
    print(f'房型:{type1}')
    print(f'开盘时间:{opening_time}')
    print(f'地址:{address}')
    print(f'价格：{true_price_list}')

request()
