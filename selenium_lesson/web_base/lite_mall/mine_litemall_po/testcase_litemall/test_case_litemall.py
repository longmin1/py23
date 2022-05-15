import pytest

from selenium_lesson.web_base.lite_mall.mine_litemall_po.page_object.loginpage import LoginPage


class TestCaseLiteMall():

    def setup_class(self):
        pass

    def teardown_class(self):
        pass
    @pytest.mark.parametrize('category_name',('a','b','c','lily','mary','bobo'),
                             ids=['test_001','test_002','test_003','test_004','test_005','test_006']
                             )
    def test_add_category(self,category_name):
        res=LoginPage().login().click_category().add_category().create_category(category_name).get_category_result(
            category_name,path='../images')
        print(res)
        assert res !=[]