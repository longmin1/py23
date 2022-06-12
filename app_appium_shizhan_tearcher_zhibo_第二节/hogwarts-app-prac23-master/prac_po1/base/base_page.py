"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 实例化 driver , find ,finds 。。。。
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from prac_po1.utils.log_util import logger


class BasePage:
    implicitly_wait_time = 30

    def __init__(self, driver: WebDriver = None):
        """
        driver 不希望被暴露出去，
        :param driver:
        """
        self.driver = driver

    def find(self, by, locator):
        """
        查找元素的方法
        :param by:
        :param locator:
        :return:
        """
        logger.info("查找元素 ")
        logger.info(by)
        logger.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def get_toast_text(self):
        toast_text = self.find(AppiumBy.XPATH,
                               "//*[@class='android.widget.Toast']").text
        return toast_text

    def set_implicitly(self, second):
        """
        设置隐式等待时长
        :param second:
        :return:
        """
        self.driver.implicitly_wait(second)

    def get_window_size(self):
        """
        获取屏幕的尺寸
        :return:
        """
        return self.driver.get_window_size()

    def swipe_up(self):
        """
        向上滑动
        :return:
        """
        size = self.get_window_size()
        width = size.get("width")
        height = size.get("height")
        logger.info(f"当前屏幕的宽：{width}, 高：{height}")
        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.3
        duration = 2000
        logger.info(f"开始滑动：{start_x},{start_y} to {end_x},{end_y}")
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def swipe_find(self, text, num=3):
        # 自定义滑动查找
        self.set_implicitly(1)
        for i in range(num):
            try:
                element = self.find(AppiumBy.XPATH, f"//*[@text='{text}']")
                self.set_implicitly(self.implicitly_wait_time)
                return element
            except:
                logger.info("未找到元素，开始滑动")
                self.swipe_up()
            if i == num - 1:
                self.set_implicitly(self.implicitly_wait_time)
                raise NoSuchElementException(f"找了{num}次 ，未找到元素{text}")

    def back(self, num=1):
        """
        返回
        :param num:
        :return:
        """
        for i in range(num):
            self.driver.back()
