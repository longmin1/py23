'''在谷歌输入：Flask-SQLAIchemy，就可以找到插件的官方文档
pip install flask-sqlalchemy'''

'''Flask-SQLAlchemy的实例化'''
#导入FLASK的类
# from flask import Flask
# #导入flask-sqlalchemy中的SQLAlchemy模块
# from flask_sqlalchemy import SQLAlchemy
#
# #实例化FLASK
# app=Flask(__name__)
# #将app与Flask-SQLAlchemy进行绑定，实例化一个db对象
# db=SQLAlchemy(app)
'''Flask-SQLAlchemy配置'''
'''常用的四个配置
SQLALCHEMY_DATABASE_URI连接数据库的 URL 配置
SQLALCHEMY_TRACK_MODIFICATIONS追踪对象的修改
SQLALCHEMY_BINDS用于多数据库连接的配置
SQLALCHEMY_POOL_SIZE连接池的配置 默认为 5
'''
'''SQLALCHEMY_DATABASE_URI常见连接格式
sqlite:sqlite:///数据库db文件所在的路径
mysql:mysql+pymysql://username:password@host:port/database'''

'''Flask-SQLAlchemy 示例'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
#mysql的信息
username="root"
pwd="123456"
host="192.168.62.129"
port="3306"
database="demo"
# 设置mysql 链接方法
app.config['SQLALCHEMY_DATABASE_URI']=f'mysql+pymysql://{username}:{pwd}@{host}:{port}/{database}?charset=utf8'
# 定义应用使用数据库的配置
# 设置SQLALCHEMY_TRACK_MODIFICATIONS参数 不设置该配置的时候会抛出警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

#将app与Flask-SQLAlchemy 的 db 进行绑定
db=SQLAlchemy(app)
#这样设置好，最后db对象就可以连接到config里设置的数据库
