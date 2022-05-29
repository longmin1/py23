from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.address import AddressPage
from app_appium_shizhan_of_mine.pageobject.basepage import BasePage


class MainPage(BasePage):

    def click_addresslist(self):
        '''点击通讯录'''
        self.driver.find_element(By.XPATH,'//*[@text="通讯录"]').click()
        return AddressPage(self.driver)

    def click_workbench(self):
        '''点击工作台'''
        self.driver.find_element(By.XPATH,'//*[@text="工作台"]').click()
        from app_appium_shizhan_of_mine.pageobject.workbenchpage import WorkbenchPage
        return WorkbenchPage(self.driver)