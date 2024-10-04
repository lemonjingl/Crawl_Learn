# 目标网站：https://bz.zzzmh.cn/index
# 要求：1、使用requests
#           2、抓取页面图片并保存
# 提交方式：代码+运行效果截图

import requests
import execjs
import os
import json
if not os.path.exists('./极简壁纸'):
    os.mkdir('./极简壁纸')

def get_data(url,i):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    params = {
        'size': '24',
        'current': f'{i}',
        'sort': '0',
        'category': '0',
        'resolution': '0',
        'color': '0',
        'categoryId': '0',
        'ratio': '0',
    }

    response = requests.post(url, headers=headers, json=params)
    print(response.text)
    data0=response.json()['result']
    return data0


def get_detail_data(data0,a):
    with open('4.js','r',encoding='utf-8')as f:
        js_file=f.read()
    data=execjs.compile(js_file).call('_0x58b5da',data0)
    b=0
    for i in data['list']:
        b+=1
        link='https://api.zzzmh.cn/bz/v3/getUrl/'+i['i']+'29'
        print(link)
        # 调用保存函数
        save(link,a,b)

def save(link,a,b):
    with open(f'极简壁纸/{str(a)+str(b)}.jpg','wb')as f:
        f.write(requests.get(link).content)
    print(f'第{str(a)+str(b)}张保存成功')


if __name__ == '__main__':
    a=0
    for i in range(1,3):
        a+=1
        url = 'https://api.zzzmh.cn/bz/v3/getData'
        print(f'正在爬取第{i}页')

        data0=get_data(url,i)
        get_detail_data(data0,a)




# 'https://api.zzzmh.cn/bz/v3/getUrl/71e52c67f5094e44b92ccaed93db15c5'
# 'https://api.zzzmh.cn/bz/v3/getUrl/ba41a32b219e4b40ad055bbb5293589629'
# 'https://api.zzzmh.cn/bz/v3/getUrl/5848e4a37f5e4fb39f4c4384a9c2752329'