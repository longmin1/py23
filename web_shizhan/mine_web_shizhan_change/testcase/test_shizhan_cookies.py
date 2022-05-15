

from selenium.webdriver.common.by import By

from mine_web_shizhan_change.page.mainpage import MainPage
'''只改造了添加成员,添加部门简单的po设计模式'''

class TestCookies():
    def setup(self):
        self.main=MainPage()

    def teardown(self):
        self.main.quit()

    def test_add_member(self):
        ac_result=MainPage().click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]')).get_member()
        assert ac_result

    def test_add_department(self):
        text=self.main.click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]'))\
            .add_department().create_departemnt_name().get_department_result()
        # print(text)
        assert text=='新建部门成功'



# if __name__ == '__main__':
#     TestCookies().test_add_member()



