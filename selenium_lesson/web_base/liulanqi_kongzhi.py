# import time
#
from selenium import webdriver
from selenium.webdriver.common.by import By
#
driver=webdriver.Chrome()
driver.get('https://www.testing-studio.com/')
driver.maximize_window()
driver.minimize_window()#最小化
# driver.find_element(By.XPATH,'//*[@id="menu-item-927"]/a').click()
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,"关于我们").click()
# driver.refresh()#刷新
# driver.back()#后退
# driver.find_element(By.ID,"su").click()
# time.sleep(2)
# # driver.close()
# driver1=webdriver.Firefox()
# driver1.get('https://www.baidu.com/')
# driver.maximize_window()
# time.sleep(2)
# driver1.close()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 显式等待

# driver = webdriver.Chrome()
# driver.get("https://vip.ceshiren.com/#/ui_study/")
# driver.maximize_window()
# WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "success_btn")))
# driver.find_element(By.ID, "success_btn").click()
# driver.get('https://www.testing-studio.com/')
# driver.find_element(By.XPATH,'//*[@id="menu-item-927"]/a').click()
# time.sleep(5)
# js='window.open("https://www.baidu.com")'#用js脚本打开一个新的标签页并进入到百度页面
# driver.execute_script(js)
# driver.execute_script("window.open('','_blank');")
# time.sleep(5)
# print(driver.window_handles)#获取浏览器的所有句柄
# print(driver.current_window_handle)#获取当前句柄
# print(driver.title)#打印标题
# driver.switch_to.window(driver.window_handles[-1])#切换到最新的句柄
# print(driver.title)
# # driver.close()#close()是关闭当前所在的这个标签页
# driver.quit()#quit()是关闭当前这个浏览器



