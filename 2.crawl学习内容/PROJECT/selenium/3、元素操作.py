'''
标签对象提取文本内容和属性值
    find_element仅仅能够获取元素，不能够直接获取其中的数据，如果需要获取数据需要使用一下方法
    获取文本element_text
        通过定位获取的标签对象的text属性，获取文本内容
    获取属性值element.get_attribute('属性名')
        通过定位获取的标签对象的get_attribute函数，传入属性名，来获取属性的值
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://gl.58.com/fuwuqi/?PGTID=0d300023-0040-f569-1ff1-d5876f3bae3f&ClickID=9'

driver=webdriver.Chrome()
driver.get(url)

ur=driver.find_elements(By.XPATH,'//*[@id="infolist"]/table/tbody/tr/td[2]/a')

for i in ur:
    print(i.get_attribute('href'))

#ur.click()  能点击的才能点击
#ur.send_keys() 是el text input 的标签才有输入的方法
#ur.clear() 对输入框做清空操作

