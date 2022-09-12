'''
只争对接口通用进行封装，不涉及业务
'''
import requests

from http_接口.http_直播实战.http_实战_直播_第二节_mine.untils.log_utils import logger


class BaseApi():
    BASE_URL=''
    xxl_cls=''




    def send_api(self,request_info):
       '''
       对requests进行的二次封装
       :return: 接口对应的返回值
       '''

       if self.BASE_URL:
           request_info['url'] = self.BASE_URL + request_info.get('url')
       logger.info(f'传入的参数为：{request_info}')
       res=requests.request(**request_info)
       logger.info(f'响应的结果为:{res.text}')
       return res