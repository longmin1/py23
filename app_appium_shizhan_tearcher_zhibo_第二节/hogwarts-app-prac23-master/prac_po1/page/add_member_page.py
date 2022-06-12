"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 添加成员页面
from appium.webdriver.common.appiumby import AppiumBy

from prac_po1.base.base_page import BasePage


class AddMemberPage(BasePage):
    _add_menual_element = (AppiumBy.XPATH, "//*[@text='手动输入添加']")

    def click_addmember_menual(self):
        # 点击手动输入添加
        self.find_and_click(*self._add_menual_element)

        from prac_po1.page.edit_member_page import EditMemeberPage
        return EditMemeberPage(self.driver)

    def get_text(self):
        result = self.get_toast_text()
        return result
