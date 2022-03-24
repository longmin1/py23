#python面对对象编程

#创建一个类
class Person:
    name='default'
    age=0
    gender='male'
    weight=0
    def __init__(self,name,age,gender,weight):
        self.name=name
        self.age=age
        self.gender=gender
        self.weight=weight

    # def set_param(self,name):
    #     self.name=name
    #
    # def set_age(self, age):
    #     self.age = age
    @classmethod
    def eat(self):
        print('eating')
        print(self.name)

    def play(self):
        print('playing')

    def jump(self):
        print('jump')

# Person().eat()
# zhangsan=Person('zhangsan',18,'male',130)#运行这个类的实例化的时候，就会首先去运行init构造函数
# print(zhangsan.name)
# zhangsan.set_param('zhangsan')
# print(zhangsan.name)#打印实例化的张三的实例化变量
# print(Person.name)#打印类变量
# Person.eat()
# zhangsan.eat()

class Airplan:
    name='川航3u8633'
    color=''

    def set_color(self,color):
        self.color=color
        print(self.color)

    def set_name(self,name):
        self.name=name
        print(self.name)

class MinyongAirplan(Airplan):

    def load_person(self,num):
        print(f'民用机能装{num}人')

    def set_name(self,name):
        print('改写了父类的这个同名的这个类方法')

minyong=MinyongAirplan()
minyong.set_color('red')
minyong.load_person(100)
minyong.set_name('民用机1号')
print(minyong.name)#继承了父类的类变量
# air1=Airplan()
# air1.set_name('第一架飞机')
# air1.set_color('红色')
# print(Airplan.name)

