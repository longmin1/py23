from faker import Faker
from selenium.webdriver.common.by import By
from time import sleep
from mine_web_shizhan_change.page.base import Base


class AddressPage(Base):

    __ELE_ADD_MEMBER=(By.CSS_SELECTOR,'.js_has_member .js_add_member')
    __NAME_INPUT_ELE=(By.CSS_SELECTOR, '#username')
    __ACCID_INPUT_ELE=(By.CSS_SELECTOR, '#memberAdd_acctid')
    __PHONE_INPUT_ELE=(By.CSS_SELECTOR, '#memberAdd_phone')
    __BUTTON_ELE=(By.CSS_SELECTOR, '.js_btn_save')
    __CLICK_PLUS_SIGN=(By.CSS_SELECTOR,'.member_colLeft_top_addBtnWrap.js_create_dropdown')
    __ADD_DEPARTMENT=(By.CSS_SELECTOR, '.js_create_party')
    __TOAST_ELE=(By.CSS_SELECTOR,'#js_tips')
    __NAME_LIST=(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
    __NEXT_PAGE=(By.CSS_SELECTOR,'.ww_pageNav_info .js_next_page')

    def random_data(self):
        fake=Faker(locale="zh_CN")
        self.name=fake.name()
        self.accid=fake.ssn()
        self.mobile=fake.phone_number()


    def add_member(self):
        '''添加成员'''
        self.random_data()
        self.wait_by_excepted_ele(self.__ELE_ADD_MEMBER)
        self.find(self.__ELE_ADD_MEMBER).click()
        self.find(self.__NAME_INPUT_ELE).send_keys(self.name)
        ele = self.find(self.__ACCID_INPUT_ELE)
        ele.send_keys(self.accid)
        self.find(self.__PHONE_INPUT_ELE).send_keys(self.mobile)
        self.action.scroll_from_element(ele, 0, 500).perform()
        self.find(self.__BUTTON_ELE).click()
        return self.name



    def get_member(self):
        '''获取成员列表中是否有刚刚所添加的成员的名字信息'''
        a=self.add_member()
        print(a)
        def func(x):
            eles=self.finds(self.__NAME_LIST)#两种方式一样的  都是获取名字的列表所有值
            for ele in eles:
                if ele.get_attribute('title')==a:
                    return ele.get_attribute('title')
            sleep(2)
            if self.finds(self.__NEXT_PAGE)!=[]:
                self.finds(self.__NEXT_PAGE)[0].click()
        result=self.wait_by_fun(func)
        print(result)
        return result

    def add_department(self):
        '''添加部门
        return 到新建部门页面'''
        self.find(self.__CLICK_PLUS_SIGN).click()
        self.find(self.__ADD_DEPARTMENT).click()
        from mine_web_shizhan_change.page.createdepartmentpage import CreateDepartmentPage
        return CreateDepartmentPage(self.driver)

    def get_department_result(self):
        self.wait_ele_visibilit(self.__TOAST_ELE)
        return self.find(self.__TOAST_ELE).text








# AddressPage().add_member()