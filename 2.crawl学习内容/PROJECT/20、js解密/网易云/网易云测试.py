import requests
import execjs

url='https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
headers={'User-Agent':'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='}



data={'params': 'JRoveRYPv0Ys8oo9TPCs3yzXawTAC7RwuphOMv3RwLDAxJ7xPBz3Ui69Gl0mX6ulEj6o3pBogMGfulUtBTDAan3e7XW2NgOKeOqd7UERTGYL5jlBbuGseFFTkDePJlQWGtgSDj1dUbC0vRm1Lp0aTQ==',
'encSecKey': '5d0991e110980ef0b8dba3cc5eac59e1237f438ba726b77a57156a516115c4d333154d31648ae9e89e705f721a6bfb6861637c1e56b1289f8000320609b95af1b6451cfc2fa10011a155449ccdac2993b9d2b71dfe7823209322a970dce78308bc138e3e4b24a8d4c4aaa04824ec55cbba4d0f6468950ae58be114054de062c5'
      }

response=requests.post(url=url,data=data,headers=headers)

url_music=response.json()['data'][0]['url']


res=requests.get(url=url_music).content
with open('循迹.mp3', 'wb+')as f:
    f.write(res)