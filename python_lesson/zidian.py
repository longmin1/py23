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
dict_1={'name': 'longmin'}
dict_2={'name': 'bobo','age':20}
dict_1.update(dict_2)
print(dict_1)#{'name': 'bobo', 'age': 20}
dict_2.update(dict_1)
print(dict_2)#{'name': 'longmin', 'age': 20}