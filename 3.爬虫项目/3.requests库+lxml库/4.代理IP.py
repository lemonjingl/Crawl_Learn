#ip89
# https://www.89ip.cn/index_1.html

#ip66
#http://www.66ip.cn/1.html

#ip3366
#https://proxy.ip3366.net/free/?action=china&page={}

#ip_huan
# https://ip.ihuan.me/?page=b97827cc

# ip_kuai
# https://www.kuaidaili.com/free/inha/1/"

# ip_jiangxi
# https://ip.jiangxianli.com/?page=1

# ip_kaixin
# http://www.kxdaili.com/dailiip/1/1.html

# ip_nima
# http://www.nimadaili.com/putong/1/

import requests
import telnetlib
from lxml import etree
from fake_useragent import UserAgent
ua=UserAgent()

#代理检测函数
def check_ip_port(ip_port):
    for item in ip_port:
        ip=item['ip']
        port=item['port']

        try:
            tn=telnetlib.Telnet(ip,port=port,timeout=3)
        except:
            print('[-] ip:{}:{}'.format(ip,port))
        else:
            print('[+] ip:{}:{}'.format(ip,port))
            with open('ipporxy.txt','a')as f:
                f.write(ip+':'+port+'\n')
    print('阶段性检测完毕')

#方法二:
def check_proxy(ip_port):
    for item in ip_port:
        ip=item['ip']
        port=item['port']

        url='http://icanhazip.com/'
        proxies={
            'http':'http://{}:{}'.format(ip,port),
            'https':'https://{}:{}'.format(ip,port)
        }
        try:
            res=requests.get(url,proxies=proxies,timeout=3)
            if res.status_code==200:
                print(res)
        except Exception as e:
            print(e)


def ip89():
    url='https://www.89ip.cn/index_1.html'
    headers={'User-Agent':ua.chrome}
    res=requests.get(url=url,headers=headers)

    html=etree.HTML(res.text)
    tr=html.xpath('//table/tbody/tr')
    ret=[]
    for i in tr:
        ip=i.xpath('./td[1]/text()')[0].replace('\t','').replace('\n','')
        port=i.xpath('./td[2]/text()')[0].replace('\t','').replace('\n','')
        item_dict={
            'ip':ip,
            'port':port
        }
        ret.append(item_dict)
    check_ip_port(ret)

def ip66():
    urls=['http://www.66ip.cn/index.html']
    for i in range(2,11):
        urls.append(f'http://www.66ip.cn/{i}.html')
    for url in urls:
        headers = {'User-Agent': ua.chrome}
        res = requests.get(url=url, headers=headers)
        res.encoding='gb2312'
        html = etree.HTML(res.text)
        ip_list = html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[1]/text()')[1:]
        port_list=html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[2]/text()')[1:]
        ret = []
        for i in range(len(ip_list)):
            ip=ip_list[i]
            port=port_list[i]
            dict={
                'ip':ip,
                'port':port
            }
            ret.append(dict)
        check_ip_port(ret)
ip66()