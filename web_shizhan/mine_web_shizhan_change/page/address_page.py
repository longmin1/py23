from faker import Faker
from selenium.webdriver.common.by import By
from time import sleep
from mine_web_shizhan_change.page.base import Base


class AddressPage(Base):

    __ELE_ADD_MEMBER=(By.XPATH,'//a[text()="添加成员"]')
    __NAME_INPUT_ELE=(By.CSS_SELECTOR, '#username')
    __ACCID_INPUT_ELE=(By.CSS_SELECTOR, '#memberAdd_acctid')
    __PHONE_INPUT_ELE=(By.CSS_SELECTOR, '#memberAdd_phone')
    __BUTTON_ELE=(By.CSS_SELECTOR, '.js_btn_save')
    def random_data(self):
        fake=Faker(locale="zh_CN")
        self.name=fake.name()
        self.accid=fake.ssn()
        self.mobile=fake.phone_number()

    def add_member(self):
        self.random_data()
        self.wait_ele_visibilit(self.__ELE_ADD_MEMBER)
        self.finds(self.__ELE_ADD_MEMBER)[1].click()
        self.find(self.__NAME_INPUT_ELE).send_keys(self.name)
        ele = self.find(self.__ACCID_INPUT_ELE)
        ele.send_keys(self.accid)
        self.find(self.__PHONE_INPUT_ELE).send_keys(self.mobile)
        self.action.scroll_from_element(ele, 0, 500).perform()
        self.find(self.__BUTTON_ELE).click()
        return self.name

    def get_member(self):
        a=self.add_member()
        def func(x):
            eles=self.finds((By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)'))#两种方式一样的  都是获取名字的列表所有值
            for ele in eles:
                if ele.get_attribute('title')==a:
                    return ele.get_attribute('title')
            sleep(2)
            self.finds((By.CSS_SELECTOR,'.ww_pageNav_info .js_next_page'))[0].click()

        res_result=self.wait_by_fun(func)
        return res_result

    def add_department(self):
        '''添加部门'''
        self.find((By.CSS_SELECTOR,'.member_colLeft_top_addBtnWrap.js_create_dropdown')).click()
        self.find((By.CSS_SELECTOR, '.js_create_party')).click()
        self.find((By.CSS_SELECTOR, '.inputDlg_item > input')).send_keys('搬砖部门')
        self.find((By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list')).click()
        self.finds((By.CSS_SELECTOR, '.jstree-anchor'))[1].click()
        self.find((By.XPATH,'//a[@d_ck ="submit"]')).click()
        self.wait_ele_visibilit((By.CSS_SELECTOR,'#js_tips'))
        return self.find((By.CSS_SELECTOR,'#js_tips')).text








# AddressPage().add_member()