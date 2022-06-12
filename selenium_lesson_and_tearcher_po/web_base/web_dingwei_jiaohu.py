from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_web_selenium_jiaohu():
    driver=webdriver.Chrome()
    driver.get('https://www.sogou.com/')
    driver.find_element(By.ID,'query').send_keys('霍格沃兹开发')
    sleep(2)
    driver.find_element(By.NAME,'query').clear()
    sleep(2)
    driver.find_element(By.ID, 'query').send_keys('五一出游方案')
    sleep(2)
    driver.find_element(By.NAME, 'query').clear()
    driver.find_element(By.ID, 'query').send_keys('1111111111111')
    driver.find_element(By.XPATH,'//input[@id="stb"]').click()
    sleep(2)
    print(driver.find_element(By.ID, "upquery").get_attribute('value'))
    sleep(2)
    driver.find_element(By.ID, 'upquery').click()
    sleep(2)
    # driver.find_element(By.ID, 'upquery').send_keys('python')
    sleep(2)
    driver.find_element(By.XPATH,'//input[@id="upquery"]').clear()
    sleep(2)
    driver.quit()
# test_web_selenium_jiaohu()
def test_yuansu_text():
    driver = webdriver.Chrome()
    driver.get('https://vip.ceshiren.com/#/ui_study/')
    driver.maximize_window()
    sleep(2)
    driver.switch_to.frame(0)
    sleep(2)
    #自己写的xpath定位
    # print(driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').text)
    # print(
    #     driver.find_element(By.XPATH, '//table[@class="el-table__body"]/tbody/tr[1]/td[2]/div').get_attribute('class'))
    #css定位1
    # print(driver.find_element(By.CSS_SELECTOR, '.el-table__row>td:nth-child(2)>div:nth-child(1)').text)
    #css定位2
    print(driver.find_element(By.CSS_SELECTOR, '.el-table__row .cell').text)
    #浏览器复制的XPATH定位
    # print(driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[3]/table/tbody/tr[1]/td[2]/div').text)
    sleep(2)

test_yuansu_text()