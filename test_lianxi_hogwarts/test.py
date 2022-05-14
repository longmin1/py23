'''回文是指一段数字或者文本，正着读和倒着读都是相同的，例如2002，110011都是回文数字。
请编写一个函数，接收2个数字n和m，找出大于数字n的m个有效回文数字，以列表的格式返回。
如果n本身也是回文数字，那么也算其中一个。单个数字不被视为回文数字。

【示例】
输入：6, 4
输出：[11, 22, 33, 44]
解释：6自身不算回文数字，继续往后找。直到找到11、22、33和44，一共4个有效的回文数字为止。'''
# def solution(n: int, m: int)-> list:
#     list_num=[]
#     while len(list_num)<m:
#         if n<10:
#             n=10
#         if n==int((str(n)[::-1])):
#             list_num.append(n)
#         n=n+1
#     return list_num


# print(solution(6, 4))
# print(solution(59,3))
# print(solution(101,2))
# assert solution(6, 4) == [11, 22, 33, 44]
# assert solution(59, 3) == [66, 77, 88]
# assert solution(101, 2) == [101, 111]
# def solution(num: int)-> bool:
#     a=int(str(num)[::-1])
#     return True if a ==num else False
import time

''':mage:‍ 回文是指一段数字或者文本，正着读和倒着读都是相同的，例如2002，110011都是回文数字。 
请编写一个函数，接收一个数字参数num，返回num中所有数字能够组成回文数字的列表，按升序排列，不允许重复。 个位数字和前后是0的数字（010和00）不被视为回文数字。如果不满足条件则返回空列表。

【示例】
输入：1221
输出：[22, 1221]
解释：数字1221中，1221整体是回文数字，22也是回文数字，因此按升序排列后为[22, 1221]。'''

# def solution(num: int)-> list:
#     list_1=[]
#     for i in range(len(str(num))):
#         for j in range(i+1,len(str(num))):
#             if str(num)[i:j+1]==str(num)[i:j+1][::-1] and str(num)[i]!='0':
#                 if len(str(num)[i:j+1])!=1:
#                     list_1.append(int(str(num)[i:j+1]))
#     list_1=sorted(list(set(list_1)))
#     return list_1
#
#
# print(solution(1221))
# print(solution(34322122))
# print(solution(1001331))
# print(solution(13598))

# def solution(r: int, g: int, b: int) -> str:
#     return ('%02X%02X%02X' % (r, g, b))
#
# print(solution(1,2,3))
# print(solution(255,255,255))
# print(solution(148,0,211))
'''给你一个整数n，且n>=3，请编写一个python函数，返回n（不含自己）以内所有的质数'''
'''质数，又称素数，是只能被1或者自己整除的自然数'''



# def find_prime(n) -> list:
#     list_1=[]
#     for i in range(2, n):
#         for y in range(2, i):
#             if i%y==0:
#                 break
#         else:
#             list_1.append(i)
#     return list_1
    # return [i for i in range(2, n) for y in range(3,n) if i==y and i%2 !=0 and 1%y==0 ]
    # list_1 = []
    # for i in range(2, n):
    #     for j in range(2, i):
    #         if (i % j) == 0:
    #             break
    #     else:
    #         list_1.append(i)
    # return list_1

# print(find_prime(10))
# assert find_prime(10) == [2, 3, 5, 7]
# assert find_prime(17) == [2, 3, 5, 7, 11, 13]
'''哈利波特最近收到一堆的数学作业，全是含有一个未知数x的等式，让我们编写一个函数帮他求出每个等式中的x的值吧。

【示例】
输入：x + 1 = 9 - 2
输出：6
解释：根据数学知识可以推断出x = 9-2-1，所以未知数x的值为6。'''
# def solution(str):
#     str_old = str.replace('x', '0').split('=')
#     print(str_old)
#     str_new = eval(str_old[1]) - eval(str_old[0])
#     print(str_new)
#     if str.find("x") < str.find("="):
#         return str_new
#     else:
#         return -str_new
# def solution(eq: str) -> int:
#     rz = eval(f'{eq.replace("=", "-(")})', {"x": 1j})
#     return -rz.real / rz.imag


# assert solution('x+1=9-2') == 6
# assert solution('x-2+3=2') == 1
# assert solution('-10=x') == -10
# assert solution('3*x - 123 + 12* (3 - x) = 12') == -11
# print(solution('- 10 = x'))
# print(solution('x + 1 = 9 - 2'))
# print(solution('x - 2 + 3 = 2'))
# print(solution('4 - 1 = 1 + x'))

# assert solution('x + 1 = 9 - 2') == 6
# assert solution('x - 2 + 3 = 2') == 1
# assert solution('- 10 = x') == -10

# def timeit(n):
#     def inner(func):
#         def wrapper(*args,**kwargs):
#             start_time=time.time()
#             for i in range(n):
#                 ret=func(i)
#             end_time=time.time()
#             print(end_time-start_time)
#             return i
#         return wrapper
#     return inner
#
# # @timeit(1000)
# def test_case(n):
#
#     print(f'这是装饰器的内部运行:{n}')
#
# a=timeit(1000)#a=inner
# b=a(test_case)#b=wrapper
# b()#--->运行函数  b()==wrapper()
# print(b())#--->print可以打印return i的值 999
# test_case(4)





















