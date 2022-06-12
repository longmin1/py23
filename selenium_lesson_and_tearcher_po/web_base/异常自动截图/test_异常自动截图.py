'''用装饰器的思想达到用例运行异常 自动截图保存，添加日志，以及保存page_souce'''
import datetime
import logging
import os

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

def get_logger():
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
    log_path=f'log/{time_now}.log'
    ch = logging.FileHandler(filename=log_path, encoding="utf-8")
    ch.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    streamHandler.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(streamHandler)
    return  logger


'''定义一个装饰器'''
def ui_exception_chuli(func):
    def inner(*args,**kwargs):
        self=args[0]
        try:
            return func(*args,**kwargs)
        except Exception as e:
            get_logger().info('用例发生异常了')
            time_now = datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')
            pic_path=f'./pic/{time_now}.PNG'
            page_souce_path=f'./page_souce/{time_now}.html'
            self.driver.save_screenshot(pic_path)
            with open(page_souce_path,'w',encoding='utf-8')as f:
                f.write(self.driver.page_source)
            allure.attach.file(pic_path,name='报错截图',attachment_type=allure.attachment_type.PNG)
            allure.attach.file(page_souce_path,name='报错的页面的page_spuce源码',attachment_type=allure.attachment_type.TEXT)
            raise e
    return inner






class TestBaidu():
    def setup_class(self):
        self.driver=webdriver.Chrome()

    def teardown_class(self):
        self.driver.quit()
    @ui_exception_chuli
    def find_click(self):
        return self.driver.find_element(By.ID,'su1')

    def test_case(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.find_click().click()




