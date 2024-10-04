'''
selenium能够帮助我们出来页面中的cookie，比如获取、删除，接下来我们就学习这部分知识

driver.get_cookies()返回列表，其中包含的是完整的cookie信息！不光有name、value，还有domain等cookie其他维度的
信息，所以如果想要把获取的cookie信息和requests模块配合使用的话，需要转换为name、value作为键值对的cookie字典

'''

from selenium import webdriver

url='https://www.baidu.com/'
driver=webdriver.Chrome()
driver.get(url)

cookies={}
for i in driver.get_cookies():
    cookies[i['name']]=i['value']
print(cookies)


#删除一条cookie
# driver.delete_cookie('CookieName')

#删除所有的cookie
# driver.delete_all_cookies()