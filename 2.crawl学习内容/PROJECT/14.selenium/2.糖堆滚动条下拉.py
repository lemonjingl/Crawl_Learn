import time
from selenium import webdriver
from selenium.webdriver.chrome .service import Service
from selenium.webdriver.common.by import By

s=Service('./chromedriver.exe')
drive=webdriver.Chrome (service=s)

drive.get('https://www.duitang.com/category/?cat=travel')
#实现网页下拉
for i in range(1,200,5):
    js='window.scrollTo(0,%s)'%(i*100)
    drive.execute_script(js)
    time.sleep(0.3)

input()
print(drive.page_source)