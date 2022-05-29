from app_appium_shizhan_of_mine.pageobject.mainpage import MainPage
from app_appium_shizhan_of_mine.until.log_until import logger


class TestWework():
    def setup(self):
        self.main=MainPage()
    def teardown(self):
        self.main.quit()
    def test_addmember(self):
        toast=self.main.click_addresslist().click_add_member().click_add().input_member().get_toast()
        logger.info(f'获取到的toast信息为:{toast}')
        assert toast=='添加成功'
    def test_clock(self):
        '''测试外出打卡'''
        result=self.main.click_workbench().click_clock().click_Punch_out()
        logger.info(f'打卡的结果是:{result}')
        assert result=='外出打卡成功'