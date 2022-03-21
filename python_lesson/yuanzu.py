#元组
'''注意单元素元组，逗号 一定不能少'''
# tup=(1)
# print(type(tup),tup)#----><class 'int'> 1
# tup_1=(1,)
# print(type(tup_1),tup_1)#----><class 'tuple'> (1,)
# tup_2=1,
# print(type(tup_2),tup_2)#---><class 'tuple'> (1,)


#元组的index(item)方法
# tup=tuple('hogwarts')
# print(tup)#('h', 'o', 'g', 'w', 'a', 'r', 't', 's')
# print(tup.index('w'))#3--->返回这个值的索引值

#元组的count(item)--->返回这个元素出现的次数
# tup=tuple([1,2,3,4,6,7,1,2,3,4,1,2,3])
# print(tup)#(1, 2, 3, 4, 6, 7, 1, 2, 3, 4, 1, 2, 3)
# print(tup.count(1))#3-->统计1这个元素出现的次数

#元组的解包
#1,传统赋值的方式
# tup=1,2,3
# print(tup)#(1, 2, 3)
# a=tup[0]
# b=tup[1]
# c=tup[2]
# print(a,b,c)#1 2 3

#2,解压平行赋值
tup=1,2,3
a,b,c=tup
print(a,b,c)#1 2 3
list_1=['hello','mama','baba']
e,d,f=list_1
print(e,d,f)#hello mama baba

