'''
点击添加类目 return 到创建类列表页面
获取类目创建结果
'''
from selenium.webdriver.common.by import By

from selenium_lesson.web_base.lite_mall.mine_litemall_po.page_object.base import Base
from selenium_lesson.web_base.lite_mall.mine_litemall_po.utils.log_utils import logger



class CategoryPage(Base):
    __ADDELE=(By.XPATH, "//*[text()='添加']")

    def add_category(self):
        '''添加商品类目'''
        # 添加商品类目操作
        self.find(self.__ADDELE).click()

        from selenium_lesson.web_base.lite_mall.mine_litemall_po.page_object.create_categorypage import \
            CreateCategoryPage
        return CreateCategoryPage(self.driver)

    def get_category_result(self,category_name,path):

        res = self.finds(By.XPATH,f"//*[text()='{category_name}']")
        self.get_screen(path)
        # 数据的清理一定到放在断言操作之后完成，要不然可能会影响断言结果
        self.find(By.XPATH,f"//*[text()='{category_name}']/../..//*[text()='删除']").click()
        logger.info(f"断言获取到的实际结果为{res}")
        return res