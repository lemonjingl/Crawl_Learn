from urllib import parse,request
print(parse.unquote('https%3A%2F%2Fshp%2Eqpic%2Ecn%2Fishow%2F2735010617%2F1672995938%5F1265602313%5F15415%5FsProdImgNo%5F2%2Ejpg%2F200'))
request.urlretrieve('https://shp.qpic.cn/ishow/2735010617/1672995938_1265602313_15415_sProdImgNo_2.jpg/0','a.jpg')