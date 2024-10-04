'''
selenium能够大幅度降低爬虫的编写难度，但是也同样会大幅降低爬虫的速度，在逼不得已的情况下我们可以使用selenium进行爬虫的编写

selenium是一个Web的自动化测试工具，最初是为了网站自动化测试而开发的，Selenium可以直接调用浏览器，它支持所有主流的浏览器，可以接受指令，
让浏览器自动加载页面，获取需要的数据，甚至页面加载截屏等，我们可以使用selenium很容易完成之前编写的爬虫

'''

import time

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

#尝试传参
from selenium.webdriver.common.by import By

# s=Service(r'E:\PYTHON\pachong\PROJECT\14.selenium\chromedriver.exe')
driver=webdriver.Chrome()

html=driver.get('https://www.baidu.com/')

# inpu=driver.find_element(By.ID,'kw')#id获取
# inpu=driver.find_element(By.NAME,'wd')#name获取
# inpu=driver.find_element(By.CLASS_NAME,'s_ipt')#class获取
inpu=driver.find_element(By.XPATH,'//*[@id="kw"]')#xpath获取
inpu.send_keys('selenium')#在搜索框中输入’selenium'

btn=driver.find_element(By.XPATH,'//*[@id="su"]')
btn.click()#点击百度一下
print(driver.page_source)

time.sleep(5)
#关闭页面
driver.close()
