#老师整理的比较全的日志输出格式

import logging
'''纯英文的日志可以直接这样输出到文件中'''
# logging.basicConfig(filename='my1.log',
#                     level=logging.INFO,
#                     format='%(asctime)s [%(levelname)s %(message)s (%(filename)s:%(lineno)s)',datefmt='%m/%d/%Y %I:%M:%S %p')

'''如果有中文的话 需要这样解决 才能正常输出到文件中'''
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)
# file_handler=logging.FileHandler('my4.log',encoding='utf-8')
# fmt=logging.Formatter('%(asctime)s [%(levelname)s %(message)s (%(filename)s:%(lineno)s)',datefmt='%m/%d/%Y %I:%M:%S %p')
# file_handler.setFormatter(fmt)
# logger.handlers.append(file_handler)
# logger.info('xxxxx日志')
# logger.error('ddddd要下雨拉')


'''网上找的方法 也可以使用'''
# import logging
# logger = logging.getLogger()  # 实例化一个logger对象
# logger.setLevel(logging.INFO)  # 设置初始显示级别
#
# # 创建一个文件句柄---文件处理器---输入到文件中
# file_handle = logging.FileHandler("my3.log", encoding="UTF-8")
#
# # 创建一个流句柄---流处理器  可以输出到控制台的
# stream_handle = logging.StreamHandler()
#
# # 创建一个输出格式
# fmt = logging.Formatter(f"{'*'*28}\n"
#                         "> %(asctime)s\n"
#                         "> %(levelname)s - "
#                         "%(filename)s - "
#                         "[line:%(lineno)d]\n"
#                         f"{'-'*40}\n"
#                         "  %(message)s\n"
#                         f"{'-'*40}\n\n",
#                         datefmt="%a, %d %b %Y"
#                         "%H:%M:%S"
#                         )
#
# file_handle.setFormatter(fmt)  # 文件句柄设置格式
# # stream_handle.setFormatter(fmt)  # 流句柄设置格式
#
# logger.addHandler(file_handle)  # logger对象绑定文件句柄
# # logger.addHandler(stream_handle)  # logger对象绑定流句柄

# logger.info("这是程序运行过程中的一条提示")

'''日志的高阶用法'''
