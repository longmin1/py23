#用logging.conf  配置文件来输出logging日志
import logging.config
logging.config.fileConfig('logging.conf')
logger=logging.getLogger('main')#conf中logger对象中的main
logger.info('这是使用logging.conf打印的日志 ')