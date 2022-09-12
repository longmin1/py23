'''
接口第一节直播课程
企业微信
自己练习
'''
from jsonpath import jsonpath
import requests

from http_接口.http_接口lesson.log_until import logger


class TestWework():
    url = 'https://qyapi.weixin.qq.com/cgi-bin'

    def setup_class(self):
        '''获取access_token'''
        params = {'corpid': 'ww1bdbd20b9a4f9e88',
                  'corpsecret': 'q-rXIMja_YEuTAOOO4xNwuFPYE26oXPUy5OPkfpnmOw'}
        res = requests.get(url=self.url + '/gettoken', params=params)
        self.access_token = res.json()['access_token']
        logger.debug(f'access_token的值是:{self.access_token}')

    def teardown_class(self):
        '''删除部门'''
        params = {'access_token': self.access_token, 'id': '917'}
        res = requests.get(url=self.url + '/department/delete', params=params)
        # print(res.json())
        logger.debug(f'删除的结果是：{res.json()}')

    def test_create_department(self):
        '''创建部门'''
        params = {'access_token': self.access_token}
        json_data = {
            "name": "0703研发中心917",
            "name_en": "0703RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 917
        }
        res = requests.post(url=self.url + '/department/create', json=json_data, params=params)
        logger.debug(f'新增部门的返回值：{res.json()}')
        print('jsonpath的结果是：' + jsonpath(res.json(), '$.errmsg')[0])
        assert res.json()['errmsg'] == 'created'
        assert jsonpath(res.json(), '$.errmsg') == ['created']

    def test_update_department(self):
        '''根据id更新部门名称'''
        params = {'access_token': self.access_token}
        json_data = {
            "id": 917,
            "name": "yangbing研发中心",
            "name_en": "yangbingRDGZ",
            "parentid": 1,
            "order": 1
        }

        res = requests.post(self.url + '/department/update', params=params, json=json_data)
        logger.debug(f'更新部门的返回值：{res.json()}')
        assert res.json()['errmsg'] == "updated"
