'''表单操作'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestFrom():

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_from(self):
        '''测试社区的登录  是在from内表单'''
        self.driver.find_element(By.XPATH,'//*[text()="登录"]').click()
        name_ele=self.driver.find_element(By.CSS_SELECTOR,'#login-account-name')
        name_ele.click()
        name_ele.clear()
        name_ele.send_keys('1987779670@qq.com')
        password_ele=self.driver.find_element(By.CSS_SELECTOR,'#login-account-password')
        password_ele.click()
        password_ele.clear()
        password_ele.send_keys('948406046.lm')
        self.driver.find_element(By.CSS_SELECTOR,'#login-button').click()
