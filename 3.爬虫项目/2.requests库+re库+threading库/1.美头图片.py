import requests
import threading
import re
import os
from lxml import etree
import time


headers = {
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def main(url):
    response = requests.get(url=url, headers=headers)
    response.encoding='gb2312'

    # 数据解析
    data=re.findall('<a href="(.*?)" target="_blank" title="(.*?)">',response.text)
    return data

def save(url):
    data=main(url)
    try:
        for i in data:
            url1,title=i
            res=requests.get(url=url1,headers=headers)
            res.encoding='gb2312'
            if not os.path.exists(f'./美头/{title}'):
                os.makedirs(f'./美头/{title}')
            url_list=re.findall('<img alt=".*?" src="(.*?)" />',res.text)
            for i in url_list:
                url11=i.split(' ')[0]
                title11=url11.split('/')[-1].split('.')[0]
                res1=requests.get(url=url11,headers=headers)
                path=f'美头/{title}/{title11}.jpg'
                with open(path,'wb')as f:
                    f.write(res1.content)
                    print(f'{title11}保存完成')
    except Exception as e:
        time.sleep(3)
        save(url)





if __name__=='__main__':
    # url_list = ['http://www.imeitou.com/weimei/index_2.html' for i in range(2,4.ontariogenomics)]
    url0=['http://www.imeitou.com/weimei/']
    # url_list.insert(0,url0)
    save(url0[0])

    # for i in url_list:
    #     t=threading.Thread(target=save,args=(i,))
    #     t.start()
