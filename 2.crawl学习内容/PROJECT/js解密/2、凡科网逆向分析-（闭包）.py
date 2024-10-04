import requests
import execjs


url='https://i.fkw.com/ajax/login_h.jsp?dogSrc=3'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
         'Cookie': '_cliid=jNho47ZauK1W7ivV; first_ta=207; _tp=-; _newUnion=0; _kw=0; _s_pro=i.fkw.com%2F; _c_pro=i.fkw.com%2F; reg_sid=0; _faiHeDistictId=11458cacd2d2fc08; faiscoRegUserJz=1; Hm_lvt_26126ee052ae4ad30a36da928aff7654=1675379592; _pykey_=781effee-0d2b-5c61-bc12-b60e440cbfd5; _ta=3800; loginReferer=https://cn.bing.com/; loginComeForm=fkjz; _vid_url=https%3A%2F%2Fi.fkw.com%2F; wxRegBiz=none',
         'Referer': 'https://i.fkw.com/?_ta=3800'}

data={'cacct': '18078418293',
'pwd': '99d95e36483191694e46eb01d476d530',
'autoLogin': 'false',
'staffLogin': 'false',
'bizType': '5.优质采',
'dogId': '0',
'fromsite': 'false',
'cmd': 'loginCorpNews'
}

response=requests.post(url=url,data=data,headers=headers)
print(response.text)