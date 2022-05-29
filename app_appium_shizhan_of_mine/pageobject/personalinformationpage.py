from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage

class PersonalInformationPage(BasePage):

    def click_menu(self):
        '''点击个人信息的右上角三点'''
        self.driver.find_element(By.ID,'com.tencent.wework:id/izt').click()
        return self

    def click_edit_member(self):
        self.driver.find_element(By.ID,'com.tencent.wework:id/bn7').click()
        from app_appium_shizhan_of_mine.pageobject.editmemberpage import EditMemberPage
        return EditMemberPage(self.driver)
