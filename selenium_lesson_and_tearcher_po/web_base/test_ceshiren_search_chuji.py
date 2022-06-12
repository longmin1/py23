#测试人搜索功能测试——录播
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestCeshiren():

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://ceshiren.com/')
        self.driver.maximize_window()

    def teardown(self):
        # pass
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(By.CSS_SELECTOR,'#search-button').click()
        ele=self.driver.find_element(By.CSS_SELECTOR,'#search-term')
        ele.send_keys('appium')
        ele.send_keys(Keys.ENTER)
        time.sleep(3)
        ele.send_keys(Keys.ENTER)

        #find_elements取出所有的结果  返回的是个列表
        search_ele=self.driver.find_elements(By.CSS_SELECTOR,'.topic-title')
        print(search_ele[0].text)
        print(search_ele[1].text)
        print(search_ele[2].text)

        #单独对每个结果进行定位
        # search_ele1_text=self.driver.find_element(By.CSS_SELECTOR,'.topic-title').text
        # search_ele2_text=self.driver.find_element(By.CSS_SELECTOR,'.fps-result-entries>div:nth-child(2) .topic-title').text
        # search_ele3_text=self.driver.find_element(By.CSS_SELECTOR,'.fps-result-entries>div:nth-of-type(3) .topic-title').text
        # print(search_ele1_text,search_ele2_text,search_ele3_text)
        # assert 'appium' in search_ele1_text.lower()
        # assert 'appium' in search_ele2_text.lower()
        # assert 'appium' in search_ele3_text.lower()


