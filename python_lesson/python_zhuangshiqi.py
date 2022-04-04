#函数引用
# def hogwarts():
#     print('hogwarts')
#
# harry=hogwarts#函数赋值给一个变量harry，记得函数不加（）
# harry()
'''简单装饰器'''
# def xinxi(func):
#     def student(*args,**kwargs):
#         print('开始了')
#         print(args,kwargs)
#         func(*args,**kwargs)
#         print('---bye--------')
#     return student
#
# @xinxi
# def func_1():
#     print('我要那17-22k')

# func_1()
import datetime

'''简单装饰器'''
from functools import wraps

# def xinxi(func):
#     def student(*args,**kwargs):
#         # print(args)
#         # print(kwargs)
#         func(*args,**kwargs)
#         print('打印完了')
#     return student
#
# @xinxi
# def sng(s,n,g):
#     print(f'学校是{s},姓名是{n},性别是{g}')

# sng(s='hogwarts',n='longmin',g='girl')
# xinxi(sng(s='hogwarts1',n='longmin1',g='girl1'))
#
# def extend(func):#func--函数--把函数作为参数传进来，函数作为参数是不用加()的，调用才是()
#     '''普通装饰器'''   #每次return-->直到return到装饰器的第一个函数
#     @wraps(func)
#     def hello(*args,**kwargs):#*args,**kwargs--涵盖了所有参数类型，看到这个就表示这个函数接收所有类型参数
#         print('nihao')
#         print(args)#打印参数传参的元组的值，和字典的值
#         print(kwargs)
#         func(*args,**kwargs)
#         print('bye')
#     return hello
# @extend
# def tmp():#传参元组和字典
#     print('hello world')
#
# tmp()

#实现一个计时器的装饰器，计算函数执行时间
def timer(func):
    def inner():
        '''装饰器逻辑'''
        start_time=datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f'函数执行时间:{end_time-start_time}')
        pass
    return inner

@timer
def hogwarts():
    print('hogwarts学校')

hogwarts()

