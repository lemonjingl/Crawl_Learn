import requests
import re
f=open('data2.csv','w+',encoding='gbk')
for i in range(0,100,24):
    url=f'https://www.douguo.com/jingxuan/{i}'
    headers = {
        'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'}
    response=requests.get(url,headers=headers)

#数据解析
    #菜名dish  作者author  观看数views  收藏数collect
    data_1=re.findall(' <a class="cookname text-lips" href=".*?" target="_blank">(.*?)</a>',response.text)
    data_2=re.findall('<img src="https://tx..douguo.com/upload/photo.*?" alt="(.*?)">',response.text)
    data_3=re.findall('<span class="view">(.*?)</span>',response.text)
    data_4=re.findall('<span class="collect">(.*?)</span>',response.text)
    data=zip(data_1,data_2,data_3,data_4)
    for dish,author,views,collect in data:
        #print(f'{dish},{author},{views},{collect}')
        try:
            f.write(f'{dish},{author},{views},{collect}\n')
        except:
            pass
f.close()
