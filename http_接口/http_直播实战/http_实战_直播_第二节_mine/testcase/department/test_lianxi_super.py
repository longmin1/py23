'''
练习理解继承
'''
class Faster():
    fastername='longtinghua'
    mastername='xuyan'

    def __init__(self):
        self.xxl='xxl'
        self.vvv='---'

    def eat(self):
        self.aihao='eat'
        print(self.aihao)
    def eat_1(self):
        self.eat1='xxx'
        print(self.eat1)

class Sun(Faster):
    sunname='longmin'

    def __init__(self):
        super().__init__()
        self.cc='cc'
        self.xxl='hahahahahxxxl------------'
        self.sunname='gaixiexixix----'

    def play(self):
        print('喜欢玩:')

    def eat(self):
        print('喜欢吃',self.xxl,self.fastername,self.vvv)

s=Sun()
# s.fastername='vvvv'
# # Faster.fastername='-----'
# #实例改变不了类变量，类变量可以改变类变量
# print(s.fastername)
# # s.fastername='longlong'
# # Faster.fastername='xxx'
# # print(s.fastername)
# print(Faster.fastername)
# print(s.mastername,Sun.sunname,Sun().sunname)
s.eat()
# print(s.xxl)

class Foo:
    def f1(self):  # _Foo__f1()
        print('Foo.f1')

    def f2(self):
        #
        print('Foo.f2')
        self.f1()  # _Foo__f1()



class Bar(Foo):
    def __f1(self):  # # _Bar__f1()
        print('Bar.f1')

    def f3(self):
        self.f2()
    def f4(self):
        self.f1()

bar = Bar()
print(Bar.mro())#注意 起始类名去查，Bar--->起始类名.mro()
# # obj.f2()
# obj.f3()
# obj.f4()

class A:
    def test(self):
        print('from A')
        super().test()
'''用于调用下一个父类的方法B.test'''
'''super（）方法的存在就是为了解决多重继承的问题，
在一个父类中使用super（）方法用于调用下一个父类的方法'''

class B:
    def test(self):
        print('from B,xxx')


class C(A, B):
    pass


c = C()
c.test()
print(C.mro())

