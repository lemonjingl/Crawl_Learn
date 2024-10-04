from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url='https://jn.lianjia.com/'
driver=webdriver.Chrome()
driver.get(url)

for i in range(1,200,5):
    js='window.scrollTo(0,%s)'%(i*100)
    driver.execute_script(js)
    time.sleep(0.3)

input()
driver.close()