
import time
from selenium import webdriver
from selenium.webdriver.chrome .service import Service
from selenium.webdriver.common.by import By

s=Service('E:\python\chromedriver.exe')
diver=webdriver.Chrome(service=s)
diver.get('https://tieba.baidu.com/')

ifranme=diver.find_element(By.ID,'iframeu6739266_0')
diver.switch_to.frame(ifranme)

btn=diver.find_element(By.ID,'title0')
btn.click()

time.sleep(20)
# input()
diver.close()
