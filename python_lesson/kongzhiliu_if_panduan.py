#2022.03.20
#python控制流——判断
#if
# bob='dev'
# if bob =='tester':
#     print('测试工程师')
# #else
# school='hogwarts'
# if school =='hogwarts':
#     print('hogwarts 测试开发')
# else:
#     print('测试开发')
#
# #elif
# food='apple'
# color='yellow'
# if food =='apple':
#     print('苹果')
#     if color=='yellow':
#         print('黄苹果')
# elif food=='banana':
#     print('香蕉')
#     if color=='yellow':
#         print('黄香蕉')
# elif food=='orange':
#     print('橘子')
#     if color=='yellow':
#         print('黄橘子')
# else:
#     print('其他未知食物')

#三目运算符
a,b=1,2
# if a>b:
#     school_1='hogwarts'
# else:
#     school_1='hogwarts2'
# print(school_1)

school_1='hogwarts' if a>b else 'hogwarts2'
print(school_1)

