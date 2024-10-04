# 目标任务
# 任务描述：在指定时间，点击下单购物车里的商品
# 知识点：selenium

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 等待
def timging():
    pass

# 抢购
def buy():
    pass

if __name__ == '__main__':
    service=Service('/chromedriver-win64/chromedriver.exe')
    opt=Options()
    opt.page_load_strategy='eager'
    opt.debugger_address='127.0.0.1:9999'
    driver=webdriver.Chrome(executable_path=service)