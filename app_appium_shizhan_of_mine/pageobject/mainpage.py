from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.address import AddressPage
from app_appium_shizhan_of_mine.pageobject.basepage import BasePage


class MainPage(BasePage):

    def click_addresslist(self):
        '''点击通讯录'''
        self.driver.find_element(By.XPATH,'//*[@text="通讯录"]').click()
        return AddressPage(self.driver)
