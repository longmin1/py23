import requests



class TestHttpDmeo:
    base_url='https://httpbin.testing-studio.com'
    def test_demo(self):
        res=requests.get(url=f'{self.base_url}/get')
        print(res)#<Response [200]>
        print(res.status_code)#200
        print(res.text)#接口返回值
        result=res.text
        print(type(result))#<class 'str'>,返回的是str对象
        b=res.json()
        print(type(b))#<class 'dict'>,返回的是字典对象
        print(res.json())#接口的返回的json串

    def test_query(self):
        '''传参'''
        payload={
            'key':'value1',
            'key2':'value2'
        }
        res=requests.get(url=f'{self.base_url}/get',params=payload)
        print(res.text)

    def test_post_form(self):
        '''post form传参'''
        payload = {
            'key': 'value1',
            'key2': 'value2'
        }
        res=requests.post(url=f'{self.base_url}/post',data=payload)
        print(res.text)

    def test_upload_file(self):
        '''文件上传'''
        files={
            'file':open('file.text','rb')
        }
        res=requests.post(url=f'{self.base_url}/post',files=files)
        print(res.status_code)
        print(res.text)

    def test_header(self):
        #普通的headers
        headers={'user-agent':'my-app/0.0.1','cookie':'hogwarts=school'}
        res=requests.get(url=f'{self.base_url}/get',headers=headers)
        print(res.text)
        #cookie
        cookies=dict(cookies_are='working')#{'cookies_are': 'working'}
        # print(cookies)
        res1=requests.get(url=f'{self.base_url}/get',cookies=cookies)
        print(res1.text)

    def test_post_json(self):
        '''json串传参'''
        json_data = {
            'key': 'value1',
            'key2': 'value2'
        }
        r=requests.post(url=f'{self.base_url}/post',json=json_data)
        print(r.text)
        assert r.json()['json']['key']=='value1'

    def test_mubanjishu(self):
        '''模板技术 mustache,返回使用给定上下文呈现的给定模板字符串。'''
        import pystache
        print(pystache.render(template='Hi,{{person}}!', context={'person': 'tom'}))#Hi,tom!

    def test_json_duanyan(self):
        '''利用jsonpath来断言json内容'''
        from jsonpath import jsonpath
        from hamcrest import assert_that
        from hamcrest import equal_to
        res=requests.get('https://ceshiren.com/categories.json')
        print(res.text)
        print(jsonpath(res.json(), '$..name'))
        assert jsonpath(res.json(),'$..name')[0]=='提问区'
        assert_that(jsonpath(res.json(),'$..name')[1],equal_to('开源项目'))






