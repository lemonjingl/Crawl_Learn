# coding = utf-8
import threading

import requests
import re
import csv


cookies = {
    'VLIBSID': 'gkgb4u4agu3susvhq0n214mb3c',
    'VOLSESS': '1687353164',
    'Hm_lvt_032bfff3c38eeefc9db7c70d96d9cae4': '1690353166',
    'Hm_lpvt_032bfff3c38eeefc9db7c70d96d9cae4': '1690353219',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Referer': 'https://kox.moe/l/all,all,all,sortpoint,all,all/2.htm',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '\\',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\\',
}

def main(i):
    url=f'https://kox.moe/l/all,all,all,sortpoint,all,all/{i}.htm'
    response = requests.get(url, headers=headers, cookies=cookies)
    html=response.text

    save(html)
    sem.release()

def save(html):

    title_list = re.findall('<a href=.*? style="font-size:13px;">(.*?)</a> <br />', html)
    score_list = re.findall('<p .*?><b>(.*?)</b></p>', html, re.S)
    href_list = re.findall('<a href=\'(.*?)\' style="padding:0px">', html)
    author_list = re.findall('<font class="pagefoot">(.*?)</font> <br />', html)
    data = zip(title_list, score_list, href_list, author_list)

    csv_file = open('./漫画数据.csv', 'a+', encoding='GB18030',newline='')
    writer = csv.writer(csv_file)

    global flage
    if flage:
        writer.writerow(['漫画名', '评分', '链接', '作者'])
        flage=False
    for title,score,href,author in data:
        try:
            lock.acquire()
            writer.writerow([title,score,href,author])
            lock.release()
            # print(f'{title}保存成功')
        except Exception as e:
            print(e)
    csv_file.close()

if __name__=='__main__':
    flage=True
    lock=threading.Lock()
    sem=threading.BoundedSemaphore(5)
    for i in range(1,101):
        sem.acquire()
        t=threading.Thread(target=main,args=(i,))
        t.start()
        print(f'正在爬取{i}')
    print('爬取成功')
