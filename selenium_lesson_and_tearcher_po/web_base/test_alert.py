'''alert弹框处理'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class TestAlert():
    def setup(self):
        self.driver=webdriver.Chrome()
        # self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.action=ActionChains(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drap_ele = self.driver.find_element(By.CSS_SELECTOR, '.ui-draggable')
        drop_ele = self.driver.find_element(By.CSS_SELECTOR, '.ui-droppable')
        print(drap_ele.text, drop_ele.text)
        # self.action.click_and_hold(drap_ele).release(drop_ele).perform()
        self.action.drag_and_drop(drap_ele, drop_ele).perform()  # 使用actionchains拖拽

        # print(self.driver.switch_to.alert.text)#打印alert弹框的文本内容

        self.driver.switch_to.alert.accept()#点击弹框的接受按钮
        # self.driver.switch_to.alert.dismiss()#解散现有的alert弹框，取消
        # self.driver.switch_to.alert.send_keys('这是龙敏弄得文本alert弹框')#发送文本到alert弹框,alert弹框 要有输入框才能用 才能输入

        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.XPATH,'//*[@id="submitBTN"]').click()

