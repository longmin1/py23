'''Flask RESTX集成Swagger'''
from werkzeug.datastructures import FileStorage

from test_web_测试平台_后端.until.log_until import logger

'''namespace的使用'''
'''举例：原本代码'''
# from flask import Flask
# from flask_restx import Resource, Api
# app = Flask(__name__)
# api = Api(app)
# # 接口路径定义到类上，对应的不同请求操作创建不同的方法
# @api.route("/case")
# class TestCase(Resource):
#     # restful 风格的 get 方法
#     def get(self):
#         return {"code": 0, "msg": "get success"}
#     # restful 风格的 post 方法
#     def post(self):
#         return {"code": 0, "msg": "post success"}
#     # restful 风格的 put 方法
#     def put(self):
#         return {"code": 0, "msg": "put success"}
#     # restful 风格的 delete 方法
#     def delete(self):
#         return {"code": 0, "msg": "delete success"}
#
# @api.route("/demo")
# class Demo(Resource):
#     # restful 风格的 get 方法
#     def get(self):
#         return {"code": 0, "msg": "get success"}
#     # restful 风格的 post 方法
#     def post(self):
#         return {"code": 0, "msg": "post success"}
#     # restful 风格的 put 方法
#     def put(self):
#         return {"code": 0, "msg": "put success"}
#     # restful 风格的 delete 方法
#     def delete(self):
#         return {"code": 0, "msg": "delete success"}
'''改造使用namespace'''
# from flask import Flask
# from flask_restx import Resource, Api,Namespace
# app = Flask(__name__)
# api = Api(app)
# '''定义两个命名空间，以路由为分界'''
# demo_ns=Namespace('demo',description='demo学习')
# case_ns=Namespace('case',description='case管理')
# # 接口路径定义到类上，对应的不同请求操作创建不同的方法
# # @api.route("/case")
# '''@api.route("/case")替换成@demo_ns.route('')'''
# @demo_ns.route('')
# class TestCase(Resource):
#     # restful 风格的 get 方法
#     def get(self):
#         return {"code": 0, "msg": "get success"}
#     # restful 风格的 post 方法
#     def post(self):
#         return {"code": 0, "msg": "post success"}
#     # restful 风格的 put 方法
#     def put(self):
#         return {"code": 0, "msg": "put success"}
#     # restful 风格的 delete 方法
#     def delete(self):
#         return {"code": 0, "msg": "delete success"}
#
# # @api.route("/demo")
# @case_ns.route('')
# class Demo(Resource):
#     # restful 风格的 get 方法
#     def get(self):
#         return {"code": 0, "msg": "get success"}
#     # restful 风格的 post 方法
#     def post(self):
#         return {"code": 0, "msg": "post success"}
#     # restful 风格的 put 方法
#     def put(self):
#         return {"code": 0, "msg": "put success"}
#     # restful 风格的 delete 方法
#     def delete(self):
#         return {"code": 0, "msg": "delete success"}
# api.add_namespace(demo_ns,'/demo')
# api.add_namespace(case_ns,'/case')

'''Flask-RESTX中的swagger文档配置
这里主要练习第二种【推荐】，使用parser=api.parser()配合@api.expect(parser)或者@namespace.except(parser)装饰器实现入参的校验和传入
，具体可以看有道笔记'''
from flask import Flask, request
from flask_restx import Resource, Api,Namespace
app = Flask(__name__)
api = Api(app)
'''定义两个命名空间，以路由为分界'''
demo_ns=Namespace('demo',description='demo学习')

# 接口路径定义到类上，对应的不同请求操作创建不同的方法
# @api.route("/case")
'''@api.route("/case")替换成@demo_ns.route('')'''
@demo_ns.route('')
class TestCase(Resource):
    '''定义get参数'''
    get_parser=api.parser()
    get_parser.add_argument('id',type=int,location='args',required=True)
    get_parser.add_argument('case_title', type=str, location='args', required=True)
    # restful 风格的 get 方法
    '''expect进行传参'''
    @demo_ns.expect(get_parser)
    def get(self):
        logger.info(f'get输入的参数是:{request.args}')
        return {"code": 0, "msg": "get success"}

    '''定义post请求json格式参数'''
    post_parser=api.parser()
    # post_parser.add_argument('post_id',type=int,location='json',required=True)
    # post_parser.add_argument('post_case_title',type=str,location='json',required=True)
    '''定义post请求---->file格式的参数定义'''
    # post_parser.add_argument('post_flie',type=FileStorage,location='files')
    '''定义post请求----->form格式的参数定义'''
    # post_parser.add_argument('param1',type=int,help='name',location='form',required=True)
    # post_parser.add_argument('param2',type=int, help='password', location='form', required=True)
    '''定义post请求----->choice格式的参数定义'''
    post_parser.add_argument('choice',choices=('A','B','C'),location='args')

    '''小知识：file和Json会互斥，form和json也会互斥，最终生成不了swagger文档'''
    # restful 风格的 post 方法
    @demo_ns.expect(post_parser)
    def post(self):
        # logger.info(f'post_json输入的参数是:{request.json}')
        # logger.info(f'post_file输入的参数是:{request.files}')
        # logger.info(f'post_form输入的参数是:{request.form}')
        logger.info(f'post_choice输入的参数是:{request.args}')
        return {"code": 0, "msg": "post success"}
    # restful 风格的 put 方法
    def put(self):
        return {"code": 0, "msg": "put success"}
    # restful 风格的 delete 方法
    def delete(self):
        return {"code": 0, "msg": "delete success"}

api.add_namespace(demo_ns,'/demo')

if __name__ == '__main__':
    app.run(debug=True)
