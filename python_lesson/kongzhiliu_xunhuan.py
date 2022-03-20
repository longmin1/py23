#python 控制流-循环
# a=[1,2,3,4,5]#还可以是元组，字符串，字典，可迭代元素
# for i in a:
#     print(i)

#while循环

# while  --break
# for   ---break
# a=0
# while a<6:
#     print(a)
#     # if a==3:
#     #     break
#     a+=1
#     if a==3:
#         break
#break放在不同的地方 显示的结果也会不一样

# list_a=[1,2,3,4,5,6,7,8,9]
# for i in list_a:
#     print(i)
#     if i==3:
#         break

#continue
# while ---continue
# for ----continue
# b=1
# while b<7:
#     print(b)
#     if b==3:
#         b+=1.5
#         continue
#     b+=1

# for ----continue
# list_a=[1,2,3,4,5,6,7,8,9]
# for i in list_a:
#     if i==3:
#         continue
#     print(i)
# sum=0
# for i in range(1,101):
#     sum= i + sum
# print(sum)

# for i in range(1,101):
#     if i%2==0:
#         sum=sum+i
# print(sum)

# sum=0
# for i in range(0,101,2):
#     sum = sum + i
# print(sum)

# list_1=[i for i in range(0,101,2)]
# print(sum(list_1))
#
# print(sum([i for i in range(0,101,2)]))

#循环判断猜数字游戏，判断输入的类型是否是数字，不是就进行提示
# com_num=50
# a=True
# while a:
#     try:
#         a=int(input('请输入你猜想的数字： '))
#     except ValueError:
#         print("Int, please.")
#     if type(a)!=int:
#         print(type(a))
#         print('输入的要为整数数字')
#     elif type(a)==int:
#         print(type(a))
#         a=False
#         print('退出循环拉')
# if int(a)<com_num:
#     print('猜小了')
# elif int(a)>com_num:
#     print('猜大了')
# else:
#     print('对了')

# list_i=[i for i in range(1,101) if i %2!=0]
# print(sum(list_i))
i=0
a=1
while a<101:
    i = i + a
    a=a+1

print(i)


























