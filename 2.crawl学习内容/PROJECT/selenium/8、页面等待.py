'''
页面在加载的过程中需要花费时间等待网站服务器的响应，在这个过程中标签元素有可能还没有加载出来，是不可见的，如何
处理这样的情况
    页面等待的分类：
        1.强制等待（time.slepp()）
            缺点是不智能，设置的时间太短，元素还没有加载出来；设置的时间太长，则会浪费时间
        2.隐式等待（driver.implicitly_wait(10)）
            隐式等待针对的是元素定位，隐式等待设置了一个时间，在一段时间内判断元素是否定位成功，如果完成了，
            就进行下一步（没有定位成功，则会报错）
        3.显示等待
            每经过多少秒就查看一次等待条件是否达成，如果达成就停止等待，继续执行后续代码
            如果没有达成就继续等待直到超过规定的时间后，报超时异常

'''
#隐式等待
from selenium import webdriver

driver=webdriver.Chrome()

driver.implicitly_wait(10)#隐式等待，最长等20秒

driver.get('https://www.baidu.com/')

print(driver.page_source)
print(driver.current_url)


