"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from prac_train1.base.bas_page import BasePage
from prac_train1.utils.contact_info import ContactInfo
from prac_train1.utils.log_util import logger

"""
前提条件：
1、提前注册企业微信管理员帐号
2、手机端安装企业微信
3、企业微信 app 处于登录状态
"""


class TestContact(BasePage):

    def test_addcontact(self):
        """
        通讯录添加成员用例步骤:
            进入【通讯录】页面
            点击【添加成员】
            点击【手动输入添加】
            输入【姓名】【手机号】并点击【保存】
        验证点：
            登录成功提示信息
        """
        name = ContactInfo.get_name()
        phonenum = ContactInfo.get_phonenum()
        # 1. 进入【通讯录】页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 2. 点击【添加成员】
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        self.swipe_find("添加成员").click()
        # 3. 点击【手动输入添加】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        # 4. 输入【姓名】
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名' )]/../*[@text='必填']"). \
            send_keys(name)
        # 5. 输入【手机号】
        self.driver.find_element(AppiumBy.XPATH,
                                 '//*[contains(@text,"手机" )]/..//android.widget.EditText'). \
            send_keys(phonenum)
        # 6. 点击【保存】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        # time.sleep(2)
        # print(self.driver.page_source)
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # 验证点：登录成功提示信息
        assert result == "添加成功"

    def wait_text_show(self, text):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.text_to_be_present_in_element((MobileBy.XPATH, f"//*[@text='{text}']"), text))

    def test_delcontact(self):
        """
        进入【通讯录】页面
        点击右上角搜索图标，进入搜索页面
        输入搜索内容（已添加的联系人姓名）
        点击展示的第一个联系人（有可能多个），进入联系人详情页面
        点击右上角三个点，进入个人信息页面
        点击【编辑成员】进入编辑成员页面
        点击【删除成员】并确定
        验证点：搜索结果页面联系人不存在
        :return:
        """
        del_contactname = "cc"
        # 1. 进入通讯录
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 2. 输入搜索内容
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@text='测试公司']/../../../following-sibling::*/*[1]").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@text='搜索']").send_keys(del_contactname)

        result = self.wait_text_show("联系人")
        print(result)
        # 无搜索结果
        if not result:
            pytest.xfail(f"无搜索结果:{del_contactname}")

        # 有搜索结果
        del_contact_locator = (
        MobileBy.XPATH, f"//*[@text='联系人']/../following-sibling::*//*[@text='{del_contactname}']")
        # 点击右上角三个点，进入个人信息页面
        self.driver.find_element(*del_contact_locator).click()
        # 点击【编辑成员】进入编辑成员页面
        self.driver.find_element(MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]").click()
        # 点击【删除成员】并确定
        self.driver.find_element(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.swipe_find("删除成员").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()
        # 重要：验证 删除是否成功！！！！！
        # 等待某个元素消失, 相当于断言
        self.wait_disappear(del_contact_locator)

    def wait_disappear(self, locator):
        # until 等到某个元素出现
        # until 等到某个元素消失
        # 隐式等待 + 显式等待的时候， 隐式等待和显式等待会同时被触发
        # 隐式等待什么时候被触发？？？ 当你调用find_element() 的时候
        self.driver.implicitly_wait(3)
        WebDriverWait(self.driver, 5).until_not(lambda x: x.find_element(*locator))
        self.driver.implicitly_wait(self.implicitly_wait_time)
