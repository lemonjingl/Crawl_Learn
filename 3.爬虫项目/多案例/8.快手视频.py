# 内容：爬取快手短视频和长视频
# 范围：第一页
# 目录链接：https://www.kuaishou.com/
# 格式：存储为mp4文件

import pprint
import re

import requests
import os
from tqdm import tqdm
if not os.path.exists('./快手视频'):
    os.mkdir('./快手视频')



def req(url):
    headers={
        'Content-Type':'application/json',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer':'https://www.kuaishou.com/search/video?searchKey=%E9%9B%AA%E7%8B%97',
        'Cookie':'kpf=PC_WEB; clientid=3; did=web_105ed4adfd1638a203d01f62f95fb3da; kpn=KUAISHOU_VISION',
        'Host':'www.kuaishou.com',
    }
    data={"operationName":"visionSearchPhoto",
          "variables":{"keyword":"考研",
                       "pcursor":"",
                       "page":"search",
                       "searchSessionId":"MTRfMF8xNzA0OTk1MDQ0MTk0X-mbqueLl180OTQz"},
          "query": "fragment photoContent on PhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n}\n\nfragment recoPhotoFragment on recoPhotoEntity {\n  __typename\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  commentCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    ...recoPhotoFragment\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionSearchPhoto($keyword: String, $pcursor: String, $searchSessionId: String, $page: String, $webPageArea: String) {\n  visionSearchPhoto(keyword: $keyword, pcursor: $pcursor, searchSessionId: $searchSessionId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    searchSessionId\n    pcursor\n    aladdinBanner {\n      imgUrl\n      link\n      __typename\n    }\n    __typename\n  }\n}\n"}

    res=requests.post(url,json=data,headers=headers).json()
    return res

def parser(res):
    pprint.pprint(res)
    data=res['data']['visionSearchPhoto']['feeds']
    for i in data:
        title=i['photo']['caption']
        title=re.sub(r'[|/<>?\\|\t|\n]','',title)
        link=i['photo']['manifest']['adaptationSet'][0]['representation'][0]['url']
        save(title,link)

def save(title,link):
    if 'm3u8' in link:
        data = requests.get(link).text
        data = re.sub('#.*', '', data).split()
        with open(f'./快手视频/{title}.mp4', 'wb')as f:
            for i in tqdm(data):
                url_detail = 'https://v4-vod.kwaicdn.com/bs3/video-hls/' + i
                f.write(requests.get(url_detail).content)
                print(f'{title}--长视频--保存成功')

    else:
        with open(f'./快手视频/{title}.mp4', 'wb')as f:
            f.write(requests.get(link).content)
            print(f'{title}--短视频--保存成功')

def main():
    url = 'https://www.kuaishou.com/graphql'
    res=req(url)
    parser(res)

if __name__ == '__main__':
    main()
