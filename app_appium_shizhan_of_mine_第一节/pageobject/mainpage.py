from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage


class MainPage(BasePage):
    __ADDRESS_ELE=(By.XPATH,'//*[@text="通讯录"]')
    __WORKBENCH_ELE=(By.XPATH,'//*[@text="工作台"]')

    def click_addresslist(self):
        '''点击通讯录'''
        from app_appium_shizhan_of_mine_第一节.pageobject.address import AddressPage
        self.find(self.__ADDRESS_ELE).click()
        return AddressPage(self.driver)

    def click_workbench(self):
        '''点击工作台'''
        self.find(self.__WORKBENCH_ELE).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.workbenchpage import WorkbenchPage
        return WorkbenchPage(self.driver)
