from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def web_locate():
    driver=webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study/')
    driver.maximize_window()
    sleep(2)
    driver.switch_to.frame(0)#元素在frame框中就要先切换到frame框里
    sleep(2)
    #id定位
    # driver.find_element(By.ID,'frame_btn').click()
    #css定位
    driver.find_element(By.CSS_SELECTOR,'#frame_btn>span').click()
    #xpath定位
    # driver.find_element(By.XPATH,'//*[@id="frame_btn"]').click()
    print(driver.switch_to.alert.text)
    sleep(2)
    driver.switch_to.alert.accept()
    driver.quit()

web_locate()