# coding = utf-8
import crawles

url = 'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort'

cookies = {
    'btoken': 'DOVE7Q72JI8HXKFS2YTFPRFFZF7Z30FA',
    'hy_data_2020_id': '18a0cb62fbb27b-06841bc688d93a-26031c51-921600-18a0cb62fbc4b4',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218a0cb62fbb27b-06841bc688d93a-26031c51-921600-18a0cb62fbc4b4%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218a0cb62fbb27b-06841bc688d93a-26031c51-921600-18a0cb62fbc4b4%22%7D',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1692430381,1692580561',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1692580561',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://www.xiniudata.com',
    'pragma': 'no-cache',
    'referer': 'https://www.xiniudata.com/industry/newest?from=data',
    'sec-ch-ua': '\\',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '\\',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = {
    'payload': 'LBc3V0I6ZGB5bXsxTCQnPRBuAgQVcDhbICcmb2x3AjI=',
    'sig': 'FCC4B7EA5867C7C82AE4CD3E1A7A979D',
    'v': '1',
}

response = crawles.post(url, headers=headers, json=params, cookies=cookies)
print(response.text)
