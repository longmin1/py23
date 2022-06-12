from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://ceshiren.com/')
driver.implicitly_wait(10)
#这里都取社区的上头的帽子的元素，写CSS定位的几种方式【标签，id，class，属性】
ele1=driver.find_element(By.CSS_SELECTOR, '#site-logo')
ele2=driver.find_element(By.CSS_SELECTOR, '.logo-big')
ele3=driver.find_element(By.CSS_SELECTOR, '[alt="测试人社区"]')
ele4=driver.find_element(By.CSS_SELECTOR, '.title [alt="测试人社区"]')
ele5=driver.find_element(By.CSS_SELECTOR, 'a #site-logo')#a标签下的子子孙孙id属性为site-logo的元素
#获取所有定位元素的src属性值，来判断是不是都定位的同一元素
print(ele1.get_attribute('src'))
print(ele2.get_attribute('src'))
print(ele3.get_attribute('src'))
print(ele4.get_attribute('src'))
print(ele5.get_attribute('src'))