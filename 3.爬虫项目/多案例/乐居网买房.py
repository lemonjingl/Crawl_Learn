import io

from fake_useragent import UserAgent
import requests
from fontTools.ttLib import TTFont
import re
import base64


ua=UserAgent()
def requests_html(url):
    res=requests.get(url=url,headers={'User-Agent':f'{ua.chrome}'}).text
    # 调用解析函数
    # parse(res)
    decrypt(res)
def parse(res):
    price_list=re.findall('<p class="price"><em>(.*?)</em><em  class="new_font">(.*?)</em><i>(.*?)</i></p>',res)
    print(price_list)

def decrypt(res):
    font_url=re.findall('<style>(.*?)</style>',res,re.S)[0].split(';base64,')[1].split(") format('woff');")[0]
    font_url1=base64.b64decode(font_url)
    ttf=TTFont(io.BytesIO(font_url1))
    ttf.save('lj.ttf')
    ttf.saveXML('lj.xml')

    glyph=ttf['cmap'].tables[0].ttFont.getGlyphOrder()
    print(glyph)
    font_cmap=ttf.getBestCmap()
    print(font_cmap)

if __name__=='__main__':
    url='https://house.leju.com/cq/#wt_source=pc_csss_mf_lpph'
    requests_html(url)

