import io
import csv
import requests
from fake_useragent import UserAgent
import re
from lxml import etree
from fontTools.ttLib import TTFont

ua=UserAgent()

flag=True
def requests_html(url):
    res=requests.get(url=url,headers={'User-Agent':f'{ua.chrome}'}).text

    # 调用解密函数
    decrypt(res)

def parse(res,real_cmap):
    # 解析书名
    html=etree.HTML(res)
    title_list=html.xpath('//*[@id="book-img-text"]/ul/li/div[2]/h2/a/text()')
    # 解析书的字数
    word=re.findall('<p class="update">(.*?)万字',res,re.S)
    for i,j in zip(word,title_list):
        word_count=re.findall('<span class=".*?">(.*?);</span>',i)[0].split(';')
        title=j

        word_count1=[]
        for i in word_count:
            word_count1.append(real_cmap[i])
        word_count2=''.join(word_count1)+'万字'

        # 调用保存函数
        save(title, word_count2)
    print('保存完成')



def decrypt(res):
    font_url=re.findall("<style>(.*?)</style>",res)[0].split("format('truetype')")[0].split("format('woff'), url('")[1].split("'")[0]
    ttf=TTFont(io.BytesIO(requests.get(url=font_url).content))
    ttf.save('qi.ttf')
    ttf.saveXML('qi.xml')

    # 字典一：得到每个数字对应的字符，并且是按顺序的
    glyph=ttf['cmap'].tables[0].ttFont.getGlyphOrder()[1:]
    str='.0123456789'
    glyph_cmap={k:v for k,v in zip(glyph,str)}

    # 字典二：字体映射关系
    font_cmap = ttf.getBestCmap()

    #字典三
    real_cmap={}

    for k,v in font_cmap.items():
        real_cmap['&#'+f'{k}']=glyph_cmap[v]

    # 调用解析函数
    parse(res,real_cmap)


def save(title,word_count2):
    f = open('qi.csv', 'a+', encoding='GB18030',newline='')
    write = csv.writer(f)
    global flag
    if flag:
        write.writerow(['小说名字','小说字数'])
        flag=False
    write.writerow([title,word_count2])


if __name__=='__main__':
    url='https://www.qidian.com/all/chanId4/'
    requests_html(url)
