"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

from prac_po1.base.base_page import BasePage
from prac_po1.page.add_member_page import AddMemberPage
from prac_po1.utils.log_util import logger


class AddressListPage(BasePage):

    def goto_addmember_page(self):
        # 点击 添加成员
        self.swipe_find("添加成员").click()
        return AddMemberPage(self.driver)
