# dict_1={'a':1,'b':2}
# dict_2=dict()
# dict_2_1=dict([('a',1),('b',2)])
# print(dict_2_1)#->{'a': 1, 'b': 2}
# dict_3=dict(name='longmin')
# print(dict_3)#--->{'name': 'longmin'}
# dict_4={ x:y for x in 'hello' for y in 'world'}
# print(dict_4)
# dict_5={k:v for k,v in [('a',1),('b',2)]}
# print(dict_5)#---》{'a': 1, 'b': 2}
# dict_1={'a':1,'b':2}
# dict_1['name']='longmin'
# print(dict_1)#---{'a': 1, 'b': 2, 'name': 'longmin'}
# dict_1['a']=5
# print(dict_1)

#update()
# dict_1={'name': 'longmin'}
# dict_2={'name': 'bobo','age':20}
# dict_1.update(dict_2)
# print(dict_1)#{'name': 'bobo', 'age': 20}
# dict_2.update(dict_1)
# print(dict_2)#{'name': 'longmin', 'age': 20}

'''pop(key)'''
# dict_1={'name': 'longmin', 'age': 20}
# val=dict_1.pop('age')
# print(dict_1)
# print(val)

'''字典推导式'''
# dict_1={k:v for k,v in [('name','longmin'),('age',18)]}
# print(dict_1)
#
# dict_2={'a':1,'b':2,'c':3}
# #传统的方式
# data={}
# for k,v in dict_2.items():
#     if v>1:
#         data[k]=v**2
# print(data)
# #使用字典推导式
# data_new={k:v**2 for k,v in dict_2.items() if v>1}
# print(data_new)


def dict_new(dict1:dict)->dict:
    return {v:k for k,v in dict1.items()}

print(dict_new({'a': 1, 'b': 2, 'c': 3}))

