import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# class Base():
#     def __init__(self):
#         self.driver=webdriver.Chrome()

class TestWindowhandle():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com/')

    def teardown(self):
        self.driver.quit()

    def test_window_handle(self):
        self.driver.find_element(By.CSS_SELECTOR,'#s-top-loginbtn').click()
        self.driver.find_element(By.LINK_TEXT,'立即注册').click()
        windows_handles=self.driver.window_handles#获取窗口的所有句柄
        print(windows_handles)
        print(self.driver.title)#打印当前的title
        print(self.driver.current_window_handle)#打印当前句柄
        self.driver.switch_to.window(windows_handles[-1])#切换到最新的句柄
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_4__userName').send_keys('username...')
        time.sleep(2)
        self.driver.switch_to.window(windows_handles[0])#切换回最开始的句柄去
        self.driver.find_element(By.CSS_SELECTOR,'#TANGRAM__PSP_11__changeSmsCodeItem').click()
        time.sleep(2)
