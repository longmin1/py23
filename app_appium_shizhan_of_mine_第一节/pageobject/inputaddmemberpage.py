from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage


class InputAddMemberPage(BasePage):
    __INPUT_USERNAME = (By.XPATH,'//*[@text="姓名　"]/..//*[@resource-id="com.tencent.wework:id/bf6"]')
    __INPUT_PHONE = (By.XPATH, '//*[@text="手机　"]/..//*[@resource-id="com.tencent.wework:id/ge0"]')
    __SAVE_ELE=(By.XPATH,'//*[@text="保存"]')

    def input_member(self):
        '''输入成员信息，点击保存'''
        self.clear_and_send_keys('小花',self.__INPUT_USERNAME)
        self.clear_and_send_keys('13882993456', self.__INPUT_PHONE)
        self.find(self.__SAVE_ELE).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)

