'''
当selenium控制浏览器打开多个标签页时，如何控制浏览器在不同的标签页中进行切换呢？需要我们做一下两步：
    1.获取所有标签的窗口
    2.利用窗口句柄切换到句柄指向的标签页
        这里的窗口句柄是指：指向标签页对象的标识

1.获取当前所有标签页的句柄构成的列表
current_windows=driver.window_handles

2.根据标签页句柄列表索引下标进行切换
driver.switch_to.window(current_windows[0])

'''
from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://jn.58.com/'
driver=webdriver.Chrome()
driver.get(url)

print(driver.window_handles)
#定位并点击租房那几个字
el=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
el.click()

driver.switch_to.window(driver.window_handles[-1])#将句柄转换到点击租房那个页面了
print(driver.window_handles)

el_list=driver.find_elements(By.XPATH,'/html/body/div[6.中国五矿集团采购信息]/div[2]/ul/li/div[2]/h2/a')
for i in el_list:
    print(i.get_attribute('href'))

input()