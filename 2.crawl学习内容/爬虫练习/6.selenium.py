from selenium import webdriver
from selenium.webdriver.common.by import By

drive=webdriver.Chrome()
drive.get('https://www.baidu.com/')
inpu=drive.find_element(By.ID,'kw')
inpu.send_keys('python')

clic=drive.find_element(By.ID,'su')
clic.click()



