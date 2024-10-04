# 目标网站：https://www.endata.com.cn/BoxOffice/BO/Year/index.html
# 要求：1、使用requests
#           2、抓取：电影排行，影片名称，类型，总票房，平均票价，场次人数，国家，上映时间
# 提交方式：代码+运行效果截图

import requests
import execjs
import prettytable as tp

def get_data(url,year):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    }

    data = {
        'year': f'{year}',
        'MethodName': 'BoxOffice_GetYearInfoData',
    }

    response = requests.post(url, headers=headers, data=data)
    return response

def get_detail_data(response):
    tb=tp.PrettyTable()
    tb.field_names = ['电影排行','影片名称','类型','总票房','平均票价','场次人数','国家','上映时间']
    with open('2.js','r',encoding='utf-8')as f:
        js_file=f.read()

    data=execjs.compile(js_file).call('de_data',response.text)
    rank0=1
    for i in data['Table']:
        rank=rank0
        moviename=i['MovieName']
        type=i['Genre_Main']
        Total_box_office=i['BoxOffice']
        avg_ticket_price=i['AvgPrice']
        number_people=i['AvgPeoPle']
        country=i['Area']
        showtime=i['ReleaseTime']
        rank0+=1
        tb.add_row([rank, moviename, type, Total_box_office, avg_ticket_price,number_people,country,showtime])
    print(tb)

if __name__ == '__main__':
    url = 'https://www.endata.com.cn/API/GetData.ashx'
    year=input('输入你想爬取哪年的年度票房的年份：')
    response=get_data(url,year)
    get_detail_data(response)