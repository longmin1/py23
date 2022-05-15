'''
创建类目
return 类目列表页面
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium_lesson.web_base.lite_mall.mine_litemall_po.page_object.base import Base
from selenium_lesson.web_base.lite_mall.mine_litemall_po.utils.web_utils import click_exception


class CreateCategoryPage(Base):
    __category_input_ele=(By.CSS_SELECTOR,".el-input__inner")
    __primary_button=(By.CSS_SELECTOR,".dialog-footer .el-button--primary")

    def create_category(self,category_name):
        '''创建类目'''
        self.send_keys(self.__category_input_ele,input_words=category_name)

        # self.driver.find_element(By.CSS_SELECTOR,
        #                          ".el-input__inner").send_keys("新增商品测试")


        WebDriverWait(self.driver, 10).until(click_exception(*self.__primary_button))
        from selenium_lesson.web_base.lite_mall.mine_litemall_po.page_object.categorypage import CategoryPage
        return CategoryPage(self.driver)