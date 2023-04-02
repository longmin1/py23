'''ORM映射'''
#每个类表示的是一张表，如User表
# class User(db.Model):
#     #每一个类的变量表示数据库的一个表头
#     #用户ID,primary_key是否主键
#     ID=db.Column(db.Integer,primary_key=True)
#     #用户名,字符串
#     user_name=db.Column(db.String(80),unique=True,nullable=False)
#     #用户密码,字符串
#     user_pwd=db.Column(db.String(80),nullable=False)

'''SQLAlchemy是python中最有名的ORM框架，
在FLASK中一般使用Flask-SQLAlchemy来进行操作数据库【flask里又对SQLAlchemy进行了封装】
[from flask_sqlalchemy import SQLAlchemy]'''
#官方文档给的最小demo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


