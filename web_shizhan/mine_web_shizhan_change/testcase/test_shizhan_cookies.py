

from selenium.webdriver.common.by import By

from mine_web_shizhan_change.page.mainpage import MainPage
'''只改造了一点点的添加成员'''

class TestCookies():
    def setup(self):
        pass

    def teardown(self):
        pass
        # self.driver.quit()

    def test_add_member(self):
        res_name=MainPage().click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]')).add_member()
        ac_result=MainPage().click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]')).get_member()
        assert ac_result==res_name

    def test_add_department(self):
        text=MainPage().click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]')).add_department()
        print(text)
        assert text=='新建部门成功'



if __name__ == '__main__':
    TestCookies().test_add_member()



