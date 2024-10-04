import requests
import re
from lxml import etree
dic={}
url='https://www.meishij.net/fenlei/wancan/'
headers = {
        'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
response=requests.get(url,headers=headers)

#数据解析
detail_url=re.findall('<a href="(.*?)" class="list_s2_item_img" .*?></a>',response.text)
for i in detail_url:
    res=requests.get(url=i,headers=headers)
    food_name=re.findall('<h1 class="recipe_title">(.*?)</h1>',res.text)#菜名
    Ingredients=re.findall('<a target="_blank" href="https://www.meishij.net/shicaizuofa/.*?">(.*?)</a>(.*?)</strong>',res.text)#主料
    html=etree.HTML(res.text)
    a=html.xpath('//div[@class="recipe_ingredients recipe_ingredients1"]/div[2]/strong/a/text()')#辅料
    b=html.xpath('//div[@class="recipe_ingredients recipe_ingredients1"]/div[2]/strong/text()')#辅料2
    Accessories2={}
    for i in range(len(a)):
        Accessories2[a[i]]=b[i]
    print(Accessories2)

