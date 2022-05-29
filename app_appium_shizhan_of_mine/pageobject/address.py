from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_appium_shizhan_of_mine.pageobject.basepage import BasePage


class AddressPage(BasePage):

    def click_add_member(self):
        '''点击添加成员'''
        addmember_location = (By.XPATH, '//*[@text="添加成员"]')
        self.scroll_wait_ele(addmember_location).click()
        from app_appium_shizhan_of_mine.pageobject.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)

    def click_member(self):
        '''点击想要删除的那个成员的名字'''
        member_location=(By.XPATH, '//*[@text="小花"]')
        self.scroll_wait_ele(member_location).click()
        from app_appium_shizhan_of_mine.pageobject.personalinformationpage import PersonalInformationPage
        return PersonalInformationPage(self.driver)

    def search(self,name):
        name_ele=(By.XPATH,f'//*[@text="{name}"]')
        WebDriverWait(self.driver,30).until_not(expected_conditions.visibility_of_element_located(name_ele))
        self.driver.find_element(By.ID,'com.tencent.wework:id/j04').click()
        self.driver.find_element(By.ID,'com.tencent.wework:id/hj5').send_keys(name)
        return len(self.driver.find_elements(*name_ele))
