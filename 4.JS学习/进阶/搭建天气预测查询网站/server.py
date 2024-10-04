from flask import Flask,render_template,url_for,request
import requests
import json
# ajax最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容

app=Flask(__name__)
city=input('请输入你要查询天气的城市：')

@app.route('/')
def index():
    result = get_weather(city)
    return render_template('index.html',city=result[0],temp=result[1],desc=result[2])

@app.route('/get_data')
def get_data():
    city = request.args.get('city')
    # 添加ua,cookies进行校验，爬虫没有设置这两个，爬虫会报错
    ua=request.headers.get('User-Agent')
    token=request.cookies.get('token')
    data=''
    if 'python' in ua:
        msg='检测到自动化程序'
    if not token or token !='abc':
        msg='Token参数错误'
    else:
        # 爬取天气
        data = get_weather(city)
        msg='请求正常'
    sender_data = {'msg': msg, 'data': data}
    sender_str=json.dumps(sender_data)
    return sender_str

@app.route('/post_data',methods=['POST','GET'])
def post_data():
    msg = '请求正常'
    city = request.json.get('city')
    # 爬取天气
    data = get_weather(city)
    sender_data = {'msg': msg, 'data': data}
    # 将字典变为字符串
    sender_str = json.dumps(sender_data)
    return sender_str

@app.route('/axios')
def axios():
    return '这是一个axios的请求'


def get_city_id():
    url = 'https://weather.cma.cn/api/map/weather/1'

    headers = {
        'Referer': 'https://weather.cma.cn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    data=response.json()
    # 存放城市名称，和城市id
    data_dict={}
    for i in data['data']['city']:
        data_dict[i[1]]=i[0]
    return data_dict

# 爬取天气信息
def get_weather(city):
    data_dict=get_city_id()
    url = f'https://weather.cma.cn/api/now/'+data_dict[city]
    print(url)

    headers = {
        'Referer': 'https://weather.cma.cn/web/weather/57957.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    city = data['data']['location']['name']
    temp = data['data']['now']['temperature']
    desc = data['data']['now']['windDirection'] + ' ' + data['data']['now']['windScale']
    result=[city,temp,desc]
    return result

if __name__ == '__main__':
    app.run()