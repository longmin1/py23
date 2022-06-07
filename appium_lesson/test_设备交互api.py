'''
模拟来电
来短信
切换网络
截图
录屏
'''
from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions
from time import sleep

def test_testcase():
    '''我用真机报错 我没有运行成功'''

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '10'
    desired_caps['deviceName'] = '77fc05f5'
    # desired_caps['udid']='77fc05f5'


    desired_caps['appPackage'] = 'com.youdao.dict'
    desired_caps['appActivity'] = '.activity.account.LoginActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    '''录屏'''
    # driver.start_recording_screen()
    # '''模拟来电'''
    # driver.make_gsm_call('5551234567',GsmCallActions.CALL)
    # '''模拟来短信'''
    # driver.send_sms('15602462915','我爱你，宝宝')
    # '''截图切换网络'''
    # driver.save_screenshot('.devices_pic/pic.png')
    # driver.set_network_connection(4)#数据模式
    # sleep(3)
    # driver.set_network_connection(2)#wifi模式
    # driver.save_screenshot('.devices_pic/pic1.png')
    # sleep(3)
    # driver.stop_recording_screen()

    driver.quit()