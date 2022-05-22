'''
连接雷电模拟器
打开API DEMO应用
点击OS,进入到下一个界面
点击[Morse Code]
输入内容[ceshiren.com]
返回上一个页面
返回上一个页面
关闭应用
'''
import time
from appium import webdriver
from selenium.webdriver.common.by import By


class TestApidemo():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.2'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.touchboarder.android.api.demos'
        desired_caps['appActivity'] = 'com.example.android.apis.ApiDemos'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print('启动【APIdemo】应用')

    def teardown(self):
        self.driver.quit()

    def test_apidemo(self):
        self.driver.find_element(By.XPATH,"//*[@text='OS']").click()
        self.driver.find_element(By.XPATH, "//*[@text='Morse Code']").click()
        self.driver.find_element(By.XPATH,'//*[@resource-id="com.touchboarder.android.api.demos:id/text"]').send_keys('这是一个测试')
        self.driver.save_screenshot('./pic.PNG')
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)



