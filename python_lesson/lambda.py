
# import math
# #常规的代码
# def circle_area(r):
#     '''计算圆的面积，r--》半径'''
#     result=math.pi*r*r
#     return result
#
# # print(circle_area(10))
#
# #lambda表达式
# g=lambda r:math.pi*r*r
# # print(g(10))
#
# print(list(map(g, (10, 20, 40, 30))))


# tinydict = [[4, 2, 9], [1, 5, 6], [7, 8, 3]]
# print(sorted(tinydict, key=lambda x: x[0]))

dic = {
    'a': [1, 2, 3],
    'b': [2, 1, 1],
    'c': [3, 1, 2],
}
print(sorted(dic, key=lambda k: dic[k][2]))
# ['a', 'b', 'c']