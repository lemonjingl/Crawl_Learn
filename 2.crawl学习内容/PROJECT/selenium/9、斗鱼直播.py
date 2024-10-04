from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class DouYu(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url='https://www.douyu.com/directory/all'


    def parse_data(self):
        room_list=self.driver.find_elements(By.XPATH,'//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        data_list=[]
        try:
            for i in room_list:
                dict={}
                # dict['image_url'] = i.find_element(By.XPATH, 'a/div[1]/div[1]/picture/img').get_attribute('src')

                dict['title']=i.find_element(By.XPATH,'./a/div[2]/div[1]/h3').text
                dict['type']=i.find_element(By.XPATH,'./a/div[2]/div[1]/span').text
                dict['author']=i.find_element(By.XPATH,'./a/div[2]/div[2]/h2/div').text
                dict['playback']=i.find_element(By.XPATH,'./a/div[2]/div[2]/span').text
                dict['image_url']=i.find_element(By.XPATH,'a/div[1]/div[1]/img').get_attribute('src')
                # data_list.append(dict)
                print(dict)
        except  Exception as e:
            print(e)



    # def data_save(self,data_list):
    #     for data in data_list:
    #         print(data)

    def run(self):
        self.driver.get(self.url)
        time.sleep(3)

        #parse
        self.parse_data()
        #save
        # self.save_data(data_list)

        #next



if __name__=='__main__':
    dou=DouYu()
    dou.run()