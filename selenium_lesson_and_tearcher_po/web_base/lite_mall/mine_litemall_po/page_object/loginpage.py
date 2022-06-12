'''登录页面
用户登录
return 到首页'''
from selenium.webdriver.common.by import By

from selenium_lesson_and_tearch_po.web_base.lite_mall.mine_litemall_po.page_object.base import Base


class LoginPage(Base):

    base_url = 'http://litemall.hogwarts.ceshiren.com/'
    __INPUT_NAME_ELE=(By.NAME, "username")
    __INPUT_PASSWORD_ELE =(By.NAME, "password")
    __INPUT_NAME_WORDS ="manage"
    __INPUT_PASSWORD_WORDS ="manage123"
    __LOGIN_BUTTLE=(By.CSS_SELECTOR,".el-button--primary")

    def login(self):
        # 登录
        self.driver.get(self.base_url)
        # 问题，输入框内有默认值，此时send——keys不回清空只会追加
        # 解决方案： 在输入信息之前，先对输入框完成清空
        # 输入用户名密码
        self.send_keys(self.__INPUT_NAME_ELE,input_words=self.__INPUT_NAME_WORDS)
        self.send_keys(self.__INPUT_PASSWORD_ELE, input_words=self.__INPUT_PASSWORD_WORDS)

        # 点击登录按钮
        self.find(self.__LOGIN_BUTTLE).click()

        from selenium_lesson_and_tearch_po.web_base.lite_mall.mine_litemall_po.page_object.mainpage import MainPage
        return MainPage(self.driver)