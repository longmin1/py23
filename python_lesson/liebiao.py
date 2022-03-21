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
# li=[1,2,3,4,5,6]
# li.insert(0,'h')
# print(li)#['h', 1, 2, 3, 4, 5, 6]

#5，pop()
# li=[1,2,3,4,5,6]
# print(li)
# li.pop(1)#-->剔除掉索引为1的那个值--也就是2
# print(li)#[1, 3, 4, 5, 6]
# data=li.pop()
# print(data)#6--不要索引就删除掉最后那个数
# print(li)#[1, 3, 4, 5]
# #注意索引不能超出范围
# li.pop(99)#--->IndexError: pop index out of range
# #需要操作的列表不要为空了
# li_1=[]
# li_1.pop()#--->IndexErroe:pop from empty list

#6,remove()
# li=[1,2,3,4,1,23,6]
# li.remove(1)
# print(li)#[2, 3, 4, 1, 23, 6]从头开始查找，删除第一个

#7，sort()
# li=[1,2,3,5,6,7,0,4,67]
# li.sort()#默认升序
# print(li)#[0, 1, 2, 3, 4, 5, 6, 7, 67]
# li.sort(reverse=True)#降序
# print(li)#[67, 7, 6, 5, 4, 3, 2, 1, 0]
# li_str=['python','java','go','ruby']
# li_str.sort(key=len)#key指定按照什么标准进行排序
# print(li_str)#['go', 'java', 'ruby', 'python']如果长度一样，按照遍历的先后排序

#列表嵌套
# li=[[1,2,3,5,6,7,0,4,67],['python','java','go','ruby']]
# print(li[1][2])#go
# li[1].append('css')
# print(li)#[[1, 2, 3, 5, 6, 7, 0, 4, 67], ['python', 'java', 'go', 'ruby', 'css']]
# li[1].extend('hello')
# print(li)
# li.extend([10,11,12])
# print(li)