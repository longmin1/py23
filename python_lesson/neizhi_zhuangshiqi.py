'''类方法'''



class MethodClass:
    CLASS_PARAM=0


    def putong_method(self):
        self.a = 'adf'
        print('这是一个普通方法')

    @classmethod
    def class_method(cls):#这是一个类方法
        print(cls.CLASS_PARAM)

# MethodClass.class_method()

'''静态方法'''
class StaticMethod:

    def putong_method(self):
        self.a = 'adf'
        print('这是一个普通方法')

    @classmethod
    def class_method(cls):  # 这是一个类方法
        print('这是一个类方法')

    @staticmethod
    def static_method():#静态方法，是没有self这个参数的，可以删掉self  静态方法是不能通过self.来进行调用的
        print('这是一个静态方法')

    @staticmethod
    def static_method_1(params):
        print('这是一个静态方法2号')
        print(params)#静态方法传普通参数这样传
# StaticMethod.static_method()
# StaticMethod.static_method_1('类静态方法传参')
# s=StaticMethod()
# s.static_method()
# s.static_method_1('静态2号')

'''例子：在不改变构造函数的基础上进行丰富代码的健壮性(假设传入的格式是json,或者字符串的)'''
class DateFormat:

      def __init__(self,year=0,month=0,day=0):
          self.year=year
          self.month=month
          self.day=day

      def out_data(self):
          return f'输入的时间为{self.year}年，{self.month}月，{self.day}日'

      @classmethod
      def json_format(cls,json_data):
          #利用类方法来兼容输入json_data这种格式的处理模式  可以不用改变构造函数
          year=json_data['year']
          month=json_data['month']
          day=json_data['day']
          return cls(year,month,day)#相当于返回类的实例，等同于DateFormat(year,month,day)类的实例，类本身，相当于构建函数的实例



# year,month,day=2017,7,1
# print(DateFormat.json_format({'year': 2017, 'month': 7, 'day': 1}).out_data())

#两个英雄对战
class Game:

    def __init__(self,hero1,hero2):
        self.hero1=hero1
        self.hero2=hero2

    def fight(self):
        print(f'对战双方是{self.hero1} vs {self.hero2}')

    @staticmethod
    def game_start():#独立的静态函数  无关任何类变量以及实例变量
        print('比赛开始了')
# Game.game_start()

# game_1=Game('bobo','tom')
# game_1.game_start()
# game_1.fight()
from typing import List
a:List[float]=[]
a=['1',1,2]