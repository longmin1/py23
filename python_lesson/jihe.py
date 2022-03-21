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

