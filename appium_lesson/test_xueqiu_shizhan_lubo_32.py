'''雪球 app自动化测试实战_录播_32分钟
练习：打开雪球
    点击搜索框【点击之前，判断搜索框的是否可用，并查看搜索框name属性值，并获取搜索框坐标，以及它的宽高】
    向搜索框输入：alibaba
    判断【阿里巴巴】是否可见
    如果可见，打印’搜索成功‘
    如果不可见，打印’搜索失败‘
'''
from appium import webdriver
from selenium.webdriver.common.by import By


class TestXueqiu():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.main.view.MainActivity'
        # desired_caps['dontStopAppOnReset']='true'
        # desired_caps['skipDeviceInitialization']='true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'  # 不需要清空缓存的时候可以加上这个
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_xueqiu(self):
        search_ele=self.driver.find_element(By.ID,'com.xueqiu.android:id/home_search')
        search_ele_enable=search_ele.is_enabled()
        search_ele_text=search_ele.text
        search_ele_location=search_ele.location
        search_ele_size=search_ele.size
        print(f'【搜索框】是否可用:{search_ele_enable},【搜索框】的name值是:{search_ele_text},'
              f'【搜索框】的坐标是:{search_ele_location},【搜索框】的宽高是:{search_ele_size}')
        if search_ele_enable:
            search_ele.click()
            self.driver.find_element(By.ID,'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            alibaba_ele=self.driver.find_element(By.XPATH,'//*[@text="阿里巴巴"]')
            if alibaba_ele.is_displayed():
                print('搜索成功')
            else:
                print('搜索失败')
        else:
            assert False,'搜索框不可用'

