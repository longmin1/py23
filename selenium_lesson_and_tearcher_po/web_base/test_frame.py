'''frame框的处理'''
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class Base():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.action=ActionChains(self.driver)

    def teardown(self):
        self.driver.quit()

class TestFrame(Base):

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drap_ele=self.driver.find_element(By.CSS_SELECTOR,'.ui-draggable')
        drop_ele=self.driver.find_element(By.CSS_SELECTOR,'.ui-droppable')
        print(drap_ele.text,drop_ele.text)
        # self.action.click_and_hold(drap_ele).release(drop_ele).perform()
        self.action.drag_and_drop(drap_ele,drop_ele).perform()#使用actionchains拖拽
        time.sleep(3)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()#退出frame框
        self.driver.find_element(By.XPATH,'//*[@id="submitBTN"]').click()




