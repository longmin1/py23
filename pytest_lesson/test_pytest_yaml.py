import pytest
import yaml


class TestDemo():

    def test_yaml(self):
        with open('./env.yaml','r')as f:
            print(yaml.safe_load(f))#[{'test': '127.0.0.1'}, 'test1 test2', {'envinr': '127.0.0.243'}]

    @pytest.mark.parametrize('env',yaml.safe_load(open('./env.yaml')))
    def test_demo(self,env):
        if 'test' in env:
            print('测试环境')
            print(env,type(env))
        elif 'dev' in env:
            print('开发环境')
        else:
            print('生产环境')
            print(env['envinr'])

#把python数据转换成yaml格式 写进yaml文件中
def test_python_yaml():
    python_data = [{'nihao': 'hahhah'}, 'lily', 'mary', {'wobuhao': 'yeyyeye'}]
    with open('./env.yaml','a',encoding='utf-8')as f:
        yaml.dump(python_data,f)