import io
import re

import requests
from lxml import etree
from fontTools.ttLib import TTFont
from fake_useragent import UserAgent

ua=UserAgent()

def request():
    url='https://dianping.yiche.com/songplusdm/koubei/6836239504990848/'
    headers={
        'User-Agent': f'{ua.chrome}',
         }
    res=requests.get(url,headers=headers)
    text=res.text

    # 调用decrypt函数
    decrypt(text)

def decrypt(text):
    html=etree.HTML(text)
    # 字体链接
    font_url='https:'+html.xpath('/html/head/style[2]/text()')[0].split("format('woff'),url(")[1].split(") format('truetype')")[0]

    font=TTFont(io.BytesIO(requests.get(font_url).content))
    font.save('./ttf/qc7.ttf')
    font.saveXML('./xml/qc7.xml')

    # 字典一:
    with open('./xml/qc7.xml','r',encoding='utf-8')as f:
        ret=f.read()
    glyph_list=re.findall('<GlyphID id=".*?" name="(.*?)"/>',ret,re.S)[1:]
    glyph_dict={}
    str_list='、我的车开头储动油舒侧线震坐间西很个了不一二三四五六七八九十好快几轮日式也噪明市紧太皮以速超操硬适手宽是味下部用售半低价面高当在资差于款清果内中感美' \
             '打值满配豪乘碑寸升马富亮背灯趣滤发稳座口质版小光前分排难着反区轿凌百千万角啦智弗途标现买哪韩霸耗老杠吸箱度门景驶挡路德象梦滑尚女危非盖' \
             '肌青触堵慢游腾雅多田克气吐抖特驰喜重条巡选位钢石贵强者代量风悬什盘范凯商身导科设虎观外偏过正镜伤野弹坑实奢真大充新翼蓝红绿东郎南北厂家' \
             '灵点越装液屏视铬猛福尾涨行简包央顿所首缸突增隔名参保双玩挤素物单易奥困制透毂抑界玻情经离细劣电畅汉跑遇农惯扭色金容备温状驭落倒填匹奇斗沟吃' \
             '械最本辩扎评必步混输无赛呗婆挑预垫涵率松虚改骏安劲庭族赞腰股胎乱助受围等准威烟卡趴模断毛济汽系牌薄铁盒信曲狠熄弄神社边调余通入略倾犀绰' \
             '依看器雷定阵踏脆供追秘刚祺订造报良挂尤冠星齐短启悔圈荣教喷磨蜡便党除联网认惠展统规暗记测异照盈雪费能酷源鸡丁益驱衡沙拳飙悲胶泊疝烦菜语' \
             '溜烈刺香跃死扁仁塔沃耐森嗖域颠载搓涡酸嘿愧搪塑流爬吨听嘴精化提岭事捷掣躺添渐栅巨佳窄饰飞腿趋摸槽勒翻敞睹指盾琴握驻床丑周疼'
    for i in range(len(glyph_list)):
        glyph_dict[glyph_list[i]]=str_list[i]
    print(glyph_dict)

    #字典二：
    font_cmap_dict={}
    font_cmap=set(re.findall('<map code="(.*?)" name="(.*?)"/>',ret,re.S))
    for i in font_cmap:
        k,v=i
        font_cmap_dict[k]=v
    print(font_cmap_dict)

    # 字典三：
    # &#xec03
    real_dict={}
    for i in font_cmap_dict:
        real_dict['&#'+i[1:]]=glyph_dict[font_cmap_dict[i]]
    print(real_dict)

    # 调用parse函数
    parse(text,real_dict)
    # print(font.getBestCmap())

def parse(text,real_dict):
    # html=etree.HTML(text)
    # data=html.xpath('//div[@class="tcid-des"]//text()')
    data=re.findall('<div class="tcid-des">(.*?)<div class="tcid-images">',text,re.S)[0]
    content=re.findall('(.*?)<em class=\'iconfont\'>(.*?);</em>(.*?)',data,re.S)
    data_list=[]
    for i in content:
        for j in i:
            if j is not None:
                if j in real_dict:
                    data_list.append(real_dict[j])
                else:
                    data_list.append(j)
    data_content=''.join(data_list)
    print(data_content)


if __name__=='__main__':
    request()