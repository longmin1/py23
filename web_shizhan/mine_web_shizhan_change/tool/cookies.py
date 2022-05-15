from time import sleep
import shelve

import yaml

from mine_web_shizhan_change.page.base import Base


class DisposeCookies(Base):

    def save_cookies(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(20)
        cookies = self.driver.get_cookies()
        with open('cookies.yml','w')as f:
            yaml.safe_dump(cookies,f)
        sleep(5)



    def add_cookies(self,path):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        with open(path,'r')as f:
            cookies=yaml.safe_load(f)
            # print(cookies)
        for cookie in cookies:
            # print(cookie)
            self.driver.add_cookie(cookie)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        # return MainPage(self.driver)


# if __name__ == '__main__':
#     DisposeCookies().save_cookies()
    # DisposeCookies().add_cookies('cookies.yml')