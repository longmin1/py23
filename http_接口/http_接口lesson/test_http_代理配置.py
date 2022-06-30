'''
http代理配置
'''

import requests
class TestDaiLi:
    base_url = 'https://httpbin.testing-studio.com'
    # 定义一个代理的配置，
    # key为协议，value为代理工具的配置
    proxy = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    def test_http_daili(self):
        #通过proxies传递代理配置
        requests.post(url=f'{self.base_url}/post',proxies=self.proxy,verify=False)

    def test_query(self):
        '''传参'''
        payload={
            'key':'value1',
            'key2':'value2'
        }
        res=requests.get(url=f'{self.base_url}/get',params=payload,proxies=self.proxy,verify=False)
        print(res.text)

    def test_post_form(self):
        '''post form传参'''
        payload = {
            'key': 'value1',
            'key2': 'value2'
        }
        res=requests.post(url=f'{self.base_url}/post',data=payload,proxies=self.proxy,verify=False)
        print(res.text)

    def test_upload_file(self):
        '''文件上传'''
        files={
            'file':open('file.text','rb')
        }
        res=requests.post(url=f'{self.base_url}/post',files=files,proxies=self.proxy,verify=False)
        print(res.status_code)
        print(res.text)

    def test_header(self):
        #普通的headers
        headers={'user-agent':'my-app/0.0.1'}
        res=requests.get(url=f'{self.base_url}/get',headers=headers,proxies=self.proxy,verify=False)
        print(res.text)
        #cookie
        cookies=dict(cookies_are='working')#{'cookies_are': 'working'}
        # print(cookies)
        res1=requests.get(url=f'{self.base_url}/get',cookies=cookies,proxies=self.proxy,verify=False)
        print(res1.text)

    def test_post_json(self):
        '''json串传参'''
        json_data = {
            'key': 'value1',
            'key2': 'value2'
        }
        r=requests.post(url=f'{self.base_url}/post',json=json_data,proxies=self.proxy,verify=False)
        print(r.text)
        assert r.json()['json']['key']=='value1'

    def test_json_duanyan(self):
        '''利用jsonpath来断言json内容'''
        from jsonpath import jsonpath
        from hamcrest import assert_that
        from hamcrest import equal_to
        res=requests.get('https://ceshiren.com/categories.json',proxies=self.proxy,verify=False)
        print(res.text)
        print(jsonpath(res.json(), '$..name'))
        assert jsonpath(res.json(),'$..name')[0]=='提问区'
        assert_that(jsonpath(res.json(),'$..name')[1],equal_to('开源项目'))