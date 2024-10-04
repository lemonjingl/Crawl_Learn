# 没爬成功


import requests

headers = {
    "content-type": "application/json",
    "user-agent": "Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Referer": "https://www.chacewang.com/chanye/news?newstype=sbtz",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Ni "#这个值每次登录都会切换
}

res = requests.get('https://web.chace-ai.com/api/gov/news/getDetailById/?id=KZwvLqpBVgE5AXB67k4XQY734MnG6ayo', headers=headers)
print(res.text)

