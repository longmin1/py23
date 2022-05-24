'''常见控件
resource-id
accessbility_id
xpath
classname（不推荐）'''
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestXueqiu():
    def setup(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='7.1.2'
        desired_caps['deviceName']='emulator-5554'
        desired_caps['appPackage']='com.xueqiu.android'
        desired_caps['appActivity']='.main.view.MainActivity'
        # desired_caps['dontStopAppOnReset']='true'
        # desired_caps['skipDeviceInitialization']='true'
        desired_caps['unicodeKeyBoard']='true'
        desired_caps['resetKeyBoard']='true'
        desired_caps['noReset']='true'#不需要清空缓存的时候可以加上这个
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_xueqiu(self):
        '''进入搜索框，输入阿里巴巴，选择阿里巴巴，最后找到阿里巴巴概念的的对应的价格做断言'''
        self.driver.find_element(By.ID,'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(By.ID,'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH,'//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        sleep(3)
        # gupiaojiage = self.driver.find_element(By.XPATH,
        #                                        '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        # print(f'这只股票的价格是:{gupiaojiage}')
        # current_price=self.driver.find_element(By.XPATH,'//*[@text="BK0515"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price" and @index=0]').text
        current_price = self.driver.find_element(By.XPATH,
                                                 '//*[@text="阿里巴巴概念"]/../..//*[@resource-id="com.xueqiu.android:id/current_price" and @index=0]').text
        print(current_price)
        assert float(current_price)==1064.58

