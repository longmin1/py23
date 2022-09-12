'''
加密的文件
以及再本地进行base64 测试平台开发-后端.json>测试平台开发-后端.txt
然后再加密的文件的目录进行起一个python服务
python -m http server 9999
然后访问这个服务地址127.0.0.1:9999
'''
import json

import requests
import base64

class TestHttp():
    def test_jiemi(self):
        url='http://127.0.0.1:9999/longmin.txt'
        res=requests.get(url=url)
        # print(res.text)#加密的内容
        # -----解密------
        res1=base64.b64decode(res.content)#b64encode解密
        # print(res1)#[100%]b'[\n    {\n       "name": "",\n       "name_en": "JISHU2",\n ....
        # 格式转换下转成json格式化一下
        result=json.loads(res1)
        print(result)#[{'name': '', 'name_en': 'JISHU2', 'parentid': 1, 'order': 2, 'id': 3, 'expected': 40058}.....
