import requests
from lxml import etree
f = open('data1.csv', 'w+', encoding='utf-8')
for i in range(0,100,24):
    url=f'https://www.douguo.com/jingxuan/{i}'

    headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
             }
    response=requests.get(url=url,headers=headers)
    #print(response.text)]
    html=etree.HTML(response.text)
    # print(html.xpath('/html/head'))#从根目录的路径获取
    # print(html.xpath('//body/div'))#相对路径获取数据
    # print(html.xpath('//@id '))
    #
    # #谓语 获取当数据1
    # print(html.xpath('//body/div[1]'))#获取第一个
    # print(html.xpath('//body/div[last()]'))#获取最后一个
    # print(html.xpath('//body/div[last()-1]'))#获取倒数第二个
    # print(html.xpath('//body/div[position()<3]'))#获取前两个
    #
    # print(html.xpath('//div[@class="imublo clearfix"]'))#获取属性

    #  @ 选取属性  /text()获取文本
    # print(html.xpath('//div[@class="imublo clearfix"][1]/a/text()'))
    # print(html.xpath('//div[@class="imublo clearfix"][1]/a/@href'))
    #
    # #  //*任何标签都会获取
    # print(html.xpath('//div[@class="imublo clearfix"][1]/a/text()'))
    #
    # #获取多个结点
    # print(html.xpath('//div|//a'))

    data_1=html.xpath('//ul[@id="jxlist"]/li/div/a[1]/text()')  #菜品名
    data_2=html.xpath('//ul[@id="jxlist"]/li/div/a[2]/img/@alt') #作者名
    data_3=html.xpath('//ul[@id="jxlist"]/li/div/div/span[1]/text()')#浏览量
    data_4=html.xpath('//ul[@id="jxlist"]/li/div/div/span[2]/text()')#收藏量
    data=zip(data_1,data_2,data_3,data_4)#压缩包
    for name,author,numbers,numbers1 in data:#解包
        print(f'{name},{author},{numbers},{numbers1}\n')
        try:
            f.write(f'{name},{author},{numbers},{numbers1}\n')
        except:
            pass
f.close()