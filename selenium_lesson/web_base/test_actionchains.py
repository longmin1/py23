import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionchains:

    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.action = ActionChains(self.driver)
    def teardown(self):
        self.driver.quit()

    def test_action_click(self):
        '''点击，右键，双击'''
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        ele_click=self.driver.find_element(By.CSS_SELECTOR,'[value="click me"]')
        ele_right_click=self.driver.find_element(By.XPATH,'//input[@value="right click me"]')
        ele_double_click=self.driver.find_element(By.XPATH,'//input[@value="dbl click me"]')
        self.action.click(ele_click).pause(1)
        self.action.context_click(ele_right_click).pause(1)#右键
        self.action.double_click(ele_double_click).pause(1)
        self.action.perform()

    def test_move_to_element(self):
        '''鼠标移动到某个元素上'''
        self.driver.get('https://www.baidu.com/')
        print(self.driver.find_element(By.CSS_SELECTOR,'#su').text,'vvvvvv ')
        ele=self.driver.find_element(By.XPATH,'//div[@class="s-top-right s-isindex-wrap"]/span')
        time.sleep(3)
        self.action.move_to_element(ele)
        self.action.perform()
        time.sleep(3)

    def test_drag_drop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_ele=self.driver.find_element(By.XPATH,'//div[@id="dragger"]')
        drop_ele=self.driver.find_elements(By.XPATH,'//div[@class="item"]')#find_elements 一次获取下面四个表格的定位，返回是个列表
        for i in drop_ele:
            '''三种拖拽写法'''
            # self.action.drag_and_drop(drag_ele,i).pause(2)
            # self.action.click_and_hold(drag_ele).release(i).pause(2)
            self.action.click_and_hold(drag_ele).move_to_element(i).release().pause(2)
        self.action.perform()

    def test_keys(self):
        '''键盘操作'''
        self.driver.get('https://sahitest.com/demo/label.htm')
        name_list=[]
        first_name_ele=self.driver.find_element(By.XPATH,'//label/input')
        last_name_ele=self.driver.find_element(By.XPATH,'//td/input')
        name_list.append(first_name_ele)
        name_list.append(last_name_ele)
        for i in name_list:
            self.action.click(i)
            self.action.send_keys('username').pause(2)
            self.action.send_keys(Keys.SPACE).pause(2)
            self.action.send_keys('longmin').pause(2)
            self.action.send_keys(Keys.BACK_SPACE)
        self.action.perform()


if __name__ == '__main__':
    pytest.main(['-vs','test_actionchains.py::TestActionchains::test_keys'])
