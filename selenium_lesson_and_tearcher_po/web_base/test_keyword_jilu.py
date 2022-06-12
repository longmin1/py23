'''自动化关键字记录
日志，截图，page_source'''

import logging
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_logger():
    # create logger
    logger = logging.getLogger(os.path.basename(__file__))
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.FileHandler(filename='mylog.log', encoding="utf-8")
    ch.setLevel(logging.DEBUG)
    streamHandler = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    streamHandler.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(streamHandler)
    return  logger

class TestKeyword():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.logger=get_logger()

    def teardown(self):
        self.driver.quit()

    def test_keyword_log(self):
        self.driver.get('https://www.sogou.com/')
        search_word='霍格沃兹开发'
        self.driver.find_element(By.ID,'query').send_keys(search_word)
        self.logger.info(f'搜索词是{search_word}')
        self.driver.find_element(By.ID,'stb').click()
        self.logger.debug('点击搜索一下')

    def test_keyword_screen_shot(self):
        self.driver.get('https://www.sogou.com/')
        search_word = '霍格沃兹开发'
        self.driver.find_element(By.ID, 'query').send_keys(search_word)
        self.driver.find_element(By.ID, 'stb').click()
        sleep(1)
        self.driver.save_screenshot('respon.png')

    def test_keyword_pagesource(self):
        self.driver.get('https://www.sogou.com/')
        search_word = '霍格沃兹开发'
        self.driver.find_element(By.ID, 'query').send_keys(search_word)
        self.driver.find_element(By.ID, 'stb').click()
        self.logger.debug(self.driver.page_source)
        with open('page_souce.html','w',encoding='utf-8') as f:
            f.write(self.driver.page_source)
