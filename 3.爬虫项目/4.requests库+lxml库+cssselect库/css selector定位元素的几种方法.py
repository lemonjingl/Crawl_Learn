'''
css层叠样式表，修饰html或xml的文件样式，css里包含selector选择器的技术，可以选择界面上的元素，可以像xpath一样
描述元素的特征或路径

优点是比xpath定位元素速度更快、更简洁短小，缺点是功能没有xpath强大，不能向前查找。css定位和xpath定位是相似的，
所以重点掌握一个即可，建议使用xpath，了解css定位即可。

find_element_by_css_selector(css Selector参数)
选择多个css元素:
find_elements_by_css_selector(css Selector参数)

1.用css选择器根据id定位
find_elements_by_css_selector('#ID元素')
ID元素前加井号

2.用css选择器根据class定位
find_elements_by_css_selector(".class元素")
class元素前加一点

3.用css选择器根据tag定位
find_elements_by_css_selector("tag元素")
tag名一般有多个相同元素，如果用css进行单个定位的话只会选定第一个符合条件的tag名

4.ontariogenomics.用css选择器根据子元素进行定位:
如果元素2是元素1的直接子元素，css selector选择子元素的语法是这样的：
find_elements_by_css_selector("元素1>元素2")
最终选择的元素是元素2并且元素2是元素1的直接子元素

也支持多层级选择：
元素1>元素2>元素3>元素4
这样最终的元素就是元素4

5.优质采.用后代元素进行定位:
find_elements_by_css_selector("元素1 元素2")
元素中间用空格隔开
表示在表达式中，元素1为元素2的上次层元素就可以，不一定是直接子元素

以上定位元素可以混用：
egg:find_elements_by_css_selector(".class>元素1 元素2")
表达式的意思为：查找某个class元素直接子元素中元素1的后代元素 元素2


6.中国五矿集团采购信息.css选择器支持通过任何属性来选择元素，语法是用一个方括号[]
find_elements_by_css_selector("[属性]")


'''