from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage

class ClockPage(BasePage):
    __CLOCK_TYPE_LOCATION=(By.XPATH,'//*[@text="外出打卡"]')
    __CLOCK_NUM_ELE=(By.ID,'com.tencent.wework:id/b4k')
    __CLOCK_TEXT_LOCATION=(By.ID,'com.tencent.wework:id/p7')

    def click_Punch_out(self):
        '''点击外出打卡'''
        self.driver.find_element(*self.__CLOCK_TYPE_LOCATION).click()
        self.driver.find_element(*self.__CLOCK_NUM_ELE).click()
        result_text=self.driver.find_element(*self.__CLOCK_TEXT_LOCATION).text
        return result_text
