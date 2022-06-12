from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage

class EditMemberPage(BasePage):
    __DEL_MEMBER=(By.XPATH, '//*[@text="删除成员"]')
    __DEL_BUTTON=(By.ID,'com.tencent.wework:id/c0w')
    def del_member(self):

        self.scroll_wait_ele(self.__DEL_MEMBER).click()
        self.find(self.__DEL_BUTTON).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.address import AddressPage
        return AddressPage(self.driver)



