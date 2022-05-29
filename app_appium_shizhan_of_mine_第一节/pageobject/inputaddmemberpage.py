from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage


class InputAddMemberPage(BasePage):
    def input_member(self):
        '''输入成员信息，点击保存'''
        self.driver.find_element(By.XPATH,'//*[@text="姓名　"]/..//*[@resource-id="com.tencent.wework:id/bf6"]').send_keys('小花')
        self.driver.find_element(By.XPATH, '//*[@text="手机　"]/..//*[@resource-id="com.tencent.wework:id/ge0"]').send_keys(13882993456)
        self.driver.find_element(By.XPATH,'//*[@text="保存"]').click()
        from app_appium_shizhan_of_mine_第一节.pageobject.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)

