"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
# 启动， 重启， 关闭
import logging

from appium import webdriver

from prac_po1.base.base_page import BasePage
from prac_po1.page.main_page import MainPage
from prac_po1.utils.log_util import logger


class App(BasePage):

    def start(self):
        # 启动
        # 资源初始化
        # 打开【企业微信】应用
        if self.driver == None:
            # logging.info("driver == None")
            logger.info("driver == None")
            caps = {}
            caps["platformName"] = "Android"
            # mac: adb logcat ActivityManager:I | grep "cmp"
            # windows:adb logcat ActivityManager:I | findstr "cmp"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # adb devices
            caps["deviceName"] = "emulator-5554"
            # "True" 是绝对不可以的  要么是"true" 要么是 True
            # 防止清缓存
            caps["noReset"] = "true"
            # 尽量不要在真实的测试环境下使用，
            caps["dontStopAppOnReset"] = "true"
            # 动态页面等待0秒 再去查找元素， 默认是等待10秒
            caps["settings[waitForIdleTimeout]"] = 0
            # 创建driver ,与appium server建立连接，返回一个 session
            # driver 变成self.driver 由局部变量变成实例变量，就可以在其它的方法中引用这个实例变量了
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # 隐式等待是全局的等待方式
            self.set_implicitly(self.implicitly_wait_time)
        else:
            # logging.info("driver 已存在 ，复用已有driver")
            logger.info("driver 已存在 ，复用已有driver")
            # 会自动的启动desire caps里记录的 页面
            self.driver.launch_app()
            # 启动另外一个app 的页面
            # self.driver.start_activity()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入到首页的入口
        return MainPage(self.driver)
