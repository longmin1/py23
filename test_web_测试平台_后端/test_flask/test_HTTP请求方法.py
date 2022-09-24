from flask import Flask

app=Flask(__name__)
'''get 方法'''
# @app.route('/request/',methods=['get'])
# def hello_wrold():
#     return '{"code": 0, "msg":"get success"}'
'''post 方法'''
# @app.route('/request/',methods=['post'])
# def hello_wrold():
#     return {"code": 0, "msg":"post success"}
'''put方法'''
@app.route('/request/',methods=['put'])
def hello_wrold():
    return {"code": 0, "msg":"put success"}
# '''delete方法'''
@app.route('/request/',methods=['delete'])
def hello_wrold1():
    return {"code": 0, "msg":"delete success"}
if __name__ == '__main__':
    app.run()