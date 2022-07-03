'''
录播实战
litemall

'''
import pytest
import requests
from jsonpath import jsonpath

from http_接口.http_接口lesson.log_until import logger


class TestLiteMall:

    def setup_class(self):
        pass
    # def teardown_class(self):
    #     '''删除商品，数据清理，通过接口'''
    #     url='http://litemall.hogwarts.ceshiren.com/admin/goods/delete'
    #     res=requests.post(url=url,json={'id':self.good_id},headers={'X-Litemall-Admin-Token': self.token})
    #     print(f'数据清理的结果是：{res.json()}')

    @pytest.fixture(scope='function')
    def test_login(self):
        login_data = {"username": "admin123", "password": "admin123", "code": ""}
        res = requests.post(url='http://litemall.hogwarts.ceshiren.com/admin/auth/login', json=login_data)
        token=res.json()['data']['token']
        print(token)
        return token

    def test_add_goods(self,test_login):
        '''上传商品接口测试'''
        # token=self.test_login
        # print(f'token的值是：{token}')
        headers = {'X-Litemall-Admin-Token': test_login}
        goods_json_data = {
            "goods": {"picUrl": "", "gallery": [], "isHot": False, "isNew": True, "isOnSale": True, "goodsSn": "ll",
                      "name": "yangyanng4"}, "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
            "products": [{"id": 0, "specifications": ["标准"], "price": "1", "number": "1", "url": ""}], "attributes": []}
        res=requests.post(url='http://litemall.hogwarts.ceshiren.com/admin/goods/create', headers=headers,
                      json=goods_json_data)
        print(res.json())

    @pytest.fixture(scope='function')
    def test_client_login(self):
        '''client登录获取token接口'''
        login_url='http://litemall.hogwarts.ceshiren.com/wx/auth/login'
        login_data={"username":"user123","password":"user123"}
        res=requests.post(url=login_url,json=login_data)
        # print(res.json()['data']['token'])
        client_token=res.json()['data']['token']
        return client_token
        # print(jsonpath(res.json(),'$..token'))

    @pytest.fixture(scope='function')
    # @pytest.mark.parametrize('name',['hogwarts','yangyanng1'])
    def test_get_goods_list(self,request,test_login):
        '''商品列表接口（可以提取商品ID）'''
        url='http://litemall.hogwarts.ceshiren.com/admin/goods/list'
        headers = {'X-Litemall-Admin-Token': test_login}
        data={"name": request.param,"order": "desc","sort": "add_time"}
        res=requests.get(url=url,params=data,headers=headers)
        good_id = res.json()['data']['list'][0]['id']
        logger.debug(f'good_id是：{good_id}')
        # self.good_id=good_id
        # self.token=test_login
        # print(good_id)
        return good_id

    def test_product_id(self,test_login):
        '''商品详情接口（可以提取商品库存ID）'''
        '''{'errno': 502, 'errmsg': '系统内部错误'}这个我暂时报错了，所以没用上'''
        url = "http://litemall.hogwarts.ceshiren.com/admin/goods/detail"
        headers = {'X-Litemall-Admin-Token': test_login}
        data = {"id": 1181668}
        res = requests.get(url=url, params=data, headers=headers)
        product_id = res.json()
        print(product_id)
        # return product_id
    @pytest.mark.parametrize('test_get_goods_list',['hogwarts','yangyanng3','yangyanng4'],indirect=True)
    def test_client_shopping_cart(self,test_client_login,test_get_goods_list):
        '''客户端添加购物车'''
        url='http://litemall.hogwarts.ceshiren.com/wx/cart/add'
        data={"goodsId":test_get_goods_list,"number":1,"productId":140}
        headers={'X-Litemall-Token':test_client_login}
        res=requests.post(url=url,headers=headers,json=data)
        logger.debug(f'添加购物车的结果是：{res.json()}')
        assert res.json()['errmsg']=='成功'
        # print(res.json())

