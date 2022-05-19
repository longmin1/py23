'''第一次连接设备测试'''
from appium import webdriver

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0.1'
desired_caps['deviceName']='127.0.0.1:7555'
desired_caps['appPackage']='com.xueqiu.android'
desired_caps['appActivity']='.common.MainActivity'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print('启动【雪球】应用')
driver.quit()