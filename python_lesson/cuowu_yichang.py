#错误与异常
def div(a,b):
    try:
        list1=[1,2,3]
        print(list1[2])
        print(a/b)
    except ZeroDivisionError as e:
        print(e)
        # return '这是个异常'
    except Exception as E:#捕获所有异常类型
        print( E)
    else:#try那里没有发生异常的时候  就会执行else这里
        print('没有异常的时候执行')

    finally:#无论有无异常  都会执行
        print('一定要执行')


# div(1, 1)

def set_age(num):
    if num<=0 or num>200:
        # raise ValueError#raise 抛出异常
        raise ValueError(f'值错误{num}')
    else:
        print(f'年龄是{num}')

# set_age(-1)

#自定义异常
class MyException(Exception):

    def __init__(self,msg):
        print(f'这是一个自定义的异常:{msg}')

def set_age_1(num):
    if num<=0 or num>200:
        # raise ValueError#raise 抛出异常
        raise ValueError(f'值错误{num}')

    elif num==1:
        raise MyException(num)
    else:
        print(f'年龄是{num}')

set_age_1(1)