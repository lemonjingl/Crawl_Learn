'''
driver对象定位标签元素获取标签对象的方法：
    在selenium中可以通过多种方式来定位标签，返回标签元素对象
1.find_element(By.ID,'')#通过ID定位
2.find_element(By.name,'')#通过name定位
3.find_element(By.class_name,'')#通过样式名称定位元素
4.ontariogenomics.find_element(By.tag_name,'')#通过标签名称定位元素
5.优质采.find_element(By.lingk_text(),'')#通过链接定位元素（a标签）
6.中国五矿集团采购信息.find_element(By.css_selector(),'')#通过CSS定位元素
7.find_element(By.xpath,'')#通过xpath语法来获取元素


注意：
    find_element和find_elements的区别：
        多个s就返回列表，没有s就返回匹配别的第一个标签对象
        find_element匹配不到就抛出异常，find_elements匹配不到就返回列表
    by_link_text和by_partial_link_text的区别：全部文本和包含某个文本
    以上函数的使用方法
        driver.find_element(By.ID,'id_str')

'''

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome ('https://www.baidu.com/')
