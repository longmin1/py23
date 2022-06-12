# coding=utf-8
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
'''讲述selenium的三种的等待方式（强制等待，隐式等待，显式等待）'''

class TestBaiduWait():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def test_wait(self):
        self.driver.find_element(By.LINK_TEXT,'贴吧').click()
        sleep(5)
        title=self.driver.title
        print(title)#百度一下，你就知道
        handle = self.driver.current_window_handle  # 获取当前窗口句柄
        print(handle)
        num = self.driver.window_handles  # 获取当前页的所有句柄
        print(num)
        self.driver.switch_to.window(num[1])  # 跳到新的标签页；因为当前只有一个主页面和新的标签页，所以num[1]表示新标签页，num[0]表示主页面
        # self.driver.switch_to_window(num[0])  # 回到主页面的句柄
        def title(x):#这个方法一定要传一个参数，这里x一定要传，虽然不用，但要穿，相当于给了self.driver用
            return self.driver.title=='百度贴吧——全球领先的中文社区'
        # print(self.driver.title)#百度贴吧——全球领先的中文社区

        WebDriverWait(self.driver,10).until(title)#显式等待，unitl要传一个方法
        sleep(2)
        a=expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, ".rcmd_forum_list:nth-child(2) .rcmd_forum_desc a"))
        #python自带的一个方法，判断元素可以点击，可以结合显式等待一起用
        WebDriverWait(self.driver, 10).until(a)#如果a是true,上个元素是可以点击的就进行走下一步操作，不能点击就报异常。
        self.driver.find_element_by_css_selector('.rcmd_forum_list:nth-child(2) .rcmd_forum_desc a').click()
        print('hello')
        #显示等待结合lambda表达式
        WebDriverWait(self.driver, 10).until(lambda x:x.find_element(By.LINK_TEXT,'贴吧'))
        #去判断这个元素是否存在，存在就继续下一步
        a=WebDriverWait(self.driver, 10).until(lambda x:x.find_element(By.LINK_TEXT,'贴吧'))
        #如果像这样前面有变量接收，就可以进行接收这个元素，a.text--》就可以这样打印出文本值，