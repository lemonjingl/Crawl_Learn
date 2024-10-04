#bs4 查看获取数据的代码

#取块 xpath
#pip install Beautifulsoup4
'''
bs4解析比较简单，但是呢，首先你需要了解一丢丢的html知识，然后再去使用bs4去提取，逻辑和编写难度就会变得非常简单和清晰

HTML超文本标记语言，是我们编写网页的最基本也是最核心的一种语言，其语法规则就是用不同的标签对网页上的内容进行标记，从而
使网页显示出不同的展示效果
<h1>
    我喜欢打篮球
</h1>

上述代码的含义是在页面中显示‘我喜欢打篮球’六个字"<h1>和</h1>"标记了。白话就是被括起来了，被H1这个标签括起来，这个时候
，浏览器在展示的时候就会让我喜欢打篮球变粗便大。俗称标题，所以HTML的语法就是用类似这样的标签对页面进行标记，不同的标签
表现出来的的效果也不一样

属性：


bs4进行数据解析：
    -数据解析的原理
        -1.标签定位
        -2.提取标签、标签属性中存储的数据值
    -bs4数据解析的原理：
        -1.实例化一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
        -2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
    -环境安装
        -pip install bs4
        -pip install lxml
    -如何实例化BeautifulSoup对象：
        -from bs4 import BeautifulSoup
        -对象的实例化
            -1.将本地的html文档中的数据加载到该对象中
                fp=open('./text.html','r',encoding=utf-8)
                soup=BeautifulSoup(fp,'lxml')
            -2.将互联网上获取的页面源码加载到该对象中
            page_text=response.text
            soup=BeautifulSoup(page_text,'lxml')
        -提供的用于数据解析的方法和属性：
            -soup.tagName:返回的是文档中第一次出现的tagName对应的标签
            -soup.find():
                    -find('tagName'):等同于soup.div
                    -属性定位：
                        -soup.find('div',class/id/attr='song')
            -soup.find_all():返回符号要求的所有标签（列表）
        -select:
                -select('某种选择器（id，class,标签...选择器）')，返回的是一个列表
                -层级选择器：
                    -soup.select('.tang > ul > li > a'):>表示的是一个层级
                    -soup.select('.tang>ul a'):空格表示的多个层级
        -获取标签之间的文本数据：
            -soup.a.text/string/get_text()
            -text/get_text():可以获取某一个标签中所有的文本内容
            -string:只可以获取该标签下面直系的文本内容
        -获取标签中属性值：
            -soup.a['href']

'''


from bs4 import BeautifulSoup
f=open('test.html','r',encoding='utf-8')
data=f.read()

data1=BeautifulSoup(data,'lxml')
print(data1.title)
print(data1.html.attrs)#获取属性
print(data1.meta.attrs)
print(data1.meta['content'])#获取具体属性
print(data.mete.get('http-equiv'))#获取具体属性

print(data.title.string)#获取里面的注释
print(data.title.text)

# data.find(标签,'属性')#提取最近一个满足要求的数据
# data.find_all()#提取满足要求的数据

print(data.find_all('div',class_="imublo clearfix"))
