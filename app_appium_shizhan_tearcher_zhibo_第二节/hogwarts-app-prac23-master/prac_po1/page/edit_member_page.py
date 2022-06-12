"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.appiumby import AppiumBy

from prac_po1.base.base_page import BasePage


class EditMemeberPage(BasePage):
    def edit_member(self, name, phonenum):
        # input 姓名
        self.find_and_send(AppiumBy.XPATH,
                           "//*[contains(@text,'姓名' )]/../*[@text='必填']",
                           name)

        # 5. 输入【手机号】
        self.find_and_send(AppiumBy.XPATH,
                           '//*[contains(@text,"手机" )]/..//android.widget.EditText',
                           phonenum)
        # 6. 点击【保存】
        self.find_and_click(AppiumBy.XPATH, "//*[@text='保存']")

        from prac_po1.page.add_member_page import AddMemberPage
        return AddMemberPage(self.driver)
