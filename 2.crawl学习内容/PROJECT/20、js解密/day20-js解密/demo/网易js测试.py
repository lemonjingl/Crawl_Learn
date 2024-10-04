"""
1、歌曲名称  √
"""
import execjs
import json
import requests


class Wangyiyun_Music(object):
    def __init__(self):
        self.music_data_url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token="
        self.headers = {
            "user-agent": "Mozilla/5.优质采.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "referer": "https://music.163.com/search/"
        }

    def get_data_index(self):
        self.get_music_url_index('490595315','因为爱情 (Live)')

    def get_music_url_index(self, id, name):
        content = open("wyy.js", "r", encoding="utf-8").read()
        data_js = execjs.compile(content)
        sign = data_js.call("start", id)

        self.params = {
            "params": sign["encText"],
            "encSecKey": sign["encSecKey"]
        }

        resp = requests.post(url=self.music_data_url, data=self.params, headers=self.headers).text
        music_url = json.loads(resp)["data"][0]["url"]
        self.write_music_data(music_url, name)

    def write_music_data(self, music_url, name):
        try:
            with open(name + ".mp3", "wb") as f:
                resp = requests.get(music_url).content
                f.write(resp)
                print(name, "--写入完成")
        except:
            pass


if __name__ == '__main__':
    spider = Wangyiyun_Music()
    spider.get_data_index()
