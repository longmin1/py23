import urllib3

def test_Http():
    #创建线程池对象
    pm=urllib3.PoolManager()#PoolManager有个大写和小写的 注意这里是大写
    response=pm.request(method='GET',url='https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=nobdidobdid26815&wd=111&rsv_spt=1&rsv_iqid=0xabfb7fb300008565&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&rsv_sug3=4&rsv_sug1=3&rsv_sug7=100&rsv_btype=i&prefixsug=111&rsp=6&inputT=18432&rsv_sug4=18432&rsv_sid=36069_36175_31660_35979_35909_36165_34584_36122_36074_36126_35994_35318_26350_36114_36047_36103_36061&_ss=1&clist=&hsug=&f4s=1&csor=3&_cr1=32697')
    # print(response,type(response))#<class 'urllib3.response.HTTPResponse'>
    print(response.status)
    print(response.headers)
    print(response.data)