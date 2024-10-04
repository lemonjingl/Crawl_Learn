# coding = utf-8
import telnetlib
import time

import crawles
import execjs
import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'https://ec.minmetals.com.cn/open/homepage/public'

cookies = {
    'Hm_lvt_f32803886966beff8fa513f7a33dea1e': '1692528938',
    '__jsluid_s': '07df8cc57ed8cfe1ac9f5a3670dd486a',
    'SUNWAY-ESCM-COOKIE': 'ce0f719f-9415-44b7-96a2-8b9b4b501eff',
    'JSESSIONID': '1B8AD140686D233848A930C361958818',
}


headers = {
    'Pragma': 'no-cache',
    'Referer': 'https://ec.minmetals.com.cn/open/home/purchase-info',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': UserAgent().random,
}



def ip66():
    urls=['http://www.66ip.cn/index.html']
    for i in range(21,50):
        urls.append(f'http://www.66ip.cn/{i}.html')
    for url in urls:
        headers = {'User-Agent': UserAgent().random}
        res = requests.get(url=url, headers=headers)
        res.encoding='gb2312'
        html = etree.HTML(res.text)
        ip_list = html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[1]/text()')[1:]
        port_list=html.xpath('//*[@id="main"]/div[1]/div[2]/div[1]/table/tr/td[2]/text()')[1:]
        ret = []
        for i in range(len(ip_list)):
            ip=ip_list[i]
            port=port_list[i]
            dict = {
                'ip': ip,
                'port': port
            }
            ret.append(dict)
        check_ip_port(ret)

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
            proxies = {
                'http': f'http://{ip}:{port}'
            }
            try:
                response = crawles.get(url, proxies=proxies, headers=headers, cookies=cookies)
                time.sleep(3)
                # 查看状态码
                if response.status_code == 200:
                    print(response.text)
                    # with open('demo.js','r',encoding='utf-8')as f:
                    #     js_file=f.read()
                    # param=execjs.compile(js_file).call('main123',response.text,3)

                    print(f'{proxies}可用')
                    break
                else:
                    print(f'{proxies}不可用')

            except Exception as e:
                print(e)
    print('阶段性检测完毕')

ip66()






