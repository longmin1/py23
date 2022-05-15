'''封装基类'''
import time

import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Base():

    base_url=''

    def __init__(self,driver:WebDriver=None):
        if driver:
            self.driver=driver
        else:
            self.driver=webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
        if self.base_url!='':
            self.driver.get(self.base_url)

    def get_screen(self,path):
        timestamp = int(time.time())
        # 注意：！！ 一定要提前创建好images 路径
        # image_path = f"./images/image_{timestamp}.PNG
        image_path=f'{path}/image_{timestamp}.PNG'
        # 截图
        self.driver.save_screenshot(image_path)
        # 讲截图放到报告的数据中
        allure.attach.file(image_path, name="picture",
                           attachment_type=allure.attachment_type.PNG)
    def find(self,by,locator=None):
        if locator:
            return self.driver.find_element(by,locator)
        else:
            return self.driver.find_element(*by)

    def finds(self,by,locator=None):
        if locator:
            return self.driver.find_elements(by,locator)
        else:
            return self.driver.find_elements(*by)

    def send_keys(self,by,input_words,locator=None):
        ele=self.find(by,locator)
        ele.clear()
        ele.send_keys(input_words)




