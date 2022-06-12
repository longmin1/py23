from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage

class PersonalInformationPage(BasePage):
    __MENU_LOCATION=(By.ID,'com.tencent.wework:id/izt')
    __EDIT_MEMBER_LOCATION=(By.ID,'com.tencent.wework:id/bn7')

    def click_menu(self):
        '''点击个人信息的右上角三点'''
        self.find(self.__MENU_LOCATION).click()
        return self

    def click_edit_member(self):
        self.find(self.__EDIT_MEMBER_LOCATION).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.editmemberpage import EditMemberPage
        return EditMemberPage(self.driver)
