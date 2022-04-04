import pymysql
def get_conn():
    conn=pymysql.connect(user='lbx',
            password="61af8346137c7a8b29b8",
            host='10.243.0.22',port=3306,
            database='shopcc-order',charset="utf8mb4")
    return conn
