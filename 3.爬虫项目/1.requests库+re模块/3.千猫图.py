import requests
import re
import os


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Sat, 17 Jul 2021 05:30:28 GMT',
    'If-None-Match': 'W/',
    'Referer': 'https://link.csdn.net/?target=http%3A%2F%2Fp.ik123.com%2Fzt%2Fmaomi%2F68_1.html',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}
cookies = {
    't': '599ed3a26a340571ed7806a365dc290c',
    'r': '2693',
}

def main(url):
    response = requests.get(url=url, headers=headers)
    response.encoding='gb2312'
    return response

def format(url):
    res=main(url)
    title=re.findall('<img  alt=(.*?) src=".*?">',res.text)
    url_detail=re.findall('<a class=preview href="(.*?)" target=_blank>',res.text)
    data=zip(title,url_detail)
    return data

def save(url):
    data=format(url)
    for title,url_detail in data:
        res=requests.get(url=url_detail,headers=headers,cookies=cookies)
        res.encoding='gb2312'
        # title_list=re.findall('<img alt="(.*?)" src=".*?" />',res.text)
        data_list=re.findall('<img alt="(.*?)" src="(.*?)" />',res.text)
        # print(data_list)

        if not os.path.exists(f'./千猫图/{title}'):
            os.makedirs(f'./千猫图/{title}')
            for i in data_list:
                title_d,url_d=i
                res1=requests.get(url=url_d,headers=headers)
                path=f'千猫图/{title}/{title_d}.jpg'
                with open(path,'wb')as f:
                    f.write(res1.content)
                    print(f'{title_d}保存成功')


if __name__=='__main__':
    url = [f'http://p.ik123.com/zt/maomi/68_{i}.html' for i in range(1, 3)]
    for i in url:
        save(i)
