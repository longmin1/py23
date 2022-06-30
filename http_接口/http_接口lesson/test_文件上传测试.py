'''
测试文件上传
以及用元组方式传参，指定filename
'''
import requests


class TestFile():
    proxy={'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
    files={'hogwartsfile_name':open('file.text','rb')}

    def test_file_upload(self):
        res=requests.post(url='https://httpbin.testing-studio.com/post',files=self.files,proxies=self.proxy,verify=False)
        print(res.text)

    def test_file_name_zhiding(self):
        '''用元组方式指定自己命名的filename'''
        zhidin_filename={'hogwartsfile_name':('longmin_filename',open('file.text','rb'))}
        res=requests.post(url='https://httpbin.testing-studio.com/post',files=zhidin_filename,proxies=self.proxy,verify=False)
