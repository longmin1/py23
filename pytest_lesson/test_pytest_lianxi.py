import pytest
#加标签
@pytest.mark.sun
def test_case1():
    print('cccc')

@pytest.mark.sun1
def test_case11():
    print('cccc')

@pytest.mark.sun2
def test_case111():
    print('cccc')

#单参数的情况   一个参数name
list_params=['lily','mary','bobo']
@pytest.mark.parametrize('name',list_params)
def test_params(name):
    print(name)
    print(list_params)
    assert name in list_params

#多参数的情况
@pytest.mark.parametrize('num,except_num',[('3+5',8),('1+2',3),('7+12',19)])
def test_more_params(num,except_num):
    print(num)
    print(except_num)
    assert  eval(num)==except_num

#笛卡尔积
@pytest.mark.parametrize('wd',('appium','selenium','pytest'))
@pytest.mark.parametrize('code',('utf-8','gbk','gb2312'))
def test_dkej(wd,code):
    print(wd,code)

# if __name__ == '__main__':
    # pytest.main()
    # pytest.main(['test_pytest_lianxi.py::test_dkej','-vs'])
    # pytest.main(["test_pytest_lianxi.py","-vs","-m","sun"])
    # pytest.main(["test_pytest_lianxi.py", "-vs", "-k", "dkej"])
    #其实就是把原本的控制台命令行的每个pytest后面的参数 写到一个列表中，用','隔开，','相当于空格


# @pytest.mark.parametrize('x,y,expected',[[1,2,3],[1,5,6]])
# def test_pytest_excel(x,y,expected):
#     assert my_add(x,y)==expected
#     print('ccccss')


def test_case124():
    print('cccc')