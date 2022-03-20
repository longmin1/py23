#列表
#1，构造方法 list()
# li=list()
# print(type(li),li)
# li1=list('hogwarts')#把字符串转成列表
# print(type(li1),li1)#['h', 'o', 'g', 'w', 'a', 'r', 't', 's']
# #2，中括号填充元素[]
# li2=[1,2,3]
# li3=['hogwarts','hello']
# li4=[1,3,3.5,'hogwarts',[5,6,7]]
# print(li4)
# #3,列表推导式
# li5=[i for i in range(0,5) if i%2==0]
# print(li5)

#列表使用运算符号
#1，* 号
# li_num1=[1]
# print(li_num1*5)#[1, 1, 1, 1, 1]---加倍显示
#
# #2，+号
# li_num2=[1,2,3]
# li_num3=[5,6,7]
# print(li_num2+li_num3)#[1, 2, 3, 5, 6, 7]-会得到两个列表合起来

#3，extend()用法
# li=[]
# li.extend('hogwarts')#['h', 'o', 'g', 'w', 'a', 'r', 't', 's']
#
# li.extend([1,2,3])#[['h', 'o', 'g', 'w', 'a', 'r', 't', 's', 1, 2, 3]
#
# li.extend((5,6,7))#['h', 'o', 'g', 'w', 'a', 'r', 't', 's', 1, 2, 3, 5, 6, 7]
#
# li.extend({'a':1,'b':2})#['h', 'o', 'g', 'w', 'a', 'r', 't', 's', 1, 2, 3, 5, 6, 7, 'a', 'b']
# print(li)

#4,insert()
li=[1,2,3,4,5,6]
li.insert(0,'h')
print(li)#['h', 1, 2, 3, 4, 5, 6]


