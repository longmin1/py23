"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.appiumby import AppiumBy

from prac_po1.base.base_page import BasePage
from prac_po1.page.address_list_page import AddressListPage


class MainPage(BasePage):

    def goto_addresslist(self):
        # click 通讯录
        # 1. 进入【通讯录】页面
        self.find_and_click(AppiumBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)
