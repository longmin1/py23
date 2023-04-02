'''Flask-SQLAlchemy 示例'''
from flask import Flask, current_app
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
#每个类表示的是一张表，如User表
class User(db.Model):
    #每一个类的变量表示数据库的一个表头
    #用户ID,primary_key是否主键
    ID=db.Column(db.Integer,primary_key=True)
    #用户名,字符串
    user_name=db.Column(db.String(80),unique=True,nullable=False)
    #用户密码,字符串
    user_pwd=db.Column(db.String(80),nullable=False)

if __name__ == '__main__':
    # 创建表
    with app.app_context():  # Create an :class:`~flask.ctx.AppContext`.
        db.create_all()

#[这个失败了，去公司用本地数据库试试][还没弄完】