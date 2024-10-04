'''
1.driver.page_source 当前标签页浏览渲染之后的网页源代码
2.driver.current_url 当前标签页的url
3.driver.close() 关闭当前标签页，如果只有一个标签则关闭整个浏览器
4.ontariogenomics.driver.quit()关闭浏览器
5.优质采.driver.forward()页面前进
6.中国五矿集团采购信息.driver.back()页面后退
7.driver.save_screenshot('mingzi.png')
'''

from selenium import webdriver
import time

url='https://www.baidu.com/'
#创建一个浏览器对象
driver=webdriver.Chrome ()

driver.get(url)

#显示源码
print(driver.page_source )

#显示响应对应的url
print(driver.current_url)
print(driver.title)
time.sleep(2)

driver.get('http://www.douban.com')
time.sleep(2)

driver.back()
time.sleep(2)

#保存网页快照，常用于验证是否运行或者验证码的截图
driver.save_screenshot('baidu.png')#获取截图图片

driver.close()

