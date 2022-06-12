'''input标签的文件上传'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileupload():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_file_upload(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.CSS_SELECTOR,'.soutu-btn').click()
        self.driver.find_element(By.CSS_SELECTOR,'.upload-pic').send_keys(r'C:\Users\longmin\Pictures\Saved Pictures\1.jpg')
        sleep(3)
