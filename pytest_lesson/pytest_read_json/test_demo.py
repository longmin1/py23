import json

import pytest

'''数据转成json格式写入文档'''

# python_data={'data':[1,2,3],'data1':[2,3,5],'data3':[3,4,7]}
# with open('./data1.json','w',encoding='utf-8')as f:
#     json.dump(python_data,f)

'''把json 文件中的数据读出来'''
# def test_read_json():
#     with open('./data.json','r',encoding='utf-8')as f:
#         # print(json.load(f))#第一种读法
#         a=json.load(f)
#         f.seek(0)#使光标处于最开始的位置 不然会读出是空的，因为read已经读完了 光标就处于最下面的  下一个继续读就读不到了
#         print(json.loads(f.read()))##第二种读法
#         f.seek(0)
#         # b=json.loads(f.read())
#         print(a,type(a))
        # assert json.load(f)==json.loads(f.read())

'''pytest 结合json进行数据驱动'''
def add(x,y):
    return x+y



def get_json_data():
    """

    :return: [[1, 2, 3], [2, 3, 5], [3, 4, 7]]
    """
    with open('./data1.json','r',encoding='utf-8')as f:
        data=json.load(f)
        # print(data.values())#dict_values([[1, 2, 3], [2, 3, 5], [3, 4, 7]])
        # print(list(data.values()))#[[1, 2, 3], [2, 3, 5], [3, 4, 7]]
        return list(data.values())

# @pytest.mark.parametrize('x,y,excepted',get_json_data())
# def test_case(x,y,excepted):
#     assert add(x,y)==excepted


# @pytest.fixture(scope='module')
# def login(request):
#     a=request.param
#     # a=1
#
#     print('xxxxxxx')
#     return a
#
# @pytest.mark.parametrize('login',['lily','tom'],indirect=True)
# def test_login(login):
#     a=login
#     print(f'login的返回值是{a}')









