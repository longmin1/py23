'''新建部门页面
填写部门名称
选择部门
return 到通讯录页面'''
from selenium.webdriver.common.by import By

from mine_web_shizhan_change.page.base import Base

class CreateDepartmentPage(Base):
    __DEPARTMENT_NAME=(By.CSS_SELECTOR, '.inputDlg_item > input')
    __CLICK_DEPARTMENT=(By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list')
    __SELECT_DEPARTMENT=(By.CSS_SELECTOR, '.jstree-anchor')
    __SUMIT_BUTTON=(By.XPATH, '//a[@d_ck ="submit"]')

    def create_departemnt_name(self):
        '''添加部门
        选择未知名部门分类
        确认后 return 通讯录页面'''
        self.find(self.__DEPARTMENT_NAME).send_keys('搬砖部门')
        self.find(self.__CLICK_DEPARTMENT).click()
        self.finds(self.__SELECT_DEPARTMENT)[1].click()
        self.find(self.__SUMIT_BUTTON).click()
        from mine_web_shizhan_change.page.address_page import AddressPage
        return AddressPage(self.driver)