# import requests
# from lxml import etree
# import os
#
# if not os.path.exists('./fengjing'):
#     os.mkdir('./fengjing')
#
# url='http://www.netbian.com/fengjing/index_2.htm'
# headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
# res=requests.get(url,headers=headers)
# res.encoding='gbk'
#
# #数据解析
# html=etree.HTML(res.text)
# title=html.xpath('//div[@class="list"]/ul/li/a/img/@alt')
# url_list=html.xpath('//div[@class="list"]/ul/li/a/img/@src')
# data=zip(title,url_list)
#
# for title1,url_detail in data:
#     res1=requests.get(url=url_detail,headers=headers)
#     path='fengjing/'+title1+'.jpg'
#     with open(path,'wb') as f:
#         f.write(res1.content)
#         print(f'{title1}保存完成')


import requests
import re
import os

if not os.path.exists('./fengjing'):
    os.mkdir('./fengjing')

headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

def main():
    url='http://www.netbian.com/fengjing/'
    urls=[f'http://www.netbian.com/fengjing/index_{i}.htm' for i in range(2,11)]
    urls.insert(0,url)
    res=requests.get(url=url,headers=headers)
    res.encoding='gbk'
    return res

def format():
    res=main()
    obj=re.compile('<img src="(?P<url>.*?)" alt="(?P<title>.*?)" />')
    result=obj.finditer(res.text)
    return result


def save():
     result=format()
     for i in result:
         url = i.group('url')
         title = i.group('title')
         res=requests.get(url=url,headers=headers)
         path='fengjing/'+title+'.jpg'
         with open(path,'wb')as f:
             f.write(res.content)
             print(f'{title}保存成功')


if __name__=='__main__':
    save()