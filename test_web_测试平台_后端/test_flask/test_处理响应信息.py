from flask import Flask, jsonify, render_template, make_response

app = Flask(__name__)

'''返回文本'''


@app.route('/text')
def res_text_api():
    return '这是一个文本返回接口'


'''返回元组'''


@app.route('/tuple', methods=['get'])
def res_tuple():
    return '返回的是元组类型+status', 200


@app.route('/tuple1')
def res_tuple1():
    return '返回的是元组类型+header', {'headers': 'tuple_res_add'}


@app.route('/tuple2')
def res_tuple2():
    return '返回的是元组类型+status+header', 201, {'headers': 'tuple_res_add'}


'''返回Json'''


@app.route('/json')
def res_json():
    '''直接返回dict,页面会自动转成json的'''
    return {'status': 200, 'result': 'success'}


@app.route('/json1')
def res_json1():
    '''通过jsonify()把键值对转成json,页面自然显示json格式'''
    # return jsonify({'status':201})
    return jsonify(status=201, name='ll', result='success')


'''返回html，
注意demo.html要放在templates这个目录下，这个名字是固定的'''


@app.route('/html')
def res_html():
    return render_template('demo1.html')


'''设置额外数据,make_response()'''


@app.route('/makeresponse')
def res_make_response():
    '''添加返回数据'''
    res = make_response(render_template('demo3.html'))
    '''设置cookie'''
    res.set_cookie('name', 'lili')
    '''设置响应头信息'''
    res.headers['add_header'] = 'lili_add'
    return res
