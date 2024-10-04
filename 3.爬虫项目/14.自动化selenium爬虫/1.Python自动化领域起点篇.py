'''
selenium项目最早是为了测试浏览器、网页开发的，并且广泛应用于爬虫
selenium不是单个软件，它由一系列的工具组成
selenium与webdriver是两个项目，webdriver是对selenium的二次开发，selenium存在三个大版本，关系如下：
selenium1.0 + webdriver = selenium2.0

'''

#1.webdriver对浏览器基本操作
'''
打开浏览器，关闭浏览器，前进，后退，刷新
'''

# from selenium import webdriver
#
# import time

# driver = webdriver.Chrome('E:\练习\Spider练习\chromedriver.exe')
#
# driver.get('http://www.baidu.com/')#打开百度
#
# time.sleep(1)#暂停1秒
# driver.get('https://www.csdn.net/')
#
# time.sleep(1)
# driver.back()#回退
#
# time.sleep(1)
# driver.forward()#前进
#
# time.sleep(1)
# driver.refresh()#页面刷新
#
# time.sleep(10)
# driver.quit()#关闭浏览器



#2.无头浏览器

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opt=Options()#创建chrom参数对象
opt.add_argument('-headless')

driver=webdriver.Chrome('E:\练习\Spider练习\chromedriver.exe')#创建chrome无界面对象

driver.get('http://www.jianshu.com')#打开简书

title=driver.title
print('网页标题是:',title)

driver.save_screenshot('./jianshu.png')

