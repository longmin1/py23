"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
from prac_po1.base.app import App
from prac_po1.utils.contact_info import ContactInfo


class TestContact:
    def setup_class(self):
        # 第一次初始化App() 实例的时候， 就需要传递一个driver =None
        self.app = App()

    def setup(self):
        # 执行第二条用例的时候，  会复用driver
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.back()

    def teardown_class(self):
        self.app.quit()

    def test_addcontact(self):
        """
        添加联系人
        :return:
        """
        # mock 联系人姓名和电话号码
        name = ContactInfo.get_name()
        phonenum = ContactInfo.get_phonenum()

        result = self.main.goto_addresslist(). \
            goto_addmember_page().click_addmember_menual(). \
            edit_member(name, phonenum).get_text()
        assert "添加成功" == result

    def test_addcontact1(self):
        """
        添加联系人
        :return:
        """
        # mock 联系人姓名和电话号码
        name = ContactInfo.get_name()
        phonenum = ContactInfo.get_phonenum()

        result = self.main.goto_addresslist(). \
            goto_addmember_page().click_addmember_menual(). \
            edit_member(name, phonenum).get_text()
        assert "添加成功" == result
