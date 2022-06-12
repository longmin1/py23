'''首页点击商品类目
return 到类目列表页面'''
from selenium.webdriver.common.by import By

from selenium_lesson_and_tearch_po.web_base.lite_mall.mine_litemall_po.page_object.base import Base


class MainPage(Base):
    __management=(By.XPATH, "//*[text()='商场管理']")
    __category=(By.XPATH, "//*[text()='商品类目']")


    def click_category(self):
        '''点击商品类目菜单'''

        # 点击商场管理/商品类目，进入商品类目页面
        # 进入商品类目页面
        self.find(self.__management).click()
        self.find(self.__category).click()

        from selenium_lesson_and_tearch_po.web_base.lite_mall.mine_litemall_po.page_object.categorypage import CategoryPage
        return CategoryPage(self.driver)