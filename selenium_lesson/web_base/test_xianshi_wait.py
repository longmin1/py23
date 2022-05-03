from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def xianshiwait():
    driver = webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study/')
    driver.maximize_window()
    # driver.find_element(By.XPATH,'//*[text()="点击两次响应"]').click()
    WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@id="success_btn"]')))
    driver.find_element(By.XPATH,'//*[text()="消息提示"]').click()
    time.sleep(2)
    #写死元素定位的一种
    # def func(x):
    #     driver.find_element(By.CSS_SELECTOR,'#primary_btn').click()
    #     return driver.find_element(By.CSS_SELECTOR,'.el-message-box__title')
    # WebDriverWait(driver,10).until(func)

    #不写死元素的一种
    def func(old_ele,except_ele):
        def inner(x):
            driver.find_element(*old_ele).click()
            return driver.find_element(*except_ele)
        return inner

    WebDriverWait(driver, 10).until(func((By.CSS_SELECTOR,'#primary_btn'),(By.CSS_SELECTOR,'.el-message-box__title')))
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,'#primary_btn').click()

    driver.quit()

if __name__ == '__main__':
    xianshiwait()