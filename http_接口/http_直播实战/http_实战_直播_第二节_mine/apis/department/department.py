'''
只实现业务流程，不进行实例化
'''
import os

import requests

from http_接口.http_直播实战.http_实战_直播_第二节_mine.apis.wework import Wework
from http_接口.http_直播实战.http_实战_直播_第二节_mine.untils.utils import Utils


class Department(Wework):





    def __init__(self):
        # super().__init__()

        file_path = os.sep.join([Utils.get_frame_root_path(), "config/secrets.yaml"])
        yaml_datas=Utils.get_yaml_data(file_path)
        corpid=yaml_datas.get('corpid')
        corpsecret=yaml_datas.get('corpsecret')
        _env = os.getenv("test_env",default='prod')
        print(_env,'xxxx')
        self.BASE_URL=yaml_datas.get(_env).get('BASE_URL')
        # self.access_token=self.get_token(corpid,corpsecret)
        self.get_token(corpid,corpsecret)#这里要先运行这个函数，才回去走到底层去赋值access_token,
        # 不然会报错的

    def create_department(self,create_json_data):
        '''创建部门'''
        print(self.access_token,'xxxxx')
        create_url='/department/create'
        params = {'access_token': self.access_token}
        request_info={'method':'POST','url':create_url,'params':params,'json':create_json_data}
        return self.send_api(request_info)

    def update_department(self,update_json_data):
        '''根据id更新部门名称'''
        update_url='/department/update'
        params = {'access_token': self.access_token}
        request_info = {'method': 'POST', 'url': update_url, 'params': params, 'json': update_json_data}
        return self.send_api(request_info)

    def del_depaerment(self,id):
        '''删除部门'''
        del_url='/department/delete'
        params = {'access_token': self.access_token, 'id': id}
        request_info = {'method': 'GET', 'url': del_url, 'params': params}
        return self.send_api(request_info)


    def department_detil(self,_id=None):
        '''部门详情'''
        detil_url = '/department/list'
        params = {'access_token': self.access_token, 'id': _id}
        request_info = {'method': 'GET', 'url': detil_url, 'params': params}
        return self.send_api(request_info)
