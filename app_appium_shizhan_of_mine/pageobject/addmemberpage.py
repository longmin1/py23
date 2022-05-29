from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage


class AddMemberPage(BasePage):
    def click_add(self):
        '''点击手动添加'''
        self.driver.find_element(By.XPATH,'//*[@text="手动输入添加"]').click()
        from app_appium_shizhan_of_mine.pageobject.inputaddmemberpage import InputAddMemberPage
        return InputAddMemberPage(self.driver)
    def get_toast(self):
        '''获取保存成功toast信息'''
        # page_source=self.driver.page_source
        # print(page_source)
        toast_text=self.driver.find_element(By.XPATH,'//*[@class="android.widget.Toast"]').text
        return toast_text
