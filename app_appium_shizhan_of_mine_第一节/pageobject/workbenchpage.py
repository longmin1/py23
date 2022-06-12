from selenium.webdriver.common.by import By
from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage

class WorkbenchPage(BasePage):
    __CLOCK_ELE=(By.XPATH,'//*[@text="打卡"]')
    def click_clock(self):
        '''点击打卡button'''
        self.driver.find_element(*self.__CLOCK_ELE).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.clockpage import ClockPage
        return ClockPage(self.driver)
