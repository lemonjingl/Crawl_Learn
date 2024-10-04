import requests
#转成字节流  .content
#二进制的爬取

#确认数据的链接
#url:https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
response=requests.get(url=url)
#stream=True时，如果是下载大的文件时，用True，可以先对请求的类型进行判断，如果时大文件，可以中止请求，而不用浪费大流量开销。
#当stream=False时，如果是请求的大文件，其当其会进入内存并进行下载，消费大量的内存和流量
f=open('百度logo.jpg','wb+')
f.write(response.content)
f.close()