'''雪球 webview
'''
from appium import webdriver
from selenium.webdriver.common.by import By


class TestXueQiu():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.common.MainActivity'
        # desired_caps['dontStopAppOnReset']='true'
        # desired_caps['skipDeviceInitialization']='true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'  # 不需要清空缓存的时候可以加上这个
        desired_caps['chromedriverExecutableDir']='D:\chromedriver_win32_app_webview\chromedriver.exe'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    def teardown(self):
        self.driver.quit()

    def test_webview_xueqiu(self):
        '''先试试我的雪球能不能找到webview，很多需要开发打开开关'''
        self.driver.find_element(By.XPATH,'//*[@text="交易"]').click()
        contexts=self.driver.contexts
        print(contexts)#['NATIVE_APP']  只能获取到一个原生native

    def test_liulanqi(self):
        '''由于雪球应用我看不到webview，
#     因此我用mumu的浏览器apk来试试，查看webview'''
        desired_caps = {
                'platformName': 'Android',
                'deviceName': '127.0.0.1:7555',
                'platformVersion': '6.0.1',
                "appPackage": "com.android.browser",
                "appActivity": ".BrowserActivity",
                'noReset': True,
                'chromedriverExecutable': 'D:\chromedriver_win32_app_webview/chromedriver.exe'
            }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        contexts = self.driver.contexts
        print(contexts)#['NATIVE_APP', 'WEBVIEW_com.android.browser']
        '''切换到webview'''
        self.driver.switch_to.context(contexts[-1])
        '''获取当前的url'''
        print(self.driver.execute_script(
            'return window.location.href'))  # http://yixiu.game.163.com/0D5CF4EB90C95F93/index.html
            #这里浏览器还是放的链接，好多app是放在手机里了像上面的雪球app那样
        '''利用js更新现有窗口，让浏览器跳转到百度网页'''
        self.driver.execute_script("window.location.href='https://www.baidu.com'")#window.location - 更新当前窗口

        window_handles=self.driver.window_handles
        print(window_handles)#['CDwindow-DC37A23BCAB38CDB2DC3AA0663661709']
        # self.driver.switch_to.window(window_handles[0])
        '''输入关键字，搜索'''
        # self.driver.find_element(By.ID,'index-kw').click()
        self.driver.find_element(By.ID,'index-kw').send_keys('huogeworts')
        self.driver.find_element(By.ID,'index-bn').click()
        print(self.driver.window_handles)
        '''利用js载入新窗口'''
        self.driver.execute_script("window.open('https://blog.csdn.net/benxiaohai888/article/details/78235017')")#js新窗口
        #不过新开窗口这一句我失败了 我没有新开窗口，也没报错
        print('添加新窗口后的句柄',self.driver.window_handles)









