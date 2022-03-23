#*args-->接收任意多个实际参数，并将其放在一个元组中
# def print_language(*args):#*接收所有参数
#     print(args)
#     for i in args:
#         print(i)
# # print_language('python','java','go')
# # print_language('python','java','php','rubby')
# list_1=['java','php','rubby']
# print_language(*list_1)#-->解包，列表中的每个元素都可以解包出来

#**kwargs--->把传进来的参数打包成字典形式
# def print_info(**kwargs):
#     print(kwargs)
# print_info(name='longmin',age=18)
# print_info(name='yangbin',age=26)
# dict_1={'name':'bobo','age':18,'score':98}
# print_info(**dict_1)