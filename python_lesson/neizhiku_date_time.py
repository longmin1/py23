
import datetime
# 获取当前的日期时间
# nowtime=datetime.datetime.now()
# print(nowtime)#2022-03-27 21:23:44.100233
# print(nowtime.day)#27  获取当前日
# print(nowtime.month)#3  获取当前月
# print(nowtime.year)#2022  获取当前年
# #转成时间戳
# print(nowtime.timestamp())#1648387518.35684
#
# #获取指定时间的时间
# print(datetime.datetime(2021,9,15))#2021-09-15 00:00:00
# print(datetime.datetime(2021,09,15))#09,15-->这样是不行的

'''时间 字符串和datetime互相转换'''

# s='2022-09-15 12:13:14'
# '''将字符串转换成datetime实例'''
# s1=datetime.datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
# print(s1)#2022-09-15 12:13:14
# s='2021:09:15 12:13:14'
# s1=datetime.datetime.strptime(s,'%Y:%m:%d %H:%M:%S')
# print(s1,type(s1))#2021-09-15 12:13:14  <class 'datetime.datetime'>
'''时间转换成字符串'''
# now=datetime.datetime.now()
# print(now,type(now))#2022-03-27 21:44:54.534326 <class 'datetime.datetime'>
# # now1=datetime.datetime.strftime(now,'%a,%b %d %H:%M')
# # print(now1,type(now1))#Sun,Mar 27 21:46 <class 'str'>
# now1=now.strftime('%a,%b %d %H:%M')
# print(now1,type(now1))#Sun,Mar 27 22:03 <class 'str'>

'''时间和时间戳互换'''
# now=datetime.datetime.now()
# print(now)#2022-03-27 21:55:31.632740
# now_shijianchuo=now.timestamp()
# print(now_shijianchuo)#1648389331.63274
#
# '''时间戳转成时间'''
# now_time=datetime.datetime.fromtimestamp(now_shijianchuo)
# print(now_time)#2022-03-27 21:57:01.981593


# import logging.config
# logging.config.fileConfig('log.ini')
# # logging.basicConfig(level=logging.INFO)
# logging.info('马上快要下雨了！')
a='2022-03-27 22:23:54,769 root  INFO     马上快要下雨了！'
now_time=datetime.datetime.now()
c_time_str=now_time.strftime('%Y%m%d_%H%M%S')
log_name=c_time_str+'.log'
with open(log_name,'w+',encoding='utf-8')as f:
    f.write(a)
