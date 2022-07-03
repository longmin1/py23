'''
连接数据库
与断言
'''
import pymysql


class TestConnectDatabase:
    def get_connect(self):
        connect = pymysql.connect(host='litemall.hogwarts.ceshiren.com',
                                  user='test',
                                  password='test123456',
                                  database='litemall',
                                  port=13306,
                                  charset='utf8mb4')
        return connect

    def execute_sql(self,sql):
        con=self.get_connect()
        cursor=con.cursor()#游标对象
        cursor.execute(sql)# 执行SQL
        result=cursor.fetchone()# 查询记录
        print(result[4])#1064006
        return result[4]

    def test_assert_database(self,sql,exc_result):
        act_result=self.execute_sql(sql)
        assert act_result==exc_result
sql='SELECT * from litemall_cart where user_id=2 LIMIT 1 ;'
exc_result='3D纯棉护颈加翼记忆枕'
TestConnectDatabase().test_assert_database(sql=sql,exc_result=exc_result)#断言ok