'''Flask RESTX接口配置'''

from flask import Flask
from flask_restx import Api, Resource

app=Flask(__name__)
api=Api(app)
#使用Api来添加路由
@api.route('/hello')
#类要继承Resource木块
class Demo(Resource):
    '''restful风格的接口示例'''
    def get(self):
        return 'this is a get request,success!!!'
    def post(self):
        return 'this is a post request,success!!!'