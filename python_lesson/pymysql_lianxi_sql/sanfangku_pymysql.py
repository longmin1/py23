import sys
from python_lesson.pymysql_lianxi_sql import get_conn
'''普通查询'''
conn=get_conn()
# conn=pymysql.connect(user='lbx',
#             password="61af8346137c7a8b29b8",
#             host='10.243.0.22',port=3306,
#             database='shopcc-order',charset="utf8mb4")#写到了这个目录中的init模块中了
cursor=conn.cursor()

sql='SELECT dept_id from scc_order_info where order_id=999327731577315328'
try:
    cursor.execute(sql)
    print(cursor.fetchone()[0])
except Exception as e:
    print(sys.exc_info())#打印系统报错
finally:
    conn.close()

'''插入语句，进行提交回滚操作'''
conn=get_conn()
cursor=conn.cursor()
sql="UPDATE scc_order_info set dept_id='730881261588975616' where order_id=999327731577315328;"
try:
    cursor.execute(sql)
    conn.commit()
    print('提交了')
except Exception as e:
    conn.rollback()
    print(sys.exc_info())
finally:
    conn.close()
    print('关闭了')

