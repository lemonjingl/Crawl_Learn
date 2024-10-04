'''
1.查票程序
2.抢票程序

#GUI界面开发 thkinter
3.界面开发

爬虫基本流程思路：《通用思路  步骤》

1.数据来源分析<确定自己采集网页以及数据内容是什么>
    浏览器自带的工具：开发者工具 f12
    -打开开发者工具  刷新网页
    -通过开发者工具，搜索车次，找到相对应数据包，可以查看请求url地址以及请求方法 请求头

代码实现步骤：
    1.发送请求，模拟浏览器对于url地址<刚刚分析得到url地址>发送请求
    2.获取数据，获取服务器返回响应数据---》response
    3.解析数据，提取我们想要车次信息
    4.ontariogenomics.保存数据
'''

import requests

# import pandas as pd
import prettytable as pt

url='https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-02-24&leftTicketDTO.from_station=GLZ&leftTicketDTO.to_station=NFZ&purpose_codes=ADULT'

headers={
'Cookie': 'JSESSIONID=84B89E3C7B98C4DF9D2758F8DFCFF0B3; RAIL_EXPIRATION=1676334958955; RAIL_DEVICEID=GW0o7uBQ52ge8Zpg6X9-XdWCx8pSB8Vk_3ObUWeFq-s7BR_ru2P5FPPsAahj27yA_VveAKO11aTHdKlNmG6FF1H5BzQRovW_X_ZOYDp-p2LHnTxfMNeYW5ZUoY0KZVoyw1HoEQwLzeoxmB9xGBxpdOjIatG-vjnF; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromStation=%u6842%u6797%2CGLZ; _jc_save_toStation=%u5357%u5B81%u4E1C%2CNFZ; _jc_save_wfdc_flag=dc; BIGipServerotn=2045247754.24610.0000; BIGipServerpassport=803733770.50215.0000; fo=wlcaywuyurp0aub6TsdsA2XEiDTK5XvQSnuJGdI44etJJYOQgPSznngSlTcbUsTr1zlncUKzzpYGMoUrQwW-L05Lz8BOI85xtELxsN00zsB443j974aFhd_cW9UdgUiXY4Ulmi4lL_tEoBKYiddPuCo9jOtXk2QkJFQqXkin_seWLRO-3PTINmb58cA; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromDate=2023-02-25; _jc_save_toDate=2023-02-11',
'User-Agent': 'Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
response=requests.get(url=url,headers=headers)
print(response.json())

num=0
tb=pt.PrettyTable()
tb.field_names=[#设置表头
        '序号',
        '车次 ',
        '出发时间',
         '到达时间',
         '耗时',
         '一等坐座',
         '二等硬卧',
         '二等座',
         '无座',
         '硬座',
    ]
for index in response.json()['data']["result"]:#for循环遍历 把列表里面元素一个一个提取出来
    #字符串分割 split+列表索引取值
    info_list=index.split('|')
    trainNumber=info_list[3]#车次
    start_time=info_list[8]#出发时间
    end_timt=info_list[9]#到达时间
    use_time=info_list[10]#耗时
    first_class=info_list[31]#一等坐
    second_class = info_list[28]#二等硬卧
    second2_class = info_list[30]#二等坐
    no_set=info_list[26]#无坐
    hard_seat=info_list[29]#硬座

    num+=1
    tb.add_row([num,
            trainNumber,
            start_time,
            end_timt,
            use_time,
            first_class,
            second_class,
            second2_class,
            no_set,
            hard_seat,])
print(tb)