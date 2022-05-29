from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage


class AddressPage(BasePage):

    def click_add_member(self):
        '''点击添加成员'''
        addmember_location = (By.XPATH, '//*[@text="添加成员"]')
        self.scroll_wait_ele(addmember_location).click()
        from app_appium_shizhan_of_mine.pageobject.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)