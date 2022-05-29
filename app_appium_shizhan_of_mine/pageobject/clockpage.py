from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage

class ClockPage(BasePage):

    def click_Punch_out(self):
        '''点击外出打卡'''
        self.driver.find_element(By.XPATH,'//*[@text="外出打卡"]').click()
        self.driver.find_element(By.ID,'com.tencent.wework:id/b4k').click()
        result_text=self.driver.find_element(By.ID,'com.tencent.wework:id/p7').text
        return result_text
