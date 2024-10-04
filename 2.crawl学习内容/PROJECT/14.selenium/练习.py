from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import  ActionChains
import time

s=Service('./chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.get('https://www.baidu.com/')

action=ActionChains(driver)

a=driver.find_element(By.ID,'kw')
action.move_to_element(a)
action.send_keys_to_element(a,'PYTHON')

b=driver.find_element(By.ID,'su')
action.move_to_element(b)
action.click()

action.perform()

input()




