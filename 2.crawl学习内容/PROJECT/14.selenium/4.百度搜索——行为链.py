from selenium import webdriver # 导入web操控模块
from selenium.webdriver.common.by import By# 获取的操作数据的方法
from selenium.webdriver.chrome .service import Service# 选取exe路径
from selenium.webdriver.common.action_chains import ActionChains# 导入行为链
# from selenium.webdriver.support.ui import Select # 选取下拉参数

s=Service('./chromedriver.exe')
driver=webdriver.Chrome(service=s)# Chrome浏览器

driver.get('https://www.baidu.com/')

action=ActionChains(driver)# 在driver创建行为链对象

a=driver.find_element(By.ID,'kw') # 获取到输入框位置
action.move_to_element(a)# 把鼠标移动到输入框
action.send_keys_to_element(a,'selenium')# 模拟输入

b=driver.find_element(By.ID,'su') # 获取搜索按钮
action.move_to_element(b)# 移动鼠标到搜索按钮
action.click(b)

action.perform()  # 执行行为

input()

driver.close()
