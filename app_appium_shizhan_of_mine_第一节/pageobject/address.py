from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app_appium_shizhan_of_mine_第一节.pageobject.basepage import BasePage


class AddressPage(BasePage):
    __ASSMEMBER_LOCATION=(By.XPATH, '//*[@text="添加成员"]')
    __MEMBER_LOCATION=(By.XPATH, '//*[@text="小花"]')
    __SEARCH_ELE=(By.ID,'com.tencent.wework:id/j04')
    __SEARCH_INPUT_LOCATION=(By.ID,'com.tencent.wework:id/hj5')


    def click_add_member(self):
        '''点击添加成员'''

        self.scroll_wait_ele(self.__ASSMEMBER_LOCATION).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.addmemberpage import AddMemberPage
        return AddMemberPage(self.driver)

    def click_member(self):
        '''点击想要删除的那个成员的名字'''

        self.scroll_wait_ele(self.__MEMBER_LOCATION).click()
        from app_appium_shizhan_of_mine_第一节.pageobject.personalinformationpage import PersonalInformationPage
        return PersonalInformationPage(self.driver)

    def search(self,name):
        name_ele=(By.XPATH,f'//*[@text="{name}"]')
        WebDriverWait(self.driver,30).until_not(expected_conditions.visibility_of_element_located(name_ele))
        self.find(self.__SEARCH_ELE).click()
        self.clear_and_send_keys(name,name_ele)
        return len(self.finds(*name_ele))
