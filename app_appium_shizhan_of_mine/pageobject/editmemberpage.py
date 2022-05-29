from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage

class EditMemberPage(BasePage):
    def del_member(self):
        del_member=(By.XPATH, '//*[@text="删除成员"]')
        self.scroll_wait_ele(del_member).click()
        self.driver.find_element(By.ID,'com.tencent.wework:id/c0w').click()
        from app_appium_shizhan_of_mine.pageobject.address import AddressPage
        return AddressPage(self.driver)



