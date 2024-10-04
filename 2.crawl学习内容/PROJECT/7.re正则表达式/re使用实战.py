import re

data='''
                            <div class="imublo clearfix">
                                <a href="/caipu/家常菜" target="_blank">家常菜</a>
                                <a href="/caipu/热菜" target="_blank">热菜</a>
                                <a href="/caipu/凉菜" target="_blank">凉菜</a>
                                <a href="/caipu/主食" target="_blank">主食</a>
                                <a href="/caipu/汤" target="_blank">汤</a>
                                <a href="/caipu/早餐" target="_blank">早餐</a>
                                <a href="/caipu/午餐" target="_blank">午餐</a>
                                <a href="/caipu/海鲜" target="_blank">海鲜</a>
                                <a href="/caipu/孕妇" target="_blank">孕妇</a>
                                <a href="/caipu/甜品" target="_blank">甜品</a>
                                <a href="/caipu/粥" target="_blank">粥</a>
                                <a href="/caipu/宝宝食谱" target="_blank">宝宝食谱</a>
                                <a href="/caipu/糕点" target="_blank">糕点</a>
                                <a href="/caipu/微波炉" target="_blank">微波炉</a>
                            </div>
'''

# str_data='<meta charset="UTF-8">'
# print(re.findall('<meta charset="(.*?)"',str_data))

print(re.findall('>(.*?)<',data))
print(re.findall('<a href="(.*?)" target',data))