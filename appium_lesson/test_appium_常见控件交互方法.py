'''常见控件交互方法
'''
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestAppdemo():
    def setup(self):
        desired_caps={'platformName':'Android','platformVersion':'7.1.2','deviceName':'emulator-5554',
                      'appPackage':'com.touchboarder.android.api.demos','appActivity':'com.example.android.apis.ApiDemos'
                      }
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_appdemo(self):
        '''打开api.demo
        点击Animation 进入下一个页面
        点击Seeking进入下一个页面
        查看【run】按钮是否显示/是否可点击
        查看【滑动条】是否显示/是否可用/是否可点击
        获取【滑动条】长度
        点击【滑动条】中心位置'''
        self.driver.find_element(By.XPATH,'//*[@text="Animation"]').click()
        self.driver.find_element(By.XPATH,'//*[@text="Seeking"]').click()
        # 1,查看【run】按钮是否显示 / 是否可点击
        run_element=self.driver.find_element(By.XPATH,'//*[@text="RUN"]')
        run_element_display=run_element.is_displayed()
        run_element_clickable=run_element.get_attribute('clickable')
        print(f'[run]元素是否可以显示:{run_element_display},是否可点击:{run_element_clickable}')
        # 2,查看【滑动条】是否显示/是否可用/是否可点击
        seekBar_element=self.driver.find_element(By.ID,'com.touchboarder.android.api.demos:id/seekBar')
        seekBar_element_display=seekBar_element.is_displayed()
        seekBar_element_enable=seekBar_element.is_enabled()
        seekBar_element_clickable=seekBar_element.get_attribute('clickable')
        print(f'[run]元素是否可以显示:{seekBar_element_display},是否可用:{seekBar_element_enable}'
              f',是否可点击:{seekBar_element_clickable}')
        # 3,获取【滑动条】长度
        seekbar_size=seekBar_element.size
        seekbar_size_height=seekbar_size['height']
        seekbar_size_width=seekbar_size['width']
        print(f'【滑动条】的高度是:{seekbar_size_height},宽度是:{seekbar_size_width}')
        # 4,点击【滑动条】中心位置
        seekbar_location=seekBar_element.location
        seekbar_location_x=seekbar_location['x']
        seekbar_location_y=seekbar_location['y']
        print(f'【滑动条】的左上角起始坐标是:{seekbar_location}')
        seekbar_centor_location=(seekbar_location_x+seekbar_size_width/2,seekbar_location_y+seekbar_size_height/2)
        #老师练习用的方法：
        self.driver.tap([seekbar_centor_location])
        # self.driver.flick(seekbar_location_x,seekbar_location_y,*seekbar_centor_location)
        # 自己找的一个方法（传入起始坐标和终点坐标）也可达到效果
        sleep(5)

