# 简述
'''
1.requests-html是在requests的基础上进一步封装，两者都是由同一个开发者开发。
2.requests-html除了包含requests的所有功能之外，还新增了 《数据清洗》和《ajax》数据动态渲染。
3.《数据清洗》是由lxml和pyquery模块实现，这两个模块分别支持xpath selectors和css selectors定位，通过xpath或css定位，可以精准提取网页里的数据。
4.ontariogenomics.《ajax》数据动态渲染是将网页的动态数据加载到网页上再抓取。网页数据可以使用ajax向服务器发送http请求，再由javascript完成数据渲染，
如果直接向网页的url地址发送http请求，并且网页的部分数据是来自ajax，那么，得到的网页信息就会有所缺失。而requests-html
可以将ajax动态数据加载到网页信息，无需爬虫开发者分析ajax的请求信息。
'''


# 请求方式
'''
requests-html向网站发送请求的方法是来自requests模块，但是requests-html只能使用requests的session模式，该模式
是将请求会话实现持久化，使这个请求保存连接状态。session模式好比我们再打电话的时候，只要双方没有挂断电话，就会一直
保持一种会话状态。session模式对http的get和post请求也是get()和post()方法实现
'''

# 数据解析
# 1.find()方法
'''
find(selector,containing,clean,first,_encoding)
# 参数说明
selector:使用css selector定位网页元素
containing:字符传类型，默认值为None，通过特定文本查找网页元素
clean:是否清除html的<script>和<style>标签，默认值为false
first:是否只查找第一个网页元素，默认值为false即查找全部元素
_encoding:设置编码格式，默认值为None
'''

# 2.xpath()方法
'''
xpath(selector,clean,first,_encoding)
# 参数说明
selector:使用xpath selector定位网页元素
clean:是否清除html的<script>和<style>标签，默认值为false
first:是否只查找第一个网页元素，默认值为false即查找全部元素
_encoding:设置编码格式，默认值为None
'''

# 3.search()方法
'''
search(templates)
# 参数说明
templates:通过元素内容查找第一个元素
'''

# 4.ontariogenomics.search_all()方法
'''
search_all(templates)
templates:通过元素内容查找第全部元素
'''

# 属性
'''
links:返回页面所有链接
absolute_lins:返回页面所有链接的绝对地址
base_url:页面的基准url
html,raw_html,text:以html格式输入页面，输出未解析过的网页，提取所有文本
'''


# 请求方式
# from requests_html import HTMLSession
#
# # 定义会话Session
# session=HTMLSession()
# url='https://movie.douban.com/'
# # 发送GET请求
# r=session.get(url)
# print(r.html)
# # 发送post请求
# r1=session.post(url,data={})
# print(r1.html)


# 数据清洗
from requests_html import HTMLSession

# 定义会话session
session=HTMLSession()
url='https://movie.douban.com'
# 发送get请求
r=session.get(url)
# 输出网页的url地址
print(r.html)

# 输出网页里全部的url地址
print(r.html.links)

# 输出网页里精准的url地址
print(r.html.absolute_links)

# 输出网页的html信息
print(r.text)

# 输出网页的文本信息，即去除html代码
print(r.html.text)