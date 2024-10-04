import base64
import json

import requests
from Crypto.Cipher import AES
# 安装 pip install pycryptodome
# 把python包(python310\Lib\site-packages)文件夹里面的crypto文件夹改成Crypto大写开头
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
param2 = "010001"
param3 = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
param4 = "0CoJUm6Qyw8W8jud"


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text = text.encode("utf-8")
    encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(text)
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text.decode('utf-8')


def analysis(p1, p2, p3, p4):
    res = {}
    rand_num = "aq9d7cvBOJ1tzj1o"
    vi = b"0102030405060708"
    h_enc_text = AES_encrypt(p1, p4, vi)
    h_enc_text = AES_encrypt(h_enc_text, rand_num, vi)
    res["encText"] = h_enc_text
    res[
        "encSecKey"] = "5dec9ded1d7223302cc7db8d7e0428b04139743ab7e3d451ae47837f34e66f9a86f63e45ef20d147c33d88530a6c3c9d9d88e38586b42ee30ce43fbf3283a2b10e3118b76e11d6561d80e33ae38deb96832b1a358665c0579b1576b21f995829d45fc43612eede2ac243c6ebb6c2d16127742f3ac913d3ac7d6026b44cee424e"
    return res


headers = {
    "User-Agent": "Mozilla/5.优质采.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    "Referer": "https://music.163.com/song?id=29004400",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://music.163.com",
    "Host": "music.163.com",
    "cookie": "_ntes_nnid=cd3afc273ef45c3d7aa0c775285f9ed0,1597726095797; _ntes_nuid=cd3afc273ef45c3d7aa0c775285f9ed0; WM_TID=WlT2lbNqsaJBRFQUARY%2BSu%2F6%2BDKEBuyt; WM_NI=t08otfTa3%2FOM5I04rBOzBTpLGKpMhWJN7T1AjcfV0O8qiwfp7bLuv9BCCVitsrGU2%2BVKCFsHyFRO%2BNSaMuZW2AjGzDXYntWnm6kpUgclbQPbPj1E1CGLgn8RYxG%2FZhjrZGY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb5c2468fab89b9c55bf2968fb3d85a868e8faeaa5296b5a8d5e67afc98a7a4db2af0fea7c3b92ab8f0f890f76e98bffdd0ce47f79700d5f14a8da68eb5f3488595c0aeeb5d8a92f9b5b44baabdaab7b345fcafa798e57cf5be8496f533829d8db7ec80b1ae89b6b12196958da7f244bb9a9eb0aa4691bf8396d95df29fa6a8f9509c87a295d666afeaa591d86da1b4aeb2d36a94b6ffa6b4498594a98fbb5a9ba889d0d964aaae96a8dc37e2a3; MUSIC_U=65ee28dc3b6e9410cc6af4a5d83e2e75b2201ad1114547680da968b7b54344b53627cb20f4afc663f83b0952ff3d00a3dd13178cb847ac8487c476919df46603c3061cd18d77b7a0; __remember_me=true; __csrf=47fa3d104922ac31cc290b63b4503c8f; JSESSIONID-WYYY=6Z6H5hBukYauQuJ%5CkbmcG2lbc%2BTD70D%2FcHYjXVr%5Ckl%5CPYpZ%5C2CQ%2FlChH8BndaKk6GnI45Cxc99QS9Xs91JRBQE5kxOXMlKOUifEPdn1EltCIw5VGyIeHmm1DeaYViISp%2FdTqTKIW5wzrFMRPaPXNrWH659%2BfUG2mgrUswFKzVafzkPAO%3A1598355303995; _iuqxldmzr_=33; ntes_kaola_ad=1; playerid=38453663"
}


def ge_ming_func():
    ge_ming = input("请输入歌手/歌名:")
    param1 = json.dumps({"hlpretag": '<span class="s-fc7">',
                         "hlposttag": "</span>",
                         "s": str(ge_ming),
                         "type": "1",
                         "offset": "0",
                         "total": "true",
                         "limit": "30",
                         "csrf_token": "767e5b80fc0f987ca69be2b4f33fcfff"})
    # param1 = json.dumps({"csrf_token": "","ids":"[404784564]","level":"standard","encodeType":"aac"})
    parse_res = analysis(param1, param2, param3, param4)
    url = "https://music.163.com/weapi/cloudsearch/get/web?csrf_token=767e5b80fc0f987ca69be2b4f33fcfff"
    param_data = {"params": parse_res["encText"],
                  "encSecKey": parse_res["encSecKey"]}
    r = requests.post(url, headers=headers, data=param_data, verify=False)
    id_list = []
    name_list = []
    print("序号" + "\t" + "歌名" + "\t" + "歌手")
    c = 1

    for i in json.loads(r.text)["result"]["songs"]:
        if i["name"] == '':
            i["name"] = '无法下载'
        if i["ar"][0]["name"] == '':
            i["ar"][0]["name"] = '无法下载'
        if i["id"] == '':
            i["id"] = '无法下载'
        name = i["name"]
        id_name = i["ar"][0]["name"]
        id_i = i["id"]
        name_list.append(name)
        id_list.append(id_i)
        print(type(name), type(id_name))
        print(str(c) + "\t" + name + "\t" + id_name)
        c += 1
    it = input("请输入要下载的序号:")
    it = int(it) - 1
    num = str([int(id_list[it])])
    param1 = json.dumps({"csrf_token": "", "ids": num, "level": "standard", "encodeType": "aac"})
    parse_res = analysis(param1, param2, param3, param4)
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=767e5b80fc0f987ca69be2b4f33fcfff"
    param_data = {"params": parse_res["encText"],
                  "encSecKey": parse_res["encSecKey"]}
    r = requests.post(url, headers=headers, data=param_data, verify=False)
    url_l = json.loads(r.text)["data"][0]["url"]
    with open(name_list[it] + ".mp3", "wb") as f:
        f.write(requests.get(url_l).content)

ge_ming_func()
