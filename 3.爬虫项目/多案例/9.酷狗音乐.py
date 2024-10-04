# 内容：爬取酷狗热门榜单音乐
# 目录链接：https://www.kugou.com/yy/html/rank.html
# 格式：存储为mp3文件

import json
import pprint
import time
import os
if not os.path.exists('./酷狗音乐'):
    os.mkdir('./酷狗音乐')

import requests

def req(url):
    headers = {
        'origin': 'https://www.kugou.com',
        'referer': 'https://www.kugou.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    params = {
        'srcappid': '2919',
        'clientver': '20000',
        'clienttime': f'1705003995096',
        'mid': '843962f5fe2ecf8a092a3d8dfd0021d7',
        'uuid': '843962f5fe2ecf8a092a3d8dfd0021d7',
        'dfid': '4FHvBd1hSTi61zQZHj0OYg6j',
        'appid': '1014',
        'platid': '4',
        'encode_album_audio_id': '9pfkxm94',
        'token': '',
        'userid': '0',
        'signature': '8bf2c6600f44e0ea9e87788b3d501cdc',
    }
    response = requests.get(url, headers=headers, params=params)
    data=json.loads(response.text)
    print(response.text)
    return data
# nze8g5a
# 377b9365881a34156737e75680f43bbe
def parse(data):
    title=data['data']['audio_name']
    link=data['data']['play_url']
    return title,link

def save(title,url):
    with open(f'./酷狗音乐/{title}.mp3','wb')as f:
        f.write(requests.get(url).content)
        print(f'{title}保存成功')

def main():
    url = 'https://wwwapi.kugou.com/play/songinfo'
    data=req(url)
    parse(data)

if __name__ == '__main__':
    main()