'''
简易demo
flask
'''
from test_web_测试平台_后端.until.log_until import logger

'''从官方文档种copy的最小应用程序代码'''
from flask import Flask

app = Flask(__name__)
'''路由'''
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!hahhahahah</p>"
#
# @app.route("/longmin")
# def hello_world1():
#     return "这是一个简易demo"

'''动态路由'''
# @app.route("/userinfo/<username>")
# def hello_world1(username):
#     return f"---这是{username}的个人信息"
'''动态路由限定类型'''
# @app.route('/userinfo/<int:username>')
# def hello_world(username):
#     return f"---这是{username}的个人信息"
'''加日志'''
@app.route('/userinfo/<string:username>')
def hello_world(username):
    logger.info(f'这是一条日志信息:{username}的个人信息')
    return f"---这是{username}的个人信息"

if __name__ == '__main__':
    app.run()#flask的实例对象来调用run()来运行