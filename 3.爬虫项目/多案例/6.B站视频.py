# 内容：爬取B站免费视频
# 链接：https://www.bilibili.com/video
# 格式：分别下载mp3、mp4文件，最后合并成mp4文件

# 运用ffmpeg模块进行合并音频和视频

import pprint
import re

import requests
import json
from lxml import etree
import os
if not os.path.exists('./b站视频'):
    os.mkdir('./b站视频')


"""请求函数"""
def req(url):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return response

"""解析标题，音频、视频链接"""
def parser(response):
    # 标题
    html=etree.HTML(response.text)
    title=html.xpath('//*[@id="viewbox_report"]/h1/text()')[0]

    info=re.findall('window.__playinfo__=(.*?)</script>',response.text,re.S)[0]
    info=json.loads(info)
    # 视频链接
    video_url=info['data']['dash']['video'][1]['baseUrl']
    # 音频链接
    audio_url=info['data']['dash']['audio'][0]['baseUrl']
    return video_url,audio_url,title

"""保存函数"""
def save(video_url,audio_url,title):
    with open(f'./b站视频/{title}.mp4','wb')as f:
        f.write(req(video_url).content)
        print(f'{title}视频保存成功')
    with open(f'./b站视频/{title}.mp3','wb')as f:
        f.write(req(audio_url).content)
        print(f'{title}音频保存成功')

# 合并视频和音频
def combine_files(title):
    cmd=fr"E:\PYTHON\ffmpeg-6.1.1-full_build\bin\ffmpeg -i b站视频\{title}.mp4 -i b站视频\{title}.mp3 -c:v copy -c:a aac -strict experimental b站视频\{title}1.mp4 -loglevel quiet"
    os.system(cmd)
    print('已完成合并')

def main():
    url = 'https://www.bilibili.com/video/BV1R64y1L7zz/'
    response=req(url)
    video_url,audio_url,title=parser(response)
    save(video_url,audio_url,title)
    combine_files(title)

if __name__ == '__main__':
    main()

