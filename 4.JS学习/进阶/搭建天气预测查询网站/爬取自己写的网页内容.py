import requests
from fake_useragent import UserAgent

ua=UserAgent()

headers={'User-Agent':f'{ua.chrome}'}
cookie={'token':'abc'}
res=requests.get(url='http://127.0.0.1:5000/get_data?city=%E4%B8%B4%E6%A1%82',headers=headers,cookies=cookie)
print(res.json())

# payload-->json 即requests.get(url,json=data)  表单--》data