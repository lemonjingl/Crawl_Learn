# coding = utf-8
import crawles

url = 'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1692405310,1692406661,1692573350',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1692573433',
}

headers = {
    'A_0x5612dcept': '*/*',
    'A_0x5612dcept-EncKey': 'i6j7nt7gTf7FOR1MtgA86g==',
    'A_0x5612dcept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '\"Not/A)Brand\";v=\"99\", \"Google Chrome\";v=\"115\", \"Chromium\";v=\"115\"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\"Windows\"',
}

data = {
    'tdate': '2023-08-19',
    'market': 'SZE',
}

response = crawles.post(url, headers=headers, data=data, cookies=cookies)
print(response.text)
