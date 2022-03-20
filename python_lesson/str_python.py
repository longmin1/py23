#\-->转义符
str_a='woaini\n3564&&^^^'
print(str_a)#会\换行
#woaini
#3564&&^^^
str_b='woaini\\n3564&&^^^'
print(str_b)#woaini\n3564&&^^^  \\n--》防止\n换行

str_c=r'woaini\n3564&&^^^'
print(str_c)#woaini\n3564&&^^^   r--->忽略转义符的作用


list_a=[0,2,4,5,6,8,9,'sdd','fsf','v',10]
print(list_a[-1::-1])
print(list_a[len(list_a)::-1])
print(list_a[::-1])
print(list_a[::1])




list_b=['foo','card','bar','aaaa','abab']
list_c=['abab','card','bar','aaaa','foo']
# list_b.sort()
g=lambda x:len(set(list(x)))
# print(list_b)
list_c.sort(key=g)
print(list_c)#['aaaa', 'abab', 'foo', 'bar', 'card']


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2,4,3, 4,6), (4, 1,7,1, 3,6)]
# 指定第二个元素排序
random.sort(key=takeSecond)
# 输出类别
print('排序列表：', random)#排序列表： [(4, 1, 7, 1, 3, 6), (2, 2, 4, 3, 4, 6)]

#格式化输出
print('my name is %s'%'longmin')
print('my name is {}'.format('longmin'))
print('my name is {},my age is {}'.format('longmin',27))
print('my name is {0},my age is {1},i love {2}'.format('longmin',27,'watch douyin'))
print('my name is {name},my age is {age}'.format(name='longmin',age=27))
name='longmin'
age=27
name_1,age_1='longmin',27#变量也可以这样横着写
print(f'my name is {name},my age is {age}')

#join拼接
list_name=['l','o','n','g','m','i','n','g']
print(''.join(list_name))
print('&'.join(list_name))#l&o&n&g&m&i&n&g

#split切割---切割的结果是列表形似
str_name='l&o&n&g&m&i&n&g'
print(str_name.split('&'))#['l', 'o', 'n', 'g', 'm', 'i', 'n', 'g']

#replace替换
c='my name is longmin'
print(c.replace('longmin','yangbin'))#my name is yangbin

#strip去掉首尾的空格
d=' my name is longmin '
print(d.strip())#去掉首尾空格的my name is longmin
print(d.rstrip())# my name is longmin--->去掉最右侧的空格
print(d.lstrip())#my name is longmin ----->去掉最左侧的空格

list_a=['a','b','c']
str_a='adcde'
str_b='bcde'
print('a'in list_a)
print('a' not in list_a)
print('a'in str_a)
print('a'not in str_a)
print('a' in str_b)