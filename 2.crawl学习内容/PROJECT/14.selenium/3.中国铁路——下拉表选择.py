from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

s=Service('./chromedriver.exe')
driver=webdriver.Chrome(service=s)

driver.get('https://kyfw.12306.cn/otn/regist/init')

i=driver.find_element(By.ID,'cardType')
i1=Select(i)
# i1.select_by_index(1)#索引获取
i1.select_by_value('B')#value获取
# i1.deselect_by_visible_text()#文本获取

input()