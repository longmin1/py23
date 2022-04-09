import  pytest

@pytest.fixture(scope='function')
def login():
    a='登录第一次'
    yield a
    print('继续一次')



def test_testcase(login):
    print(f'yield的返回值是{login}')
    print('测试yield')