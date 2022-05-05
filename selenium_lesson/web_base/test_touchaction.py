'''TouchAction'''
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

class TestTouchaction():

    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.action=TouchActions(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        '''打开百度，搜索框输入selenium测试
        通过TouchAction 点击搜索框，滑动到最底部，点击下一页'''
        ele=self.driver.find_element(By.CSS_SELECTOR,'#kw')
        ele.send_keys('selenium测试')
        seach_ele = self.driver.find_element(By.CSS_SELECTOR, '#su')
        self.action.tap(seach_ele).perform()
        self.action.scroll_from_element(ele,0,10000).perform()
        self.action.tap(self.driver.find_element(By.XPATH,'//a[text()="下一页 >"]')).perform()
        sleep(3)


