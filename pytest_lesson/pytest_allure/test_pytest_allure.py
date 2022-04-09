'''pytest和allure结合运用'''

import allure
# class TestSarch():
#     @allure.title('搜索词为android')
#     def test_case1(self):
#         print('test_case1')
#
#     @allure.title('搜索词为ios')
#     def test_case2(self):
#         print('test_case2')
@allure.feature('搜索模块')
class TestSarch():
    @allure.story('搜索成功1')
    def test_case1(self):
        print('test_case1')

    @allure.story('搜索失败')
    def test_case2(self):
        print('test_case2')

@allure.feature('登录模块')
class TestLogin():

    @allure.story('登录成功')
    def test_case1(self):
        with allure.step('步骤1:打开应用'):
            print('打开应用的步骤')
        with allure.step('输入密码'):
            print('输入密码成功')
        with allure.step('点击登录'):
            print('登录成功')

