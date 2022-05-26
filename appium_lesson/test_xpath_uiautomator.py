'''
xpath
uiautomator定位
'''
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestXueqiu():
    def setup_class(self):
        desired_caps={}
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

    def teardown_class(self):
        self.driver.quit()
    def test_xueqiu_price(self):
        '''xpath进行价格断言'''
        '''进入搜索框，输入阿里巴巴，选择阿里巴巴，最后找到阿里巴巴-SW的的对应的价格做断言'''
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/home_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/name" and @text="阿里巴巴"]').click()
        sleep(3)
        current_price = self.driver.find_element(By.XPATH,
                                                 '//*[@text="阿里巴巴-SW"]/../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        print(current_price)
        assert float(current_price) <100
    def test_xueqiu_login(self):
        '''uiautomator进行定位登录'''
        name_text='text("我的")'
        self.driver.find_element_by_android_uiautomator(name_text).click()
        account_login_text='textContains("帐号密码登录")'
        self.driver.find_element_by_android_uiautomator(account_login_text).click()
        account_id='resourceId("com.xueqiu.android:id/login_account")'
        self.driver.find_element_by_android_uiautomator(account_id).send_keys('173')
        password_id='resourceId("com.xueqiu.android:id/login_password")'
        self.driver.find_element_by_android_uiautomator(password_id).send_keys('123sss')
        login_text='text("登录")'
        self.driver.find_element_by_android_uiautomator(login_text).click()
        toast_text_id='resourceId("com.xueqiu.android:id/md_content")'
        text=self.driver.find_element_by_android_uiautomator(toast_text_id).text
        print(text)
        assert text=='手机号码填写错误'



    def test_xueqiu_scroll(self):
        '''滚动查找某元素--满仓日记  并点击进入其主页'''
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()'
                                                        '.scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("满仓日记").instance(0));').click()