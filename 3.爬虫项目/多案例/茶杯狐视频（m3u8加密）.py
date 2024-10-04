# coding = utf-8
import re
from tqdm import tqdm
import requests
from Cryptodome.Cipher import AES

def req(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return response

def get_m3u8(response):
    title=re.findall('<h1 class="movie-list-title">(.*?)</h1>',response.text)[0]
    m3u8_url=re.findall('<script type="text/javascript">(.*?)</script>',response.text)[0].split('"url":')[1].split(',')[0].strip('"').replace('\\','')
    return m3u8_url,title

def get_ts(m3u8_url):
    data=req(m3u8_url).text
    ts_url=re.findall('#EXTINF:5.000000,(.*?)#EXTINF:5.000000,',data,re.S)
    ts_url_list=[]
    for i in ts_url:
        ts_url_list.append(i.strip('\n'))
    return ts_url_list

# 获取密钥
def enc_key():
    url='https://v.gsuus.com/play/QbY0yWKa/enc.key'
    key=req(url).content
    print(key)
    # 解码器
    ci=AES.new(key,AES.MODE_CBC)
    return ci

def save(ts_url_list,title,ci):
    with open(f'./{title}.mp4', 'wb')as f:
        for i in tqdm(ts_url_list):
            content = req(i).content
            content=ci.decrypt(content)# 视频解密
            f.write(content)
    print(f'{title}保存成功')


if __name__ == '__main__':
    # url = 'https://www.bhlsm.com/cupfoxplay/609-3-1/'
    # response=req(url)
    # m3u8_url,title=get_m3u8(response)
    # ts_url_list=get_ts(m3u8_url)# ts链接
    # ci=enc_key()# 获取密钥
    # save(ts_url_list,title,ci)
    enc_key()

# b'u\x0e\xd6\x84C2\x82\r\x01\x14[B\x96\x94\x9d3'