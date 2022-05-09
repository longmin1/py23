

from selenium.webdriver.common.by import By

from mine_web_shizhan_change.page.mainpage import MainPage


class TestCookies():
    def setup(self):
        pass

    def teardown(self):
        pass
        # self.driver.quit()

    def test_add_member(self):
        MainPage().click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]')).get_member()

    def test_add_department(self):
        text=MainPage().click_address(path='../tool/cookies.yml', tip=(By.XPATH, '//*[text()="通讯录"]')).add_department()
        print(text)
        assert text=='新建部门成功'



if __name__ == '__main__':
    TestCookies().test_add_member()



