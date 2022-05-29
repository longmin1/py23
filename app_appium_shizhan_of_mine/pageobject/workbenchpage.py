from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage
class WorkbenchPage(BasePage):
    def click_clock(self):
        '''点击打卡button'''
        self.driver.find_element(By.XPATH,'//*[@text="打卡"]').click()
        from app_appium_shizhan_of_mine.pageobject.clockpage import ClockPage
        return ClockPage(self.driver)
