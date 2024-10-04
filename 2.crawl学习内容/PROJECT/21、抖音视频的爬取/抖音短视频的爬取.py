import re
from pprint import pprint
from urllib import parse,request
import requests
import os

'''
使用tqdm必须知道的几个常见参数：
iterable：可迭代的对象 默认None
total：进度条总长度大小（int or float）默认None
desc：进度条的前缀内容（str）默认None
unit：进度条的单位（str）默认 it ，实际表带为 it/s
'''
if not os.path.exists('./刘所长'):
    os.mkdir('./刘所长')

url='https://www.douyin.com/user/MS4wLjABAAAAFBa-9-LC79kJeX_5ax_yTE4uX_E_43wCuTiiCvc4nSY'
headers={'User-Agent':'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
         'cookie': 'douyin.com; __ac_referer=__ac_blank; ttwid=1%7CpoN8BjPQJ7BkKVqQu2mdqOuSIXFTc1gn7bWOhzmQ-zg%7C1674679675%7Ccf893f1d9b7904f5ec79673521f6bd4cbca8d0bd893f3822f37d0f48753e0ccb; passport_csrf_token=acb91425a3e84fad6b2eb181e87bb930; passport_csrf_token_default=acb91425a3e84fad6b2eb181e87bb930; s_v_web_id=verify_ldc51gs7_ZfcUpb5A_Piy2_4Ivi_9qwG_UR27GkfxMXGO; douyin.com; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1675998074323%2C%22type%22%3A1%7D; csrf_session_id=0343ff671ad63e036892a8a2594219e4; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20230203%22; __ac_signature=_02B4Z6wo00f01ezMD2wAAIDAZ4eUje3Yn13s7AvAABjxdZlp1HWHiozUx-csEfggw.sBG-4GeimIqq7v1-Pj2TLq1kyr9EiB4S0fB7zEnNVVsFmPE37t.ovhfevkLe0qj4UBdFTrbykwxSix7e; msToken=9ZGqPXQ6D4-TRRpIDsb0TcO1fRVQK3mKD_6efy8aKUqFsWDr9jzTF9fRAWax_Xgz8bUHeCw2QXb_dBnYyWo8q82Ug39C4btsjvLJIHWfVQouwVAb97QIwg==; __ac_nonce=063dc916100600f8356d6; _tea_utm_cache_2018=undefined; strategyABtestKey=%221675399554.309%22; home_can_add_dy_2_desktop=%221%22; msToken=Pw-krWu_xaQX-lex63RQ7ftl_Z-GRWAij3QJIHSvtr2Yc5usRyCWA-eF2nmTMWt2eIJQki3vTThaRghvZ5AZCDtItld4kqPdvXNYJJ8bX8_eJqPXgTWLbQ==; tt_scid=HSLoUgpP020rAQs3lNUKQ-tihmIer4vt9mRc5YDguF6WfvN7-IOpuCYpGxqChbPp6f77',
         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
         }
response=requests.get(url=url,headers=headers)
# print(response.text)

data=re.findall(r'<script id="RENDER_DATA" type="application/json">(.*?)</script>',response.text,re.S)[0]
false=False
true=True
null=None
data1=eval(parse.unquote(data))['37']['post']['data']
# pprint(data1)
url_mp4_list=[]

for i in data1:
    # print(i)
    title=i['desc']
    # print(title)
    url_data=i['video']['bitRateList']
    for j in url_data:
        url_mp4='https:'+j['playApi']
    url_mp4_list.append((title,url_mp4))

for title,url_mp4 in url_mp4_list:
    mp4_data=requests.get(url_mp4,stream=True)
    try:
        path='刘所长/'+title+'.mp4'
        f=open(path,'wb')
        f.write(mp4_data.content)
        print(f'{title}爬取成功')
    except Exception as e:
        print(e)
    f.close()
