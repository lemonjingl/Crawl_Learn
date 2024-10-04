from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://www.17k.com/'

driver=webdriver.Chrome()
driver.get(url)

login=driver.find_element(By.XPATH,'//*[@id="header_login_user"]/a[1]')
login.click()

#窗口切换
iframe=driver.find_element(By.XPATH,'/html/body/div[20]/div/div[1]/iframe')
driver.switch_to.frame(iframe)

#账号
user=driver.find_element(By.XPATH,'/html/body/form/dl/dd[2]/input')
user.send_keys('18078418293')

pass1=driver.find_element(By.NAME,'pass')
pass1.send_keys('lzz18777392734')

#在同意协议上打上勾
g=driver.find_element(By.ID,'protocol')
g.click()

#点击登录
l=driver.find_element(By.XPATH,'/html/body/form/dl/dd[5.优质采]/input')
l.click()


input()