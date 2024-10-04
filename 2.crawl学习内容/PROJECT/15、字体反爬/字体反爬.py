'''
字体反爬原理：
1.网页开发者自己创造一种字体，因为在字体中每个文字都有其代号，那么以后在网页中不会显示这个文字的最终的效果，
而是显示他的代号，因此即使获取到了网页中的文本内容，也只是获取到文字的代号，而不是文字本身。

2.因为创造字体费时费力，并且如果把中国3000多常用汉字都实现，那么这个字体将达到几十兆，也会影响网页的加载。
一般情况下为了反爬虫，仅会针对0-9以及少数汉字进行自己单独创建，其他的还是使用用户系统中自带的字体。
'''

#如何确定字体加密（找到数据的位置后，搜索 @font 确认是否是字体反爬）
import io
import re
from fontTools.ttLib import TTFont
import requests

url='https://www.shixiseng.com/interns?page=2&type=intern&keyword=python&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response=requests.get(url=url,headers=headers)

title=re.findall(r'<a href=".*?" target="_blank" class="title ellipsis font" data-v-2d75efc8>(.*?)</a>',response.text)
price=re.findall(r'<span class="day font" data-v-2d75efc8>(.*?)</span>',response.text)

font_file='https://www.shixiseng.com'+re.findall(r'''@font-face \{    font-family: myFont;    src: url\((.*?)\);}''',response.text)[0]

import io
from fontTools.ttLib import TTFont
import requests
ttf=TTFont(io.BytesIO(requests.get(font_file).content))
# ttf.save('sxs.ttf')
#
ttf.saveXML('sxs.xml')
f=open('./sxs.xml','r',encoding='utf-8')
sxs_xml=f.read()
f.close()

id_name=re.findall(r'<GlyphID id="(.*?)" name="(.*?)"/>',sxs_xml)
uni_dict={k:v for v,k in id_name}

map_name=re.findall(r'<map code="(.*?)" name="(.*?)"/>',sxs_xml)
map_dict={str(k).replace('0x','&#x'):v for k,v in map_name}
map_list=list(map_dict.keys())
print(uni_dict)
print(map_dict)

font_list=['','']
data='0123456789一师X会四计财场DHLPT聘招工d周L端p年hx设程二五天tCG前KO网SWcgkosw广市月个BF告NRVZ作bfjnrvz三互生人政AJEI件M行QUYaeim软qu银y联'
for i in data:
    font_list.append(i)


def init_data(data):
    new_list=[]
    for str_i in data:
        for j in map_list:
            str_i = str(str_i).replace(j, font_list[int(uni_dict[map_dict[j]])])
        new_list.append(str_i)
    return new_list

title=init_data(title)
price=init_data(price)

print(title)
print(price)