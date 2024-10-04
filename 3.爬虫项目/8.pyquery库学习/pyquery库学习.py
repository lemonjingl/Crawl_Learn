'''
在用pyquery库解析HTML文本的时候，需要先将其初始化为一个PyQuery对象。
初始化有很多种方法，比如直接传入"字符串"，传入"url"，"文件名称"。
'''
# 一、初始化
# 1.字符串初始化
# from pyquery import PyQuery as pq
# html = '''
# <div>
# <ul>
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
# doc=pq(html)
# print(doc('ul'))

# 2.url初始化
# from pyquery import PyQuery as pq
# doc1=pq(url='https://cuiqingcai.com')
# print(doc1('title'))


# 3.文件初始化
# from pyquery import PyQuery as pq
# doc2=pq(filename='data.html')
# print(doc2('title'))


# 二、数据解析
# 1.基本CSS选择器
# html = '''
# <div id="container">
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))
#
# for item in doc('#container .list li').items():
#     print(item.text())


# 2.查找节点
'''
子节点：查找子节点时，需要用到find方法，其参数是CSS选择器。

其实find方法的查找范围的节点的所有子孙节点。如果只想查找子节点，那么可以用children方法。

如果要筛选所有的子节点中符合条件的节点，例如向筛选出子节点中class为active的节点，则可以向children方法传入class选择器。
'''
# from pyquery import PyQuery as pq
#
# html = '''
# <div id="container">
# <ul class="list">
# <li class="item-0">first item</li>
# <li class="item-1"><a href="link2.html">second item</a></li>
# <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
# <li class="item-1 active"><a href="link4.html">fourth item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a></li>
# </ul>
# </div>
# '''
# doc=pq(html)
# items=doc('.list')
# lis=items.find('li')
# print(lis)
#
# lis1=items.children()
# print(lis1)
#
# lis2=items.children('.active')
# print(lis2)
#
#
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc(".list")
# container = items.parent()
# print(type(container))
# print(container)


# 父节点
# 父节点：我们可以用parent方法获取某个节点的父节点
html = '''
<div id="container">
	<div class="wrap">
	    <ul class="list">
	         <li class="item-0">first item</li>
	         <li class="item-1"><a href="link2.html">second item</a></li>
	         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
	         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
	         <li class="item-0"><a href="link5.html">fifth item</a></li>
	     </ul>
	</div>
 </div>
'''
# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc(".list")
# container = items.parent()
# print(type(container))
# print(container)


# 兄弟节点
# 获取兄弟节点可以用siblings方法
# from pyquery import PyQuery as pq
# doc4=pq(html)
# items=doc4(".list .item-0.active")
# print(items.siblings())
# print(items.text())# 获取文本


# 3.遍历节点
# attr方法获取属性


# 四、节点操作
'''
pyquery库提供了一系列方法对节点进行动态修改，例如为某节点添加一个class，移除某个节点等，有时候这些操作会为提供信息带来极大便利。

addClass 和 removeClass
'''

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

