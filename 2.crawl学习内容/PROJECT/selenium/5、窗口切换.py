'''
iframe是html中常用的一种技术，即一个页面中嵌套了另一个网页，selenium默认是访问不了frame中的内容的，对应
的解决思路是driver.switch_to.frame(frame_element)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://qzone.qq.com/'
driver=webdriver.Chrome()
driver.get(url)

frame=driver.find_element(By.ID,'login_frame')
driver.switch_to.frame(frame)

login=driver.find_element(By.ID,'switcher_plogin')
login.click()

#账号
account=driver.find_element(By.ID,'u')
account.send_keys('2197685543')

#密码
passwd=driver.find_element(By.ID,'p')
passwd.send_keys('lzz18777392734')

#点击登录
login1=driver.find_element(By.ID,'login_button')
login1.click()

input()