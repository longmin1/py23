#集合的方法
#1,add()--->add(item)
# set_1=set()
# print(set_1)#空集合
# set_1.add(1)
# set_1.add('hogwarts')
# print(set_1)#{1, 'hogwarts'}

#2,update()
# str='hogwarts'
# list_1=[1,2,3]
# tup_1=(4,5,6)
# set_1={'a','b','c'}
# set_test=set()
# #批量添加字符串中的元素
# set_test.update(str)
# print(set_test)#{'h', 'w', 'o', 't', 'g', 'a', 'r', 's'}
# #批量添加列表中的元素
# set_test.update(list_1)
# print(set_test)#{1, 2, 3}
# #批量添加元组中的元素
# set_test.update(tup_1)
# print(set_test)#{4, 5, 6}
# #批量添加集合中的元素
# set_test.update(set_1)
# print(set_test)#{'c', 'a', 'b'}

# list_1=[1,2,3,5]
# a=list_1.pop()
# print(a)--->列表pop()不传值删除最后一个
# list_1=[2,3,4,5,6]
# set_1=set(list_1)
# b=set_1.pop()#--->集合随机剔除
# print(b)

#集合的交集运算
#可以使用 intersection 也可以使用 &
# set_1={1,2,3,4,5,7,8,0}
# set_2={2,5,6,3,4,9}
# print(set_1.intersection(set_2))#---{2, 3, 4, 5}
# print(set_1&set_2)#{2, 3, 4, 5}

#集合的并集运算
#可以使用 union 也可以使用 |
# set_1={1,2,3,4,5,7,8,0}
# set_2={2,5,6,3,4,9}
# print(set_1.union(set_2))
# print(set_1|set_2)

#集合的差集运算
#可以使用 difference 也可以使用 -
# set_1={1,2,3,4,5,7,8,0}
# set_2={2,5,6,3,4,9}
# #属于set_1但不属于set_2的集合
# print(set_1.difference(set_2))
# print(set_1-set_2)

# set_1=set('hogwartsss')
# set_2=set('hello world')
# print(set_1,set_2)
# print(set_1&set_2)

#集合推导式
set_x={i if i in 'cccc' else 'wd' for i in 'hogwarts'}
print(set_x)
#推导式也可以结合if-else使用
#但是要把if else放在前面  for循环放在后面
set_y={ i for i in 'hogwartsss' if i in 'hello world'}
print(set_y)

