'''flask RESTX接口使用'''

from flask import Flask
from flask_restx import Api, Resource

app=Flask(__name__)
api=Api(app)

@api.route('/user','/user1','/user2')

class NameDemo(Resource):
    def get(self):
        return 'get success!!!'
    def post(self):
        return 'post success!!!'
    def put(self):
        return 'put success!!!'
    def delete(self):
        return 'delete success!!!'

@app.route('/userinfo/<username>')
def func(username):
    return f'{username}的信息获取成功!!!'
api.add_resource(NameDemo,'/user3')