import requests
from fontTools.fontBuilder import TTFont
import io
import re

url='https://www.shixiseng.com/interns?page=2&type=intern&keyword=python&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response=requests.get(url=url,headers=headers)

title=re.findall(r'<a href=".*?" target="_blank" class="title ellipsis font" data-v-2d75efc8>(.*?)</a>',response.text)
price=re.findall(r'<span class="day font" data-v-2d75efc8>(.*?)</span>',response.text)

font_url='https://www.shixiseng.com'+re.findall(r'@font-face \{    font-family: myFont;    src: url\((.*?)\);}',response.text)[0]
ttf=TTFont(io.BytesIO(requests.get(font_url).content))
# ttf.save('sxs.ttf')
ttf.saveXML('sxs.xml')

f=open('sxs.xml','r',encoding='utf-8')
xml=f.read()
f.close()
id_name=re.findall(r'<GlyphID id="(.*?)" name="(.*?)"/>',xml)
uni_dict={k:v for v,k in id_name}

map_name=re.findall(r'<map code="(.*?)" name="(.*?)"/>',xml)
map_dict={str(k).replace('0x','&#x'):v for k,v in map_name}
map_list=list(map_dict.keys())


data='0123456789一师X会四计财场DHLPT聘招工d周L端p年hx设程二五天tCG前KO网SWcgkosw广市月个BF告NRVZ作bfjnrvz三互生人政AJEI件M行QUYaeim软qu银y联'
font_list=['','']

for i in data:
    font_list.append(i)

def init_data(data):
    new_list=[]
    for str_i in data:
        for j in map_list:
            str_i=str(str_i).replace(j,font_list[int(uni_dict[map_dict[j]])])
        new_list.append(str_i)
    return new_list

title=init_data(title)
price=init_data(price)

print(title)
print(price)