'''
企业微信
产品独有的特性
如获取token
'''
import requests

from http_接口.http_直播实战.http_实战_直播_第二节_mine.apis.base_api import BaseApi


class Wework(BaseApi):

    # def __init__(self):
    #     super().__init__()
    #     self.access_token=self.get_token()




    '''url写死的所以要提取出去，getenv,yaml'''
    # BASE_URL = 'https://qyapi.weixin.qq.com/cgi-bin'


    def __int__(self):
        self.xxl=''
        self.access_token = ''


    def get_token(self,corpid,corpsecret):
        '''获取access_token'''
        url = '/gettoken'
        # params = {'corpid': 'ww1bdbd20b9a4f9e88',
        # 'corpsecret': 'q-rXIMja_YEuTAOOO4xNwuFPYE26oXPUy5OPkfpnmOw'}
        params = {'corpid': corpid,
                  'corpsecret': corpsecret}
        request_info = {'method': 'GET', 'url': url, 'params': params}
        r = self.send_api(request_info)
        '''给access_token赋值'''
        # return r.json()['access_token']

        self.access_token = r.json()['access_token']


