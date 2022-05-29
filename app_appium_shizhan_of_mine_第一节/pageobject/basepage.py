from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage():

    def __init__(self, driver:WebDriver=None):
        self.driver = driver
        if driver==None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.1.2'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            # desired_caps['dontStopAppOnReset']='true'
            # desired_caps['skipDeviceInitialization']='true'
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            desired_caps['noReset'] = 'true'  # 不需要清空缓存的时候可以加上这个
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        else:
            self.driver=driver
            # self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def quit(self):
        self.driver.quit()

    def scroll_wait_ele(self,location):
        '''滑动寻找某元素'''
        while True:
            ele_num = self.driver.find_elements(*location)
            if len(ele_num)>0:
                return self.driver.find_element(*location)
            self.scroll()

    def scroll(self):
        '''从下网上滑动'''
        win_sizes = self.driver.get_window_size()
        win_sizes_width = win_sizes['width']
        win_sizes_height = win_sizes['height']
        self.driver.swipe(win_sizes_width * 0.5, win_sizes_height * 0.9, win_sizes_width * 0.5,win_sizes_height * 0.2, 200)



