from selenium.webdriver.common.by import By

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage


class AddMemberPage(BasePage):
    __ADD_MEMBER=(By.XPATH,'//*[@text="手动输入添加"]')
    __TOAST_ELE=(By.XPATH,'//*[@class="android.widget.Toast"]')
    def click_add(self):
        '''点击手动添加'''
        self.find(self.__ADD_MEMBER).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.inputaddmemberpage import InputAddMemberPage
        return InputAddMemberPage(self.driver)
    def get_toast(self):
        '''获取保存成功toast信息'''
        # page_source=self.driver.page_source
        # print(page_source)
        toast_text=self.find(self.__TOAST_ELE).text
        return toast_text
