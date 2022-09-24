'''利用flask封装的request来进行处理请求的数据'''
import requests as requests
from flask import Flask, request

app=Flask(__name__)
'''get 请求参数类型params数据处理'''
# @app.route('/request/',methods=['get'])
# def get_func():
#     print(request.args)
#     res=request.args
#     print(f'name:{res.get("name")}，password:{res.get("pw")}')
#     return {"code": 0, "msg":"get success"}

# '''post 请求参数类型json数据处理'''
# @app.route('/request/',methods=['post'])
# def get_func():
#     print(request.json)
#     res=request.json
#     print(f'name:{res.get("name")}，password:{res.get("pw")}')
#     return {"code": 0, "msg":"post success"}
'''post/put 请求参数类型form数据处理'''
# @app.route('/request/',methods=['post'])
# def get_func():
#     print(request.form)
#     res=request.form
#     print(f'表单的数据：name:{res.get("name")}，password:{res.get("pw")}')
#     return {"code": 0, "msg":"post form success"}
'''post  处理请求参数为文件上传的数据处理'''
@app.route('/request/',methods=['post'])
def get_func():
    print(request.files)
    flieobj=request.files.get('file')
    filename=flieobj.filename
    flieobj.save('./wojiatext.txt')
    print(f'文件的名字为：name:{filename}')
    return {"code": 0, "msg":"post update file success"}

'''自己写的上传文件的接口'''
# def test_update_file():
#     url='http://127.0.0.1:5000/request'
#     file={'file':open('text.txt','rb')}
#     res=requests.post(url=url,files=file)
#     assert res.status_code==200

# update_file()