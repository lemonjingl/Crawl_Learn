# 目标网站：https://www.oklink.com/cn/btc/tx-list
# 要求：1、使用requests
#           2、抓取：交易哈希,区块,时间,输入,输出,输入数量,手续费
# 提交方式：代码+运行效果截图
import pprint

import requests
import execjs
import re
import base64
import prettytable as tp
import datetime


def get_api():
    with open("3.js", "r") as f:
        js_file = f.read()

    # 获取 API_KEY
    r = requests.get(url="https://static.oklink.com/cdn/assets/okfe/oklink-nav/vender/index.03c3bde2.js").text
    API_KEY = re.findall('this.API_KEY.*?=.*?"(.*?)"', r)[0]

    l = 1111111111111
    # 调用 js
    api_key=execjs.compile(js_file).call('getApiKey',API_KEY,l)
    return api_key


def req_get(url,api_key):
    headers = {
        'referer': 'https://www.oklink.com/cn/btc/tx-list/page/2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-apikey': f'{api_key}',
    }
    params = {
        't': '1707065222432',
        'offset': '0',# 要爬取其它页数修改这个参数，每页增加20
        'txType': '',
        'limit': '20',
        'curType': '',
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_detail_data(data):
    tb = tp.PrettyTable()
    tb.field_names = ['交易哈希','区块','时间','输入','输出','输入数量','手续费']
    for i in data['data']['hits']:
        hash=i['hash']
        block=i['blockHeight']
        time=datetime.datetime.utcfromtimestamp(i['blocktime'])
        input=i['inputsCount']
        output=i['outputsCount']
        inputsValue=str(i['realTransferValue'])+' '+'BTC'
        premium=str(i['fee']/100000000)+' '+'BTC'
        tb.add_row([hash,block,time,input,output,inputsValue,premium])
    print(tb)

if __name__ == '__main__':
    url = 'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict'
    api_key=get_api()
    data=req_get(url,api_key)# 调用请求函数
    get_detail_data(data)

