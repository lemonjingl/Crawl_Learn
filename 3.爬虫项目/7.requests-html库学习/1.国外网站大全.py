
# 获取网站名和网站地址
from requests_html import HTMLSession
session = HTMLSession()

with open('国外网站数据.txt', 'w', encoding='utf-8')as f:
    for i in range(1,11):
        url=f'http://www.world68.com/top.asp?t=5star&page={i}'

        word=session.get(url)

        data=word.html.find('body > div.w.content.sort > div.content_r_sort.r > div.content_r_sort_c > dl')

        for i in data:
            site_name=i.find('dt > a')[0].text
            site_url=i.find('dt > a')[0].attrs['href']
            print(site_name)
            print(site_url)

            f.write(f'{site_name} {site_url}\n')