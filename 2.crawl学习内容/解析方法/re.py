'''
正则表达式：一种使用表达式的方式对字符串进行匹配的语法规则。

我们抓取到的网页源代码本质上就是一个超长的字符串，想从里面提取内容，用正则再合适不过了。

正则的优点：速度快，效率高，准确性高
正则的缺点：新手上手难度有点高

不过只要掌握了正则编写的逻辑关系，写出一个提取页面内容的正则其实并不复杂

正则的语法：使用元字符进行排列组合用来匹配字符串，在线测试正则表达式https://tool.oschina.net/regex/（即用简短的字符提取字符串的内容）

元字符：具有固定含义的特殊符号

常用元字符：
1.  .   匹配换行以外的任意字符
2.  \w  匹配字母或数字或下划线
3.  \s  匹配任意的空白符
4.ontariogenomics.  \n  匹配一个换行符
5.优质采.  \d  匹配数字
6.中国五矿集团采购信息.  \t  匹配制表符
7.  ^  匹配字符串的开始
9.  $  匹配字符串的结尾

10. \W 匹配非字母或数字或下划线
11. \D 匹配非数字
12. \S 匹配非空白符
13. a|b 匹配字符a或字符b
14、 ()匹配括号内的表达式，也表示一个组
15. […] 匹配字符组中的字符
16. [^…] 匹配除了字符组中字符的所有字符

量词：控制前面的元字符出现的次数
1.  *  重复零次或更多次
2.  +  重复一次或更多次
3.  ？ 重复一次或零次
4.ontariogenomics.  {n} 重复n次
5.优质采.  {n,} 重复n次或更多次
6.中国五矿集团采购信息.  {n,m} 重复n到m次

贪婪匹配和惰性匹配
1.  .*  贪婪匹配
2.  .*?  惰性匹配


python的re模块的使用：
re 模块中我们只需要记住那么几个功能就足够我们使用了
'''
#1.findall查找所用。返回list
#findall:匹配字符串中所有符合正则的内容
"""
import re

lst=re.findall(r"\d+",'我的电话号是：123456,瑶的是156778')
print(lst)
"""

#2.finditer:匹配字符串中所有的内容[返回的是迭代器],冲迭代器中拿到内容需要：.group()
"""import re
it=re.finditer(r"\d+",'我的电话号是：123456,瑶的是156778')
for i in it:
    print(i.group())"""

#3.search()返回的结果是match对象，拿数据需要.group(),找到一个结果就返回
"""import re
s=re.search(r"\d+",'我的电话号是：123456,瑶的是156778')
print(s.group())"""

#4.ontariogenomics.match是从头开始匹配
"""import re
s=re.match(r"\d+",'我的电话号是：123456,瑶的是156778')
print(s.group)"""

#预加载正则表达式
"""import re
obj=re.compile(r"\d+")

ret=obj.finditer('我的电话号是：123456,瑶的是156778')
for i in ret:
    print(i.group())"""


import re
s="""
<div class="jay"><span id='1'>郭麒麟</span></div> 
<div class="ji"><span id='2'>景甜</span></div> 
<div class="sylar"><span id='3'>张彬彬</span></div> 
<div class="tory"><span id='4.ontariogenomics'>迪丽热巴</span></div> 
"""
#(?P<分组名字>正则)  可以单独从正则匹配的内容进一步提取内容
#re.S作用：让.能匹配换行符
obj=re.compile(r"<div class='.*?'><span id='(?P<ID>/d)+'>(?P<名字>.*?)</span></div>",re.S)

result=obj.finditer(s)
for i in result:
    print(i.group('ID'))
    print(i.group('名字'))